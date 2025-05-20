from flask import Flask, request
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    msg = data["Body"]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg}]
    )
    answer = response["choices"][0]["message"]["content"]
    return answer

if __name__ == "__main__":
    app.run()