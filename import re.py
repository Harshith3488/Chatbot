import re
import random

# Define some sample responses
responses = {
    "hello": ["Hello! How can I help you?", "Hi there! What's on your mind?", "Hey! How's it going?"],
    "how are you": ["I'm a bot, so I don't have feelings, but I'm here to help!", "I'm doing great! How about you?"],
    "name": ["I'm a chatbot created to assist you.", "My name is ChatBot!", "I'm just a friendly assistant."],
    "bye": ["Goodbye! Have a great day!", "See you soon!", "Take care!"],
}

# Function to get a random response based on keyword match
def get_response(user_input):
    user_input = user_input.lower()

    # Loop through keywords in responses to find a match
    for key in responses:
        if re.search(key, user_input):
            return random.choice(responses[key])

    return "I'm sorry, I don't understand that."

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
