import requests

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

def main():
    print("==================================================")
    print("Request Tests")
    print("==================================================\n")

    try:
        requests.get(f"{BASE_URL}/health", timeout=2)
    except requests.exceptions.ConnectionError:
        print("Make sure `serve.py` is running in another terminal.\n")
        return

    test_valid_question(1, "Which town is the easiest for walking?")
    test_valid_question(2, "When do the restaurants close?")
    test_valid_question(3, "Which town's market has been running the longest?")
    test_valid_question(4, "How many tram lines does Marchwood have?")
    test_valid_question(5, "What to see at Givens Mills?")
    test_valid_question(6, "Where to stay in Krestrelford?")
    test_valid_question(7, "What are the local eatery specialities?")
    test_valid_question(8, "Which local is best to vist in the summer?")
    test_valid_question(9, "How do I get to Pellew Sands?")
    test_valid_question(10, "Which town has a full hospital?")
    test_refused_question()
    test_bad_payload_1()
    test_bad_payload_2()
    test_bad_input()

if __name__ == "__main__":
    main()