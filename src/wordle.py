import os

# Function to read the contents of a file
def read_file(file_to_read):
    with open(file_to_read, "r") as f:
        return f.read().split()

# Load data into lists
wordle_words = read_file("../data/wordle_words.txt")
quordle_words = read_file("../data/quordle_words.txt")

# Color themes
color_sets = {
    "wordle": {
        "light": ["green", "yellow", "gray", "grey"],
        "dark": ["green", "yellow", "gray", "grey"],
    },
    "quordle": {
        "light": [],
        "dark": [],
        "colorblind": [],
    },
}

accepted_game_modes = [
    {
        "name": "wordle",
        "words": wordle_words,
        "color_themes": ["light", "dark"],
    },
    {
        "name": "quordle",
        "words": quordle_words,
        "color_themes": ["light", "dark", "colorblind"],
    },
]

# Function to prompt the user for game settings
def get_game_settings():
    game_mode = ""
    while game_mode not in [mode["name"] for mode in accepted_game_modes]:
        game_mode = input("Are you playing the original Wordle or a game similar to Wordle? Please type the name of the game you are playing: ")
    
    color_theme = ""
    while color_theme not in color_sets[game_mode]:
        color_theme = input("What color theme are you using? (light, dark, etc.) Please type the name of the theme you are using: ")
    
    hard_mode = ""
    while hard_mode not in ["y", "n"]:
        hard_mode = input("Are you playing in hard mode? (y/n): ")
    
    return {
        "game_mode": game_mode,
        "color_theme": color_theme,
        "hard_mode": hard_mode,
    }

# Get game settings
settings = get_game_settings()
game_mode = settings["game_mode"]
color_themes = settings["color_theme"]
hard_mode_on = settings["hard_mode"]