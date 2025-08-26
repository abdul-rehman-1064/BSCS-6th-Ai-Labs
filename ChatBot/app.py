from flask import Flask, render_template, request, jsonify
import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Load training prompt
with open("training.json", "r") as f:
    config = json.load(f)

training_prompt = f"""
You are a helpful assistant for '{config['store_name']}'.
Only answer questions related to {config['department']}.
{config['prompt']}
"""

# Load chat history
HISTORY_FILE = "history.json"
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        chat_history = json.load(f)
else:
    chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Empty input"}), 400

    prompt = training_prompt + "\n\nCustomer: " + user_input

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_URL, headers=headers, json=payload)
        response_data = response.json()

        if "candidates" in response_data:
            reply_text = response_data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            reply_text = "Sorry, I couldn't understand that."

        # Save history
        chat_history.append({
            "timestamp": str(datetime.now()),
            "user": user_input,
            "bot": reply_text
        })

        with open(HISTORY_FILE, "w") as f:
            json.dump(chat_history, f, indent=2)

        return jsonify({"reply": reply_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
