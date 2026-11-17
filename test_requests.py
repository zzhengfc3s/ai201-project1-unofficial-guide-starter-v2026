import requests
import json
import os
import config
import store

BASE_URL = "http://localhost:5000/ask"

def print_result(test_name: str, passed: bool, response: requests.Response):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")
    print(f"       Status: {response.status_code}, Body: {response.text.strip()}")

def test_valid_question(num: int, question: str):
    test_name = f"Valid Question {num}"
    payload = {"question": question}
    response = requests.post(BASE_URL, json=payload)
    passed = response.status_code == 200
    print_result(test_name, passed, response)

def test_refused_question():
    test_name = "Refused Question"
    payload = {"question": "What is the capital of Mongolia?"}
    response = requests.post(BASE_URL, json=payload)
    passed = response.status_code == 200
    print_result(test_name, passed, response)

def test_bad_payload_1():
    test_name = "Bad Payload 1"
    response = requests.post(BASE_URL, json=[1, 2, 3], headers={"Content-Type": "application/json"})
    passed = response.status_code == 400
    print_result(test_name, passed, response)

def test_bad_payload_2():
    test_name = "Bad Payload 2"
    payload = {"id": "28357"}
    response = requests.post(BASE_URL, json=payload)
    passed = response.status_code == 400
    print_result(test_name, passed, response)

def test_bad_input():
    test_name = "Bad Input - Whitespaces"
    payload = {"question": "    "}
    response = requests.post(BASE_URL, json=payload)
    passed = response.status_code == 400
    print_result(test_name, passed, response)

# ─── AI Gen'd Tests ───────────────────────────────────────────────────────────────────
def print_result_criteria(test_name: str, passed: bool, details: str = ""):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")
    print(f"       {details}")

