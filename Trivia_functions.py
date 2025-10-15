#Function Psuedo

#-Display Game name function

def game_title():
    print("|----------------------------------------------------------|")
    print("|      WELCOME TO THE CODE CONJURORS TRIVIA CHALLENGE      |")
    print("|----------------------------------------------------------|")

#-Player name input function
def player_name():
    name = input("Enter your name: ")
    return name
    
##-Topic choice input function
def game_topic():
    #Create a while loop for input validation
    while True:
        topic_choice = int(input("Enter the number for your trivia topic!:" \
                                "\n1. Science" \
                                "\n2. History" \
                                "\n3. Sports" \
                                "\n4. Music" \
                                "\n5. Tech" \
                                "\nPick a topic number: "))
        if topic_choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice. Please select a topic number.")
        else:
            print(f"You selected option {topic_choice}")
            return {topic_choice}
        
#-Difficulty choice input function
def game_difficulty():
    difficulty = int(input("1. Easy" \
    "\n2. Medium" \
    "\n3. Hard" \
    "\nChoose Your Difficulty: "))
    return difficulty
#-fetch the questions based on input

##game
#-questions, choices
#-input
#-answer check, score

#-relay back score and acuracy, all at the end

#-continue game function, yes continue, no exit