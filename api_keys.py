# Purpose: Store and automatically build all 15 URLs.

# Base API Configuration (Constants)

BASE_URL = "https://opentdb.com/api.php"                                          # The start of the API URL is always the same
DEFAULT_AMOUNT = 5                                                                # Number of questions to request (5)
QUESTION_TYPE = "multiple"                                                        # Type of questions ("multiple" or "boolean")

# Categories

CATEGORIES_LIST = [                                                               # List that contains the trivia categories
    ("Science", 17),                                                              # Science category, API ID is 17
    ("History", 23),                                                              # History category, API ID is 23
    ("Sports", 21),                                                               # Sports category, API ID is 21
    ("Music", 12),                                                                # Music category, API ID is 12
    ("Tech", 18)                                                                  # Tech category, API ID is 18
]

# Difficulty Levels

DIFFICULTIES_LIST = [                                                             # List that contains the trivia difficulties
    "easy",                                                                       # Easy Difficulty
    "medium",                                                                     # Medium Difficulty
    "hard"                                                                        # Hard Difficulty
]

# Look up the API ID for the category based on the name from CATEGORIES_LIST (Ignoring capitalization).

def get_category_id(category_name: str) -> int:
    for cat_name, cat_id in CATEGORIES_LIST:
        if cat_name.lower() == category_name.lower():
            return cat_id
    raise ValueError(f"Unknown category name: {category_name}")

# Function to build a complete API URL

def build_url(category_id: int, difficulty: str) -> str:
    api_url = f"{BASE_URL}?amount={DEFAULT_AMOUNT}&category={category_id}&difficulty={difficulty}&type={QUESTION_TYPE}"
    return api_url

# Dictionary to hold all generated URLs




# THINGS TO DO:
## Make it so that the cat_id in the new function is used as the category_id in the url builder. Right now, it is using whatever is entered, even if it is a string.
## Make it so that it can work with trivia_functions