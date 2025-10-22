# Function Pseudo

# trivia_functions.py

import requests  # ADD: Required for API calls
import random   # ADD: Required for shuffling answers
import html     # ADD: Required for decoding HTML entities

# Display game name function
# KEEP: Unchanged from your original code
def game_title():
    print("|----------------------------------------------------------|")
    print("|      WELCOME TO THE CODE CONJURORS TRIVIA CHALLENGE      |")
    print("|----------------------------------------------------------|")

# Player name input function
# KEEP: Unchanged from your original code
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
                                    "\nPick a topic number: "
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
            "\nChoose Your Difficulty:"
        except ValueError:
            continue
            print(f"You selected option {difficulty_choice}")
            return difficulty_choice
        else:

# Topic choice input function
# MODIFY: Changed to accept string inputs and use 'not in' validation
def game_topic():
    # Create a while loop for input validation
    valid_topics = ["science", "history", "sports", "music", "tech"]
    while True:
        topic_choice = input("Enter your trivia topic!:" \
                            "\n1. Science" \
                            "\n2. History" \
                            "\n3. Sports" \
                            "\n4. Music" \
                            "\n5. Tech" \
                            "\nPick a topic: ").lower()
        if topic_choice not in valid_topics:  # Check if input is NOT in the list
            print("Invalid choice. Please enter a valid topic (Science, History, Sports, Music, Tech).")
            continue
        print(f"You selected {topic_choice.capitalize()}")
        return topic_choice.capitalize()  # Return capitalized for API key

# Difficulty choice input function
# MODIFY: Changed to accept string inputs and use 'not in' validation
def game_difficulty():
    # Create a while loop for input validation
    valid_difficulties = ["easy", "medium", "hard"]
    while True:
        difficulty_choice = input("Enter your difficulty level:" \
                                 "\n1. Easy" \
                                 "\n2. Medium" \
                                 "\n3. Hard" \
                                 "\nChoose a difficulty: ").lower()
        if difficulty_choice not in valid_difficulties:  # Check if input is NOT in the list
            print("Invalid choice. Please enter a valid difficulty (Easy, Medium, Hard).")
            continue
        print(f"You selected {difficulty_choice.capitalize()}")
        return difficulty_choice.lower()  # Return lowercase for API compatibility

# Fetch the API key based on topic and difficulty
# MODIFY: Updated to handle string inputs directly
def api_test(topic_choice, difficulty_choice):
    api_key = f"{topic_choice}&{difficulty_choice.capitalize()}"
    print(f"Selected: {topic_choice} ({difficulty_choice.capitalize()})")
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


#-continue game function, yes continue, no exit


# TEST

import api_keys

url = api_keys.build_url(17, "easy")

print(url)



# Fetch questions from the API
# ADD: New function to fetch questions from OpenTDB
def fetch_questions(api_key):
    try:
        url = api_keys.API_URLS.get(api_key)
        if not url:
            print(f"Error: Invalid API key {api_key}")
            return []
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        if data['response_code'] == 0:
            return data['results']
        else:
            print("Error: Could not fetch questions from API")
            return []
    except requests.RequestException as e:
        print(f"Error fetching questions: {e}")
        return []

# Run the quiz loop
# ADD: New function to handle question display, user input, and scoring
def run_quiz(questions, player):
    score = 0
    total_questions = len(questions)
    
    for i, question_data in enumerate(questions, 1):
        # Decode HTML entities in question and answers
        question = html.unescape(question_data['question'])
        correct_answer = html.unescape(question_data['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]
        
        # Combine and shuffle answers
        all_answers = incorrect_answers + [correct_answer]
        random.shuffle(all_answers)
        
        # Display question
        print(f"\nQuestion {i}/{total_questions}: {question}")
        for j, answer in enumerate(all_answers, 1):
            print(f"{j}. {answer}")
        
        # Get user answer
        while True:
            try:
                user_choice = int(input("Enter your answer (1-4): "))
                if 1 <= user_choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Check if the answer is correct
        selected_answer = all_answers[user_choice - 1]
        if selected_answer == correct_answer:
            print(f"Correct, {player}!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")
    
    return score, total_questions
