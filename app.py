from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are StratGenie, a strategic AI for creative agencies."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=1000
        )
        return jsonify({"result": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
