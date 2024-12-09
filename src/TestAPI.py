import os
import requests
import Env
Env.envset()

h=os.getenv('HUGGINGFACE_TOKEN')
print(h)
print(f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}")
api_url = "https://api-inference.huggingface.co/models/HuggingFaceTB/SmolLM2-1.7B-Instruct"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}
payload = {"inputs": "Who are you"}

response = requests.post(api_url, headers=headers, json=payload)
print(response.status_code, response.json())
