#Function Psuedo
import api_keys

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
            topic_choice = str(input("Enter the name of your trivia topic!:" \
                                    "\n1. Science" \
                                    "\n2. History" \
                                    "\n3. Sports" \
                                    "\n4. Music" \
                                    "\n5. Tech" \
                                    "\nPick a topic number: ")).capitalize()
        except ValueError:
            print("Please enter a topic name: \n")
            continue
        if topic_choice not in ["Science", "History", "Sports", "Music", "Tech"]:
            print("Invalid choice. Please select a topic choice.")
        else:
            print(f"You selected option {topic_choice}")
            return topic_choice
        
#-Difficulty choice input function
def game_difficulty():
    #Create a while loop for input validation
    while True:
        try:
            difficulty_choice = str(input("1. Easy" \
                                        "\n2. Medium" \
                                        "\n3. Hard" \
            "\nChoose Your Difficulty: ")).capitalize()
        except ValueError:
            print("Please enter a difficulty name: \n")
            continue
        if difficulty_choice not in ["Easy", "Medium", "Hard"]:
            print("Invalid choice. Please select a difficulty.")   
        else:
            print(f"You selected option {difficulty_choice}")
            return difficulty_choice

##game
def game_loop():
    while True:
        # Display each question and choices
        # Call function to ask for questions and difficulty choices
        topic_choice = game_topic()
        difficulty_choice = game_difficulty()

        # Build URL Based on previous answers

        url = api_keys.build_url(topic_choice, difficulty_choice)

        #PRINT URL JUST FOR TESTING REASONS
        print(url)

        #-answer check, score

        #-relay back score and acuracy, all at the end

        #-continue game function, yes continue, no exit
        replay_ask = input("Play another round? (Y/N): ").upper()

        if replay_ask == "N":
            break

        else:
            continue