import requests

URL = "http://127.0.0.1:8000/api/v1/users/"

# Prepare 10 fake users
users = [
    {"username": f"user{i}", "email": f"user{i}@example.com", "password": "pass123"}
    for i in range(1, 11)
]

for user in users:
    response = requests.post(URL, json=user)
    try:
        print(f"{user['username']} -> {response.status_code} | {response.json()}")
    except Exception:
        print(f"{user['username']} -> {response.status_code} | {response.text}")

