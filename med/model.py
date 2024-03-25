import requests

API_URL = "https://api-inference.huggingface.co/models/Clinical-AI-Apollo/Medical-NER"
headers = {"Authorization": "Bearer your_token"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

