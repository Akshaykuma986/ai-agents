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
            print("AI:",responses["bye"])

            break
  #history command
        elif user_input == "history":
            print("AI : here is our conversation so far")
            for msg in memory["messages"]:
                print("-",msg)
            continue    

       
#smart keyword matching
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

