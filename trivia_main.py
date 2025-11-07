#Name: trivia_main.py

# Import functions file
import trivia_functions
from trivia_functions import game_topic, game_difficulty
# Import api_key file
import api_keys

# Display game title
trivia_functions.game_title()

# Ask for player name
trivia_functions.player_name()

# call game loop
trivia_functions.game_loop()

#Show total score and accuracy at the end

#Ask if user wants to play again, if yes restart, if no exit