# task8_chatbot.py
print("🤖 ChatBot: Hi! I’m PyBot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("PyBot: Hello there! How are you doing?")
    elif "how are you" in user:
        print("PyBot: I'm just code, but feeling productive today! 😄")
    elif "name" in user:
        print("PyBot: I’m PyBot, your Python assistant.")
    elif "weather" in user:
        print("PyBot: I can’t check weather yet, but it’s always sunny in Python ☀️")
    elif "help" in user:
        print("PyBot: Sure! You can ask about Python, AI, or just say hello.")
    elif user in ["bye", "exit", "quit"]:
        print("PyBot: Goodbye! Have a great day! 👋")
        break
    else:
        print("PyBot: Sorry, I didn't understand that. Try again?")
