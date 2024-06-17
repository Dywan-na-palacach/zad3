import requests
import json

def send_request(url, expected_status, expected_keys):
    print(f"Testing endpoint: {url}")
    
    response = requests.get(url)
    if response.status_code != expected_status:
        print(f"Test FAILED: Expected status {expected_status} but got {response.status_code}")
        return False
    
    print(f"HTTP Status OK: {response.status_code}")

    response_json = response.json()
    if isinstance(response_json, list):
        response_json = response_json[0]

    for key in expected_keys:
        if key not in response_json:
            print(f"Test FAILED: Missing key '{key}' in response")
            return False

    print("All expected keys are present.")
    return True

# Test 1: GET /posts
test_1 = send_request("https://jsonplaceholder.typicode.com/posts", 200, ["userId", "id", "title"])
print("Test 1: PASSED" if test_1 else "Test 1: FAILED")

# Test 2: GET /comments
test_2 = send_request("https://jsonplaceholder.typicode.com/comments", 200, ["postId", "id", "name", "email"])
print("Test 2: PASSED" if test_2 else "Test 2: FAILED")

# Test 3: GET /users
test_3 = send_request("https://jsonplaceholder.typicode.com/users", 200, ["id", "name", "username", "email"])
print("Test 3: PASSED" if test_3 else "Test 3: FAILED")
