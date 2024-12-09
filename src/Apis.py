from flask import Flask, jsonify, request
import requests
from Llmmodel import get_llm_response


app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow all origins
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    return response
# API endpoint to handle POST request and return a string
@app.route('/get-prompt', methods=['POST'])
def get_string():
    # Retrieve data from the POST request if needed
    data = request.get_json()
    msg=data['message']
    print("Received data:", msg)

    response=get_llm_response(msg)
    print(response)

    # Respond with a JSON object containing a string
    return jsonify({"message": response})



def run_server():
    app.run(debug=True, host='127.0.0.1', port=5000)


def send_prompt_to_api(prompt):

    api_url = "http://localhost:5001/receive-response"
    data = {"prompt": prompt}

    try:
        # Send the POST request to the API endpoint
        response = requests.post(api_url, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            print("Successfully sent the prompt!") 
        
            print("Response from API:", response.json())
        else:
            print(f"Failed to send prompt. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
run_server()