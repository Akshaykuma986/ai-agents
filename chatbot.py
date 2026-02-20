#Take user input
#Store conversation history
#respond based on rules

#Stop when user types "bye"
def chatbot():
    print("AI: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input  == "bye":
            print("AI: Goodbye")
            break
        elif "hello" in user_input:
            print("AI: Hi there!")

        elif "i love rachana or not" in user_input:
            print("AI: of course i know you love rachana forever!")    
        
        elif "How are you" in user_input:
            print("AI: I'm just code ,but I'm doing Great")
        elif "can i ask something" in user_input:
            print("yeah you can ask anything")
        else:
            print("AI: I dont understand that yet.")
chatbot()