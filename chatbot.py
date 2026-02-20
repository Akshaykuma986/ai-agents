#Take user input
#Store conversation history
#respond based on rules

#Stop when user types "bye"
import random
def chatbot():
    memory = { 
        "messages":[]
    }

    responses = {
    "hi": ["Hello 👋", "Hey there!", "Hi Akshay 😄"],
    "hello": ["Hi!", "Hello friend!", "Nice to see you!"],
    "how are you": ["I'm doing great!", "Feeling awesome!", "All good here!"]
}
    print("AI: Hello! Type 'bye' to exit.")

    while True :
        user_input =input("You :").lower()
        memory["messages"].append(user_input)
        #exit condition
        if user_input == "bye":
            print("AI:","goodbye")

            break
  #history command
        elif user_input == "history":
            print("AI : here is our conversation so far")
            for msg in memory["messages"]:
                print("-",msg)
            continue    

        if "sad" in user_input:
         print("AI: I'm sorry to hear that. Want to talk about it?")
         continue

        elif "happy" in user_input:
         print("AI: That’s great to hear! 😄")
         continue

        elif "tired" in user_input:
         print("AI: Maybe you should take some rest 💤")
         continue

        found = False

        for key in responses:
            if key in user_input:
             print("AI:",random.choice(responses[key]))   
             found = True
             break
        if not found:
         print("AI: I dont understand yet.")
     
#Store conversation history
chatbot()
#Count messages

#Remember what user said

