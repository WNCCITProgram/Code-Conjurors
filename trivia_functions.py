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
        try:
            topic_choice = int(input("Enter the number for your trivia topic!:" \
                                    "\n1. Science" \
                                    "\n2. History" \
                                    "\n3. Sports" \
                                    "\n4. Music" \
                                    "\n5. Tech" \
                                    "\nPick a topic number: "))
        except ValueError:
            print("Please enter a number 1-5\n")
            continue
        if topic_choice in [1, 2, 3, 4, 5]:
            print(f"You selected option {topic_choice}")
            return topic_choice
        else:
            print("Invalid choice. Please select a topic number.")
        
#-Difficulty choice input function
def game_difficulty():
    #Create a while loop for input validation
    while True:
        try:
            difficulty_choice = int(input("1. Easy" \
                                        "\n2. Medium" \
                                        "\n3. Hard" \
            "\nChoose Your Difficulty:"))
        except ValueError:
            print("Please enter a number 1-3\n")
            continue
        if difficulty_choice in [1, 2, 3]:
            print(f"You selected option {difficulty_choice}")
            return difficulty_choice
        else:
            print("Invalid choice, Please select a difficulty number.")

        
#-fetch the questions based on input
def api_test(topic_choice, difficulty_choice):
    if topic_choice == 1 and difficulty_choice == 1:
        api_key = "Science&Easy"
    elif topic_choice == 1 and difficulty_choice == 2:
        api_key = "Science&Medium"
    elif topic_choice == 1 and difficulty_choice == 3:
        api_key = "Science&Hard"
    print(f"{api_key}")
    return api_key

##game
#-questions, choices
#-input
#-answer check, score

#-relay back score and acuracy, all at the end

#-continue game function, yes continue, no exit


# TEST

import api_keys

url = api_keys.build_url(17, "easy")

print(url)