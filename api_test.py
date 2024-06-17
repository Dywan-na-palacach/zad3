import requests
import json

# Lista endpointów do testowania
endpoints = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

# Funkcja do wysyłania żądania i sprawdzania odpowiedzi
def test_api(endpoint):
    response = requests.get(endpoint)
    http_code = response.status_code
    json_response = response.json()
    return http_code, json_response

# Testy
def run_tests():
    for i, endpoint in enumerate(endpoints):
        http_code, json_response = test_api(endpoint)
        if http_code == 200 and 'userId' in json_response:
            print(f"Test {i + 1}: PASSED")
        else:
            print(f"Test {i + 1}: FAILED")

if __name__ == "__main__":
    run_tests()
