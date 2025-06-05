import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nlp = spacy.load("en_core_web_sm")

questions = [
    "What is the weather like?",
    "How are you?",
    "What is your name?",
    "What's up?",
    "Hello!",
    "Can you help me?",
    "What time is it?",
    "What can you do?",
    "Tell me a joke!",
    "What's the date today?",
    "How's it going?",
    "What is your favorite color?",
    "Can you sing?",
    "Where are you from?",
    "What is the capital of France?",
    "Do you like to chat?",
    "What's your purpose?",
    "How old are you?",
    "Can you tell me about yourself?",
    "What is the meaning of life?",
    "Do you know any fun facts?",
    "What is your favorite food?",
    "Are you human?",
    "Can you speak other languages?"
]

responses = [
    "Tell me your location, and I can check the weather!",
    "I'm doing great, thanks for asking!",
    "I'm Chatty, your friendly chatbot!",
    "Not much, just chilling in the digital world. What's up with you?",
    "Hey there! Nice to see you!",
    "Of course, I'm here to assist. What's on your mind?",
    "I don't have a clock, but you can check the time on your device!",
    "I can chat, answer questions, tell jokes, and maybe even share some fun facts!",
    "Why did the scarecrow become a motivational speaker? Because he was outstanding in his field!",
    "I think it's June 5, 2025, but you might want to double-check!",
    "Pretty good, thanks! How about you?",
    "I like all colors, but if I had to pick, I'd say binary blue!",
    "I can't sing, but I can hum some binary tunes: 010101!",
    "I'm from the cloud, born in a server far, far away.",
    "The capital of France is Paris!",
    "I love chatting with humans like you!",
    "My purpose is to help answer your questions and bring a smile to your face!",
    "I'm ageless, existing in the timeless realm of code.",
    "I'm Chatty, a chatbot designed to assist and entertain with my vast digital knowledge!",
    "42, of course! Or maybe it's just to have a good chat.",
    "Did you know that octopuses have three hearts? Pretty cool, right?",
    "I don't eat, but I'd probably pick digital pizza if I could!",
    "Nope, I'm a friendly AI, not a human, but I love hanging out with you!",
    "I can understand many languages, but I stick to English for now. What's your favorite language?"
]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


def get_response(user_input):
    if not user_input or not isinstance(user_input, str):
        return "Sorry, I didn't receive a valid input. Please try again."

    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, question_vectors)
    best_match_idx = similarities.argmax()

    if similarities[0][best_match_idx] < 0.1:
        return "Sorry, I didn't understand. Can you clarify?"
    return responses[best_match_idx]
