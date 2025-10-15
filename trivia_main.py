#Name: trivia_main.py

# Import functions file
import trivia_functions
# Import api_key file
import api_keys

# Display game title
trivia_functions.game_title()

# Ask for player name
trivia_functions.player_name()

# Ask for topic (1–5) and difficulty (1–3)
trivia_functions.game_topic()

trivia_functions.game_difficulty()

# Use topic and difficulty to select correct API key


# Fetch questions using that key via a helper function

# Start quiz loop
    # Display each question and choices
    # Get user input
    # Check correctness, update score

#Show total score and accuracy at the end

#Ask if user wants to play again, if yes restart, if no exit