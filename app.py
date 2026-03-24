from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"response": "Invalid request"})

    user_input = data["message"].strip()

    print("User:", user_input)

    response = bot.generate_response(user_input)

    print("Bot:", response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)