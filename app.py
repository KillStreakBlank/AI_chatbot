# app.py
from flask import Flask, request, jsonify, abort
import openai
import os
import logging
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    logging.error("No OpenAI API key found")
    raise ValueError("No OpenAI API key found")

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    data = request.get_json() if request.method == 'POST' else {}
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a talkative chatbot that enjoys engaging in friendly conversations."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        abort(500, description="An error occurred while processing your request")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)