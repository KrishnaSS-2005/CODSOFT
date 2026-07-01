print("========================================")
print("      WELCOME TO MY CHATBOT")
print("========================================")
print("Type 'bye' to exit the chatbot.\n")

while True:

    user = input("You : ")

    user = user.lower()

    if user == "hello":
        print("Bot : Hello! Nice to meet you.")

    elif user == "hi":
        print("Bot : Hi! How can I help you?")

    elif user == "how are you":
        print("Bot : I am doing well. Thank you!")

    elif user == "what is your name":
        print("Bot : My name is CodeBot.")

    elif user == "who created you":
        print("Bot : I was created by Krishna for the CODSOFT AI Internship.")

    elif user == "what can you do":
        print("Bot : I can answer simple questions based on predefined rules.")

    elif user == "thank you":
        print("Bot : You're welcome!")

    elif user == "bye":
        print("Bot : Goodbye! Have a wonderful day.")
        break

    else:
        print("Bot : Sorry, I don't understand that question.")
