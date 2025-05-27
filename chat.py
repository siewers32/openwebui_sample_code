import requests
from dotenv import load_dotenv
import os

load_dotenv()
# token = os.getenv("OPENWEBUI_API_KEY")
# url = 'http://localhost:8080/api/chat/completions'

token = os.getenv("MIEP_KEY")
url = 'https://ai.edutorial.nl/api/chat/completions'

def chat_with_model(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "Why is the sky blue?"
        }
      ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

print(chat_with_model(token, url))