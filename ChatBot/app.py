from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
import os, requests, json

load_dotenv()
app = Flask(__name__)

# Database config (SQLite file-based)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Chat History Model
class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.Column(db.Text, nullable=False)
    bot = db.Column(db.Text, nullable=False)

# Create DB tables
with app.app_context():
    db.create_all()

# Gemini API setup
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

# Get history limit from .env (default = 5)
HISTORY_LIMIT = int(os.getenv("CHAT_HISTORY_LIMIT", 5))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Empty input"}), 400

    # Get limited chat history for context
    history = ChatHistory.query.order_by(ChatHistory.timestamp.desc()).limit(HISTORY_LIMIT).all()
    history = list(reversed(history))  # oldest → newest

    # Build conversation history string
    conversation = ""
    for h in history:
        conversation += f"Customer: {h.user}\nAssistant: {h.bot}\n"

    # Add current user input
    prompt = training_prompt + "\n\n" + conversation + f"Customer: {user_input}\nAssistant:"

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        response = requests.post(GEMINI_URL, headers=headers, json=payload)
        response_data = response.json()

        if "candidates" in response_data:
            reply_text = response_data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            reply_text = "Sorry, I couldn't understand that."

        # Save chat to database
        new_chat = ChatHistory(user=user_input, bot=reply_text)
        db.session.add(new_chat)
        db.session.commit()

        return jsonify({"reply": reply_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optional: Get full chat history
@app.route("/history")
def history():
    chats = ChatHistory.query.order_by(ChatHistory.timestamp.asc()).all()
    history_data = [
        {"timestamp": c.timestamp.strftime("%Y-%m-%d %H:%M:%S"), "user": c.user, "bot": c.bot}
        for c in chats
    ]
    return jsonify(history_data)

if __name__ == "__main__":
    app.run(debug=True)

