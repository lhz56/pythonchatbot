from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

set_pairs = [
    [r"my name is (.*)", ["Hello %1, How are you doing today?"]],
    [r"hi|hey|hello", ["Hello", "Hey there"]],
    [r"what is your name?", ["You can call me Lin's chatbot."]],
    [r"how are you ?", ["I am fine, thank you! How can I help you?"]],
    [r"I am fine, thank you", ["Great to hear that, how can I help you?"]],
    [r"i'm (.*) doing good", ["That's great to hear", "How can I help you? :)"]],
    [r"quit", ["Bye, take care. See you soon!"]],
    [r"who is your favorite football player?", ["Lionel Messi"]],
    [r"which football team do you support?", ["I support Arsenal FC! Who do you support?"]],
    [r"who is the best football player of all time?", ["Bad question, you know it's Messi"]],
    [r"what is the best football team in the world?", ["That depends on who you ask! Some say Real Madrid, Barcelona, or Manchester City."]],
    [r"when is the next world cup?", ["The next FIFA World Cup will be in 2026, hosted by the USA, Canada, and Mexico."]],
    [r"what is offside in football?", ["Offside is when an attacking player is ahead of the last defender before receiving the ball."]],
    [r"how many players are on a football team?", ["Each football team has 11 players on the field at one time."]],
    [r"who won the last world cup?", ["Argentina won the 2022 FIFA World Cup, defeating France in an epic final."]],
    [r"which country has won the most world cups?", ["Brazil has won the most World Cups with 5 titles."]],
]

chat = Chat(set_pairs, reflections)

def chatbot_response(user_input):
    if not user_input:
        return "I didn't understand that. Can you rephrase it?"
    return chat.respond(user_input)

app = Flask(__name__)

@app.route("/")
def home():
    print("Loading index.html...")
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    if not request.is_json:
        return jsonify({"error": "Invalid request format. Please send JSON."}), 400
    
    user_input = request.json.get("message", "")
    print(f"Received user input: {user_input}")
    
    if not user_input:
        return jsonify({"response": "I didn't understand that. Please try again."})
    
    response = chatbot_response(user_input)
    print(f"Chatbot response: {response}")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5001)  
