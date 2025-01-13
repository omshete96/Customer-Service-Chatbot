from flask import Flask, render_template, request

app = Flask(__name__)

# Define responses for common queries
responses = {
    "hello": "Hi there! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "how are you?": "I'm just a bot, but I'm functioning perfectly!",
    "help": "Sure! How can I help you today?",
    "what is your name?": "I'm your friendly customer service chatbot.",
    "thank you": "You're welcome! Let me know if you need anything else.",
    "how can I contact support?": "You can reach support at support@example.com.",
    "hours of operation": "We're open from 9 AM to 5 PM, Monday through Friday.",
    "payment options": "We accept credit cards, PayPal, and bank transfers.",
    "order status": "Please provide your order number to check the status."
}

# Initialize conversation history globally
history = []

@app.route("/", methods=["GET", "POST"])
def chat():
    global history

    if request.method == "POST":
        user_message = request.form["message"].lower()
        # Get bot response from predefined responses or default response
        bot_response = responses.get(user_message, "Sorry, I don't understand that.")
        history.append(("You", user_message))  # Add user message to history
        history.append(("Bot", bot_response))  # Add bot response to history

    return render_template("index.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)
