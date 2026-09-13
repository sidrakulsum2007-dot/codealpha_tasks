# CodeAlpha Task 4 - Basic Chatbot

# Function to generate chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # 1. Hello
    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    # 2. How are you?
    elif "how are you" in user_input:
        return "I'm fine, thanks! How are you?"

    # 3. I'm fine
    elif "i'm fine" in user_input or "im fine" in user_input:
        return "That's great to hear!"

    # 4. What is your name?
    elif "what is your name" in user_input:
        return "I'm a simple Python chatbot."

    # 5. Weather
    elif "weather" in user_input:
        return "Sorry, I cannot check live weather."

    # Goodbye
    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    # Unknown input
    else:
        return "Sorry, I don't understand that."


# Welcome message
print("================================")
print("        BASIC CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.")
print()

# Main chatbot loop
while True:

    # Get input from the user
    user_input = input("You: ")

    # Get chatbot response
    response = chatbot_response(user_input)

    # Display chatbot response
    print("Bot:", response)

    # Stop the chatbot when user says bye
    if user_input.lower().strip() == "bye":
        break

print("\nThank you for chatting!")