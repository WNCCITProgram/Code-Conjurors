# Purpose: Store and automatically build all 15 URLs.

# Base API Configuration (Constants)

BASE_URL = "https://opentdb.com/api.php"                      # The start of the API URL is always the same
DEFAULT_AMOUNT = 5                                            # Number of questions to request (5)
QUESTION_TYPE = "multiple"                                    # Type of questions ("multiple" or "boolean")

# Categories

CATEGORIES_LIST = [                                           # List that contains the trivia categories
    ("Science", 17),                                          # Science category, API ID is 17
    ("History", 23),                                          # History category, API ID is 23
    ("Sports", 21),                                           # Sports category, API ID is 21
    ("Music", 12),                                            # Music category, API ID is 12
    ("Tech", 18)                                              # Tech category, API ID is 18
]

# Difficulty Levels

DIFFICULTIES_LIST = [                                         # List that contains the trivia difficulties
    "easy",                                                   # Easy Difficulty
    "medium",                                                 # Medium Difficulty
    "hard"                                                    # Hard Difficulty
]

# Function to build a complete API URL

# Dictionary to hold all generated URLs