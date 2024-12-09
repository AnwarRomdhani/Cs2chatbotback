import os
import requests
import Env
Env.envset()
print(os.getenv('HUGGINGFACE_TOKEN'))

print()
api_url = "https://api-inference.huggingface.co/models/HuggingFaceTB/SmolLM2-1.7B-Instruct"
headers = {"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"}

response = requests.get(api_url, headers=headers)
print(response.status_code, response.text)
