#Function Psuedo
import api_keys

# Requests to get the JSON from the URL, HTML for site entities, and Random for shuffling the choices
import requests
import html
import random

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

        # Provide the questions
        questions = fetch_questions(url)
        print (questions)

        #-answer check, score

        #-relay back score and acuracy, all at the end

        #-continue game function, yes continue, no exit
        replay_ask = input("Play another round? (Y/N): ").upper()

        if replay_ask == "N":
            break

        else:
            continue

# Get the questions from the API URL and turn them into usable items
def fetch_questions(api_url: str):
    # Ask API for JSON data using the URL that was created. AI was used to help understand what to do in this section.
    try:
        # Goes to the website and get's JSON data
        r = requests.get(api_url, timeout=10)
        # Checks for errors
        r.raise_for_status()
        # Turns JSON data into a python library
        data = r.json()
    # If request takes too long (10 seconds)
    except requests.exceptions.Timeout():
        print("\nThe Request timed out. Please try again.\n")
        return []
    # If there is a network or HTTP error
    except requests.exceptions.RequestException as e:
        print("\nNetwork or HTTP error: {e}\n")
        return []
    # If there is an invalid JSON
    except ValueError:
        print("\nReceived a response, but it was not a valid JSON.\n")
        return []
    
    # Check if the server found questions (response_code 0 means success) (data.get("results") checks for an empty list)
    if data.get("response_code") != 0 or not data.get("results"):
        print("\nNo questsions found for that choice. Try a different topic or difficulty.\n")
        return []
    
    # Empty list that will hold the questions, answers, and answer location
    prepared = []

    # Loop through the questions we got from the API URL
    for item in data["results"]:
        # For the next 3 lines, html.unescape will clean up the text so that HTML codes are turned into normal characters
        question_text = html.unescape(item.get("question", ""))
        correct = html.unescape(item.get("correct_answer", ""))
        incorrect = [html.unescape(x) for x in item.get("incorrect_answers", [])]

        # Combine all answers into a list
        choices = incorrect + [correct]
        # Shuffle the answers
        random.shuffle(choices)

        # Finds the location of the correct answer in the list
        answer_location = choices.index(correct)

        # Puts all of the cleaned up questions, answers, and location of the correct answer in an empty list
        prepared.append({
            "question": question_text,
            "choices": choices,
            "answer_location": answer_location
        })
    
    return prepared