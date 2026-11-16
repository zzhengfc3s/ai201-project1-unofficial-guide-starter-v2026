import json
import threading
from datetime import datetime, timezone

import config

_lock = threading.Lock()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def log_event(
    status_code: int,
    question: str,
    answer: str | None = None,
    refused: str | None = None,
    sources: list[str] | None = None,
    best_distance: float | None = None,
    threshold: float | None = None,
    tokens: dict[str, int] | None = None
) -> dict:
    entry = {
        "timestamp": _now(),
        "status_code": status_code,
        "question": question,
        "answer": answer,
        "refused": refused,
        "sources": sources,
        "best_distance": best_distance,
        "threshold": threshold,
        "prompt_tokens": tokens.get("prompt", 0),
        "output_tokens": tokens.get("output", 0),
        "corpus": config.CORPUS
    }
    return _append(entry)

def log_rejection(status_code: int, question: str, error: str, message: str) -> dict:
    return _append({
        "timestamp": _now(),
        "status_code": status_code,
        "question": question,
        "error": error,
        "message": message
    })


def _append(entry: dict) -> dict:
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry, ensure_ascii=False)
    with _lock:
        with config.AUDIT_LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    return entry
