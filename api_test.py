import requests

# endpointy
ENDPOINTS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

def fetch_data(url):
    response = requests.get(url)
    return response.status_code, response.json()

def validate_response(status_code, data):
    if status_code == 200 and 'userId' in data:
        return True
    return False

def run_tests(endpoints):
    for index, url in enumerate(endpoints, start=1):
        status_code, data = fetch_data(url)
        if validate_response(status_code, data):
            print(f"Test {index}: PASSED")
        else:
            print(f"Test {index}: FAILED")

if __name__ == "__main__":
    run_tests(ENDPOINTS)
