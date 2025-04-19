# app.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def chat_with_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    response = chat_with_ollama(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
