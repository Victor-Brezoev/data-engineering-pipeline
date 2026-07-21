import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def extract_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    return data