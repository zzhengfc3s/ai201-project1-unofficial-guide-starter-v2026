#!/usr/bin/env python3
"""
The Unofficial Guide — the same pipeline, over HTTP.

    python serve.py                          run it locally on port 5000
    gunicorn serve:app                       run it the way a host runs it

Nothing new happens in this file. It is a wrapper: a request comes in, it
hands the question to `app.py::ask_pipeline` — the exact function the command
line uses — and hands the answer back as JSON. Retrieval, the relevance gate
and the grounded prompt all still live where they lived. If you change how
your system answers, you change it in those files and this one follows.

Two routes:

    POST /ask       {"question": "..."} in, the answer and its sources out
    GET  /health    is the service up, and is there an index to search

Why this exists: `app.py` runs once and exits, which is fine on your laptop
and impossible to deploy. A hosted service has to stay up and wait for
requests. This is the smallest thing that does that.

⚠️ There is deliberately no logging, no timing and no metrics in this file.
Unit 9 has you build the structured log yourself — the request line, the
timing field everyone skips, the whole instrument-before-you-deploy exercise.
Shipping a logger here would hand you the answer to that. Add yours in unit 9;
this file stays the bare shell until then.
"""

import os
import re

from flask import Flask, jsonify, request

import config
from generate import QuotaGuard
from store import index_exists

app = Flask(__name__)


def validate_question(text: str) -> tuple[bool, str]:
    """
    Returns:
        (is_valid: bool, error_message: str)
    """
    if not isinstance(text, str) or not text.strip():
        return False, "Send JSON with a non-empty 'question' string field."
    
    if len(text) > 5000:
        return False, f"Question exceeds maximum length of 5000 characters."
    
    if re.search(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', text):
        return False, "Question contains invalid control characters."
    
    words = re.findall(r'[a-zA-Z0-9]+', text)
    
    if not words:
        return False, "Question must contain words."
    
    latin_chars = len(re.findall(r'[a-zA-Z]', text))
    total_chars = len(text)
    if latin_chars / max(total_chars, 1) < 0.30:
        return False, "Question must be written primarily in plain English."

    max_word_len = max(len(w) for w in words)
    if max_word_len > 100:
        return False, "Question contains excessively long unspaced strings."

    return True, ""

@app.get("/health")
def health():
    """Is the service up, and is there an index to search?

    Two different questions, and the second one is the one that bites. A
    freshly deployed service answers this route happily while every /ask
    returns "no index" — hosts give you no disk that survives a restart, so
    the index has to be built as part of getting the service up. Checking
    here means you find that out in one request instead of five.
    """
    ready = index_exists(config.CORPUS)
    return jsonify(
        {
            "status": "ok",
            "corpus": config.CORPUS,
            "index_ready": ready,
            "detail": (
                "ready"
                if ready
                else "no index for this corpus — run `python app.py index`"
            ),
        }
    )


@app.post("/ask")
def ask():
    """One question in, one grounded answer out.

    A refused question is a 200, not an error. The gate refusing is your
    system working — it is an answer, and the JSON says so with
    `"refused": true` so whatever calls this can tell the two apart.
    """
    from app import ask_pipeline

    payload = request.get_json(silent=True) or {}

    if not isinstance(payload, dict):
        return jsonify({
            "error": "bad_request",
            "message": "Request must be a valid JSON object"
        }), 400

    question = payload.get("question")
    is_valid, error_message = validate_question(question)
    if not is_valid:
        return jsonify({
            "error": "bad_request",
            "message": error_message
        }), 400

    if not index_exists(config.CORPUS):
        return jsonify({
            "error": "index_not_ready",
            "message": "No index for this corpus"
        }), 500

    try:
        outcome = ask_pipeline(question, corpus=config.CORPUS)
    except RuntimeError as exc:
        return jsonify({
            "error": "runtime_error",
            "message": f"{type(exc).__name__}: {exc}"
        }), 500
    except QuotaGuard as exc:
        return jsonify({
            "error": "quota_guard_error",
            "message": f"{type(exc).__name__}: {exc}"
        }), 500
    except Exception as exc:  # noqa: BLE001 — a reader gets this, not a traceback
        return jsonify({
            "error": "unexpected_error",
            "message": f"{type(exc).__name__}: {exc}"
        }), 500

    return jsonify({
            "question": question,
            "answer": outcome["answer"],
            "refused": outcome["refused"],
            "sources": outcome["sources"],
            "best_distance": round(outcome["best_distance"], 4),
            "threshold": outcome["threshold"],
            "corpus": config.CORPUS,
        }), 200


def main():
    # Hosts tell you which port to listen on through PORT, and they expect you
    # on 0.0.0.0. Binding 127.0.0.1 instead works perfectly on your laptop and
    # then answers nothing at all once deployed, because the host's router
    # can't reach a socket that only accepts connections from inside the
    # container. It is the single most common way a first deploy "succeeds"
    # and is unreachable.
    port = int(os.getenv("PORT", "5000"))

    # Debug mode reloads on save, which is handy, and prints a console that
    # runs arbitrary code, which is not something to leave switched on where
    # strangers can reach it. Off unless you ask for it.
    debug = os.getenv("AI201_DEBUG", "0") == "1"

    print(f"Serving The Unofficial Guide on http://localhost:{port}")
    print(f"Corpus: {config.CORPUS}    (Ctrl-C to stop)\n")
    print("Try it from another terminal:\n")
    print(f"  curl http://localhost:{port}/health")
    print(
        f"  curl -X POST http://localhost:{port}/ask \\\n"
        f"    -H 'Content-Type: application/json' \\\n"
        f"    -d '{{\"question\": \"is the housing lottery random?\"}}'\n"
    )

    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == "__main__":
    main()