def read_audit_log() -> list[dict]:
    """Helper to read structured entries from the audit log file."""
    if not os.path.exists(config.AUDIT_LOG):
        return []
    entries = []
    with open(config.AUDIT_LOG, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    entries.append(json.loads(line.strip()))
                except json.JSONDecodeError:
                    pass
    return entries

def test_criteria_1_malformed_payloads() -> bool:
    """
    Criteria 1: Given 5 malformed or invalid POST payloads, 100% returns a 400 error response with structured JSON body.
    """
    print("\n--- Criteria 1: Malformed & Invalid POST Payloads ---")
    bad_payloads = [
        ("JSON Array Payload", [1, 2, 3]),
        ("Missing Question Field", {"id": "28357"}),
        ("Empty Whitespace Question", {"question": "    "}),
        ("Control Characters", {"question": "Hello\x00World"}),
        ("No Meaningful Words", {"question": "???!!!"}),
    ]

    all_passed = True
    for name, payload in bad_payloads:
        if isinstance(payload, list):
            response = requests.post(
                BASE_URL,
                json=payload,
                headers={"Content-Type": "application/json"},
            )
        else:
            response = requests.post(BASE_URL, json=payload)

        is_400 = response.status_code == 400
        is_json = False
        try:
            body = response.json()
            is_json = isinstance(body, dict) and (
                "error" in body or "message" in body
            )
        except Exception:
            is_json = False

        passed = is_400 and is_json
        if not passed:
            all_passed = False

        print_result_criteria(
            f"Payload: {name}",
            passed,
            f"Status: {response.status_code}, Body: {response.text.strip()}",
        )

    print_result_criteria("Criteria 1 Overall Result", all_passed)
    return all_passed

def test_criteria_2_request_logging() -> bool:
    """
    Criteria 2: Given 5 requests (valid question or bad input), 100% of requests are logged.
    """
    print("\n--- Criteria 2: Request Logging Verification ---")
    initial_log_count = len(read_audit_log())

    test_payloads = [
        {"question": "Which town is the easiest for walking?"},
        {"question": "    "},  # Bad input
        {"question": "When do the restaurants close?"},
        {"id": "invalid_payload"},  # Bad payload
        {"question": "What to see at Givens Mills?"},
    ]

    for payload in test_payloads:
        requests.post(BASE_URL, json=payload)

    final_logs = read_audit_log()
    new_logs_count = len(final_logs) - initial_log_count
    passed = new_logs_count == 5

    print_result_criteria(
        "Criteria 2 Overall Result",
        passed,
        f"Logged requests: {new_logs_count}/5 (Initial: {initial_log_count}, Final: {len(final_logs)})",
    )
    return passed

def test_criteria_3_unindexed_corpus() -> bool:
    """
    Criteria 3: Given valid request against a corpus that's not indexed,
    100% of request returns a 500 JSON error response mentioning to run python app.py index.
    """
    print("\n--- Criteria 3: Unindexed Corpus Guard ---")
    payload = {"question": "Which town is the easiest for walking?"}

    # Execute request against serve.py
    response = requests.post(BASE_URL, json=payload)

    status_is_500 = response.status_code == 500
    contains_index_msg = "python app.py index" in response.text.lower()
    is_json = False
    try:
        body = response.json()
        is_json = isinstance(body, dict) and "error" in body
    except Exception:
        is_json = False

    passed = status_is_500 and contains_index_msg and is_json
    print_result_criteria(
        "Criteria 3 Overall Result",
        passed,
        f"Status: {response.status_code}, Body: {response.text.strip()}",
    )
    return passed

def test_criteria_4_quota_limit() -> bool:
    """
    Criteria 4: Given the quota limit is 3, a request hitting the quota limit,
    the 4th request returns a 500 JSON error response.
    """
    print("\n--- Criteria 4: Quota Limit Enforcement ---")

    # Send 3 valid requests to fill quota budget
    for i in range(1, 4):
        requests.post(
            BASE_URL, json={"question": f"Which town is the easiest for walking? {i}"}
        )

    # 4th request should exceed quota limit and return 500 JSON error
    response_4th = requests.post(
        BASE_URL, json={"question": "4th request exceeding quota budget. Which town is the easiest for walking?"}
    )

    is_500 = response_4th.status_code == 500
    is_json = False
    try:
        body = response_4th.json()
        is_json = isinstance(body, dict) and (
            body.get("error") == "quota_guard_error" or "QuotaGuard" in response_4th.text
        )
    except Exception:
        is_json = False

    passed = is_500 and is_json
    print_result_criteria(
        "Criteria 4 Overall Result",
        passed,
        f"4th Request Status: {response_4th.status_code}, Body: {response_4th.text.strip()}",
    )
    return passed

def test_criteria_5_token_usage_limit() -> bool:
    """
    Criteria 5: Given 5 valid requests, the sum of the 5th request log's prompt and output token value is less than 6,000.
    """
    print("\n--- Criteria 5: Token Usage Cap on 5th Request ---")
    valid_questions = [
        "Which town is the easiest for walking?",
        "When do the restaurants close?",
        "Which town's market has been running the longest?",
        "How many tram lines does Marchwood have?",
        "What to see at Givens Mills?",
    ]

    for q in valid_questions:
        requests.post(BASE_URL, json={"question": q})

    logs = read_audit_log()
    if not logs:
        print_result_criteria("Criteria 5 Overall Result", False, "No log records found.")
        return False

    # Get the latest entry corresponding to the 5th request
    fifth_log = logs[-1]
    prompt_tokens = fifth_log.get("prompt_tokens", 0)
    output_tokens = fifth_log.get("output_tokens", 0)

    total_tokens = prompt_tokens + output_tokens
    passed = total_tokens < 6000

    print_result_criteria(
        "Criteria 5 Overall Result",
        passed,
        f"5th Request Token Sum: {total_tokens} (Prompt: {prompt_tokens}, Output: {output_tokens}) < 6,000",
    )
    return passed

def main():
    print("==================================================")
    print("Criteria Acceptance Tests")
    print("==================================================\n")

    # try:
    #     requests.get("http://localhost:5000//health", timeout=2)
    # except requests.exceptions.ConnectionError:
    #     print("Make sure `serve.py` is running in another terminal.\n")
    #     return

    # test_valid_question(1, "Which town is the easiest for walking?")
    # test_valid_question(2, "When do the restaurants close?")
    # test_valid_question(3, "Which town's market has been running the longest?")
    # test_valid_question(4, "How many tram lines does Marchwood have?")
    # test_valid_question(5, "What to see at Givens Mills?")
    # test_valid_question(6, "Where to stay in Krestrelford?")
    # test_valid_question(7, "What are the local eatery specialities?")
    # test_valid_question(8, "Which local is best to vist in the summer?")
    # test_valid_question(9, "How do I get to Pellew Sands?")
    # test_valid_question(10, "Which town has a full hospital?")
    # test_refused_question()
    # test_bad_payload_1()
    # test_bad_payload_2()
    # test_bad_input()

    # test_criteria_5_token_usage_limit()
    # for i in range(1, 4):
    #     test_criteria_1_malformed_payloads()
    # for i in range(1, 4):
    #     test_criteria_2_request_logging()
    # test_criteria_4_quota_limit()
    # store.reset()
    # test_criteria_3_unindexed_corpus()

if __name__ == "__main__":
    main()