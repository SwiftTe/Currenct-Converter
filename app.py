from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

@app.route('/api/rates', methods=['GET'])
def get_exchange_rates():
    try:
        response = requests.get(BASE_URL)
        data = response.json()
        if response.status_code == 200:
            return jsonify(data["conversion_rates"])
        else:
            return jsonify({"error": data.get("error-type", "Failed to fetch rates")}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
