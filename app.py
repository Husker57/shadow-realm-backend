from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ====================== GOOGLE SHEET SETUP ======================
# Replace with your actual Google Sheet ID (the long string in the URL)
SHEET_ID = "YOUR_GOOGLE_SHEET_ID_HERE"   # ←←← CHANGE THIS

@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.form.to_dict() if request.form else request.get_json(force=True)
        
        tier = data.get('tier', 'free')
        name = data.get('name', '')
        email = data.get('email', '')
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        # Simple row to append to "Shadow Realm Earnings" Sheet1
        row = [timestamp, name, email, tier, "New Subscriber", "", ""]

        # TODO: Replace this with your actual Google Sheets append code
        # For now, we log it so you can see it's working
        print(f"✅ SIGNUP RECEIVED → {row}")
        
        return jsonify({"status": "success", "message": "Subscriber saved"}), 200

    except Exception as e:
        print(f"Signup error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# ====================== CHAT & VOICE ROUTES ======================
@app.route('/chat', methods=['POST'])
def chat():
    return jsonify({"reply": "Chat route is active"})

@app.route('/voice', methods=['POST'])
def voice():
    return jsonify({"status": "voice route active"})

@app.route('/', methods=['GET'])
def home():
    return "Shadow Realm Backend is running ✅"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
