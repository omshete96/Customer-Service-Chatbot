def get_response(user_message):
    responses = {
        "hello": "Hi there! Welcome to our customer service chatbot. How can I assist you today?",
        "bye": "Goodbye! Thank you for reaching out to us. Have a wonderful day!",
        "how are you?": "I'm just a bot, but I'm here to help you with anything you need!",
        "help": "Sure! You can ask me about order status, product details, returns, or anything else.",
        "order status": "Please provide your order ID, and I'll check the status for you.",
        "return policy": "You can return any item within 30 days of delivery. Would you like to start a return?",
        "payment methods": "We accept credit cards, debit cards, PayPal, and UPI. Do you need help with a specific payment method?",
        "shipping cost": "Shipping is free for orders above $50. For smaller orders, it's $5.",
        "delivery time": "Delivery typically takes 3-5 business days. Do you have a specific order you'd like me to check?",
        "track order": "Please provide your tracking number to get the latest updates on your shipment.",
        "product warranty": "Most of our products come with a one-year warranty. Let me know if you need warranty details for a specific item.",
        "contact support": "You can contact our support team at support@example.com or call us at 1-800-123-4567.",
        "offers": "Check out our latest offers on the homepage! Let me know if you'd like help finding them.",
        "cancel order": "Please provide your order ID so I can assist you with cancellation.",
        "refund status": "Refunds are processed within 5-7 business days. Do you have a specific refund you'd like me to check?",
        "thank you": "You're welcome! Let me know if there's anything else I can help with.",
    }

    return responses.get(user_message.lower(), "I'm sorry, I don't have an answer for that. Could you rephrase?")
