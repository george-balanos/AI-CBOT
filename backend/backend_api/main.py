import requests

BASE_URL = "http://localhost:8000"

def test_put_query(user_id: str, text: str):
    url = f"{BASE_URL}/query/{user_id}"
    payload = {"text": text}
    headers = {"Content-Type": "application/json"}

    response = requests.put(url, json=payload, headers=headers)

    print(f"\nRequests to: {url}")
    print("Status: ", response.status_code)
    print("Response: ", response.json())

def test_get_message_history():
    url = f"{BASE_URL}/messages"

    response = requests.get(url)

    all_messages = response.json()

    for user_id in all_messages.keys():
        print(f"User -> {user_id}")
        for msg in all_messages[user_id]:
            print(f"Message: {msg}")
        print()
        print()

if __name__ == "__main__":
    test_put_query("user123", "Hello, how are you?")
    test_put_query("user123", "What's the weather?")
    test_put_query("user456", "Tell me a joke.")

    test_get_message_history()
