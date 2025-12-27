from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # <--- важно

app = Flask(__name__)
CORS(app)  # <--- разрешава всички origin по default

@app.route("/api/virtual-board")
def virtual_board():
    stop_code = request.args.get("stop_code")
    if not stop_code:
        return jsonify({"error": "stop_code is required"}), 400

    url = "https://sofiatraffic-proxy.onrender.com/v2/virtual-board"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Origin": "http://127.0.0.1:1234"
    }

    r = requests.get(url, params={"stop_code": stop_code}, headers=headers, timeout=10)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
