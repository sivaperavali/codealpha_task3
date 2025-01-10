import random 
import nltk 
from nltk.chat.util import Chat, reflections

# Download NLTK data (run this once if not already done)
# nltk.download('punkt')

# Define chatbot pairs (input patterns and corresponding responses)
chat_pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you?", "Hi there! What can I do for you?"]),
    (r"how are you|how's it going", ["I'm just a program, but I'm functioning perfectly!"]),
    (r"what is your name", ["I'm a simple chatbot created to assist you.", "You can call me ChatBot!"]),
    (r"can you help me", ["Of course! Tell me what you need help with."]),
    (r"thank you|thanks", ["You're welcome!", "No problem!"]),
    (r"quit", ["Goodbye! Have a great day!"]),
    (r".*", ["I'm not sure about that. Could you tell me more?", "Sorry, I don't understand. Can you rephrase?"])
]

# Define the chatbot
chatbot = Chat(chat_pairs, reflections)

def run_chatbot():
    print("Hello! I'm your basic chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
run_chatbot()
