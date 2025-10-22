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
trivia_functions.api_test(
    topic_choice=game_topic(),
    difficulty_choice=game_difficulty()
    )


# Fetch questions using that key via a helper function

# Start quiz loop
    # Display each question and choices
    # Get user input
    # Check correctness, update score

#Show total score and accuracy at the end

#Ask if user wants to play again, if yes restart, if no exit