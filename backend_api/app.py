import time
import random
import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

def generate_log():
    logs = [
        "Success",
        "Created",
        "Failed",
    ]
    return random.choice(logs)

@app.route('/api_1')
def api_call():
    log_message = generate_log()
    print(f"Operation log: {log_message}")
    time.sleep(0.5)  # Wait for half a second
    return f"completed: {log_message}"

@app.route('/health_check')
def health_check():
    return f"healthy"

@app.route('/download_external_logs')
def download_external_logs():
    # get the key from env if not use default
    external_integration_key = os.getenv('EXTERNAL_INTEGRATION_KEY', 'default_key')

    # setting up auth header
    headers = {
        'Authorization': f'Bearer {external_integration_key}'
    }
    external_api_url = "https://dummy-external-api.com/download_logs"

    # time to make a call and return accordingly
    try:
        response = requests.get(external_api_url, headers=headers)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
