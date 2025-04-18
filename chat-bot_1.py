def chatbot_response(user_input):
    """Simple chatbot that responds to basic greetings."""
    responses = {
        "hello": "Hi there! How can I assist you?",
        "hi": "Hello! What would you like to ask?",
        "how are you": "I'm just a bot, but I'm feeling great! 😊",
        "bye": "Goodbye! Have a nice day!",
    }
    
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")

if __name__ == "__main__":
    print("Simple Chat Bot 🤖 (Type 'bye' to exit)")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() == "bye":
            print("Bot: See you later!")
            break
        print("Bot:", chatbot_response(user_message))
