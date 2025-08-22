import spacy
import random

# Load English model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
intents = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning"],
        "responses": ["Hi there!", "Hello!", "Hey! How can I help you?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "No problem!", "Glad to help!"]
    },
    "about": {
        "keywords": ["who are you", "what are you", "your name"],
        "responses": ["I'm a chatbot built using spaCy!", "Your AI helper."]
    },
    "unknown": {
        "responses": ["Sorry, I didn't get that.", "Can you rephrase?", "I'm not sure I understand."]
    }
    
}

# Function to match user input
def match_intent(user_input):
    doc = nlp(user_input.lower())
    tokens = [token.text for token in doc]

    for intent, data in intents.items():
        for keyword in data.get("keywords", []):
            if keyword in user_input.lower():
                return random.choice(data["responses"])

    return random.choice(intents["unknown"]["responses"])


# Chat loop
print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("🤖 Chatbot:", random.choice(intents["goodbye"]["responses"]))
        break

    response = match_intent(user_input)
    print("🤖 Chatbot:", response)
