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
                                    "\n1. Science" \
                                    "\n2. History" \
                                    "\n3. Sports" \
                                    "\n4. Music" \
                                    "\n5. Tech" \
                                    "\nPick a topic number: "))
        except ValueError:
            continue
        else:
            print(f"You selected option {topic_choice}")
            return topic_choice
            
        
#-Difficulty choice input function
def game_difficulty():
    #Create a while loop for input validation
    while True:
        try:
                                        "\n2. Medium" \
                                        "\n3. Hard" \
            "\nChoose Your Difficulty:"))
        except ValueError:
            continue
            print(f"You selected option {difficulty_choice}")
            return difficulty_choice
        else:

        
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
def build_api(topic_choice, difficulty_choice):

    #Find category ID from name
    category_id = None
    for name, cid in CATEGORIES_LIST:
        if name.lower() == game_topic.lower():
            category_id = cid
            break

    #Validate difficulty
    if game_difficulty.lower() not in DIFFICULTIES_LIST:
        raise ValueError("Invalid response. Choose Easy, Medium, or Hard.")
    
    #Build API
    if category_id is None:
        raise ValueError("Invalid category name. Choose from the list of topics.")
    
    api_url = (
        f"{BASE_URL}?amount={DEFAULT_AMOUNT}"
        f"&game_topic={category_id}"
        f"&game_difficulty={difficulty_choice.lower()}"
        f"&type={QUESTION_TYPE}"
    )

    return api_url


##game
#-questions, choices
#-input
#-answer check, score

#-relay back score and acuracy, all at the end

#-continue game function, yes continue, no exit
