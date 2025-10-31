#Name: trivia_main.py

# Import functions file
import trivia_functions
from trivia_functions import game_topic, game_difficulty, api_test
# Import api_key file
import api_keys

# Display game title
trivia_functions.game_title()

# Ask for player name
trivia_functions.player_name()

# Use function that runs topic and difficulty function and then pulls an API key
"""
trivia_functions.api_test(
    topic_choice=game_topic(),
    difficulty_choice=game_difficulty()
    )
"""

# Fetch questions using that key via a helper function

# Start quiz loop
while True:
    # Display each question and choices
    # Call function to ask for questions and difficulty choices
    trivia_functions.game_topic()
    trivia_functions.game_difficulty()

    # Get user question inputs for those questions

    # Check correctness, update score

    #End Game
    ask = input("Play another round? (Y/N): ").upper()

    if input == "N":
        break

    else:
        continue

#Show total score and accuracy at the end

#Ask if user wants to play again, if yes restart, if no exit