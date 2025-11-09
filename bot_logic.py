import random
import json
import nltk
from nltk.stem import WordNetLemmatizer

# Download required nltk data
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents data
with open('intents.json') as file:
    data = json.load(file)

def clean_sentence(sentence):
    words = nltk.word_tokenize(sentence.lower())
    return [lemmatizer.lemmatize(word) for word in words]

def chatbot_response(user_input):
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm sorry, I didn’t understand that. Could you rephrase?"
