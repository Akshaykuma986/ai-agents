#Take user input
#Store conversation history
#respond based on rules

#Stop when user types "bye"
def chatbot():
    memory = {
        "messages": []
    }

    print("AI: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        memory["messages"].append(user_input)

        if user_input == "bye":
            print("AI: Goodbye 👋")
            break

        elif "hello" in user_input:
            print("AI: Hi there!")

        elif "how are you" in user_input:
            print("AI: I'm doing great 😄")
        elif "history" in user_input:
            print("AI : Here is your conversation so far:")
            for msg in memory["messages"]:
             print("-",msg)
        else:
            print("AI: I don't understand that yet.")

    print("Conversation history:", memory["messages"])

chatbot()


#Store conversation history

#Count messages

#Remember what user said

