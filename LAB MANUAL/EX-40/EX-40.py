import re
def chatbot(text):
    text=text.lower()
    if re.search(r"\b(hi|hello|hey)\b",text):
        return "Hello! How can I help you?"
    elif "name" in text:
        return "I am a simple NLP chatbot."
    elif "how are you" in text:
        return "I am fine! Thank you."
    elif "your college" in text:
        return "I can help you with college-related questions."
    elif "bye" in text:
        return "Goodbye! Have a nice day!"
    elif "help" in text:
        return "Sure! Tell me what you need help with."
    else:
        return "Sorry, I did not understand. Please try again."
print("Chatbot Started! Type 'bye' to exit.")
while True:
    user=input("You: ")
    response=chatbot(user)
    print("Bot:",response)
    if re.search(r"\bbye\b",user.lower()):
        break
