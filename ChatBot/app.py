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

Please provide helpful, accurate responses to customer inquiries.
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

    # Clean and validate user input
    user_input = user_input.strip()
    if len(user_input) > 2000:  # Limit input length
        return jsonify({"error": "Message too long"}), 400

    try:
        # Get limited chat history for context
        history = ChatHistory.query.order_by(ChatHistory.timestamp.desc()).limit(HISTORY_LIMIT).all()
        history = list(reversed(history))  # oldest → newest

        # Build a simple prompt instead of complex conversation history
        # This approach is more reliable for Gemini API
        conversation_context = ""
        
        # Add recent conversation context if available
        if history:
            conversation_context = "\n\nRecent conversation:\n"
            for h in history[-3:]:  # Only last 3 exchanges to avoid token limits
                conversation_context += f"Customer: {h.user}\nAssistant: {h.bot}\n"
        
        # Create the full prompt
        full_prompt = training_prompt + conversation_context + f"\n\nCurrent customer question: {user_input}\n\nAssistant:"

        headers = {"Content-Type": "application/json"}
        
        # Simplified payload structure
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": full_prompt
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 1000
            }
        }
        
        print(f"Payload being sent: {json.dumps(payload, indent=2)}")
        
    except Exception as e:
        print(f"Error preparing request: {str(e)}")
        return jsonify({"error": "Failed to prepare request"}), 500

    try:
        print(f"Sending request to Gemini API...")
        response = requests.post(GEMINI_URL, headers=headers, json=payload, timeout=30)
        
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 400:
            error_data = response.json() if response.text else {}
            print(f"400 Error details: {error_data}")
            return jsonify({
                "error": f"Bad request to API: {error_data.get('error', {}).get('message', 'Unknown error')}"
            }), 400
        elif response.status_code != 200:
            print(f"API Error: {response.status_code} - {response.text}")
            return jsonify({"error": f"API request failed: {response.status_code}"}), 500
            
        response_data = response.json()
        print(f"API Response: {response_data}")

        if "candidates" in response_data and len(response_data["candidates"]) > 0:
            if "content" in response_data["candidates"][0]:
                reply_text = response_data["candidates"][0]["content"]["parts"][0]["text"].strip()
            else:
                print("No content in API response")
                reply_text = "Sorry, I couldn't generate a response at this time."
        else:
            print("No candidates in API response")
            reply_text = "Sorry, I couldn't understand that. Please try rephrasing your question."

        # Save chat to database only if we got a valid response
        if reply_text and reply_text != "Sorry, I couldn't generate a response at this time.":
            new_chat = ChatHistory(user=user_input, bot=reply_text)
            db.session.add(new_chat)
            db.session.commit()
            print(f"Saved chat: User: '{user_input}' Bot: '{reply_text[:50]}...'")

        return jsonify({"reply": reply_text})
        
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timed out. Please try again."}), 500
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return jsonify({"error": "Network error occurred. Please try again."}), 500
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again."}), 500

# Test endpoint to verify API connection
@app.route("/test_api", methods=["GET"])
def test_api():
    """Simple endpoint to test if Gemini API is working"""
    if not API_KEY:
        return jsonify({"error": "API_KEY not found in environment variables"}), 400
    
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "Hello, please respond with 'API test successful'"
                    }
                ]
            }
        ]
    }
    
    try:
        response = requests.post(GEMINI_URL, headers=headers, json=payload, timeout=10)
        
        return jsonify({
            "status_code": response.status_code,
            "response": response.text,
            "api_key_present": bool(API_KEY),
            "api_url": GEMINI_URL
        })
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

# Optional: Clear chat history (useful for testing)
@app.route("/clear_history", methods=["POST"])
def clear_history():
    try:
        ChatHistory.query.delete()
        db.session.commit()
        return jsonify({"message": "Chat history cleared successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)