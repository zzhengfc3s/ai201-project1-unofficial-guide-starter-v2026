import requests

BASE_URL = "http://localhost:5000/ask"


def print_result(test_name: str, passed: bool, response: requests.Response):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")
    print(f"       Status: {response.status_code}, Body: {response.text.strip()}")

def test_valid_question():
    test_name = "Valid Question"
    payload = {"question": "Which town's market has been running the longest?"}
    response = requests.post(BASE_URL, json=payload)
    passed = response.status_code == 200
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

    test_valid_question()

if __name__ == "__main__":
    main()