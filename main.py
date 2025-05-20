from flask import Flask, request
import openai
import os
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

openai.api_key = os.environ.get("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")

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "")
    response = MessagingResponse()

    if incoming_msg:
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": incoming_msg}]
            )
            reply = completion.choices[0].message["content"]
        except Exception as e:
            reply = f"Erro ao gerar resposta: {str(e)}"
    else:
        reply = "Não entendi sua mensagem."

    response.message(reply)
    return str(response)

if __name__ == "__main__":
    app.run()
