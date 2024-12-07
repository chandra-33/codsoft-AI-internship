import random
from datetime import datetime
def chatbotcha():
    print("Chatbot: Hi! I am your chatbot. Type 'exit' to end the conversation.")
    motivational_quotes = [
        "Believe in yourself and all that you are.",
        "Life is not just simple good experience",
    ]
    
    fun_facts = [
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not!",
    ]
    
    jokes = [
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? It had too many problems.",
    ]
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "weather" in user_input:
            print("Chatbot: I'm not connected to the internet right now, check in app!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm ready to help! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm your friendly chatbot! I don’t have a specific name yet.")
        elif "time" in user_input:
            now = datetime.now()
            print(f"Chatbot: The current time is {now.strftime('%H:%M:%S')}.")
        elif "python" in user_input:
            print("Chatbot: Python is a powerful, versatile programming language")
        elif "quote" in user_input or "motivate me" in user_input:
            print(f"Chatbot: Here's a motivational quote for you: \"{random.choice(motivational_quotes)}\"")
        elif "fact" in user_input:
            print(f"Chatbot: Did you know? {random.choice(fun_facts)}")
        elif "joke" in user_input:
            print(f"Chatbot: Here's a joke: {random.choice(jokes)}")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! It was nice talking to you.")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. Could you ask something else?")
chatbotcha()
