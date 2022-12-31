import os

# Function to read the contents of a file
def read_file(file_to_read):
    with open(file_to_read, "r") as f:
        return f.read().split()

accepted_game_modes = ["wordle", "quordle"]

# Load data into lists
wordle_words = read_file("data/wordle_words.txt")
quordle_words = read_file("data/quordle_words.txt")

# Color themes
wordle_accepted_color_themes = ["light", "dark"]
quordle_accepted_color_themes = ["light", "dark", "colorblind"]
wordle_light_color_set = ["green", "yellow", "gray", "grey"]
wordle_dark_color_set = ["green", "yellow", "gray", "grey"]
quordle_light_color_set = []
quordle_dark_color_set = []
quordle_colorblind_color_set = []

os.system('cls||clear')

# Change what loaded data word list to use depending of game mode
while True:
    game_mode = input("Are you playing the original Wordle or a game similar to Wordle? Please type the name of the game you are playing: ")
    game_mode_lowered = game_mode.lower()
    if game_mode_lowered in accepted_game_modes:
        break
    else:
        os.system('cls||clear')
        print("Unknown game mode given: %s\nAvailable game modes to choose:\n%s\n" % (game_mode, accepted_game_modes))

os.system('cls||clear')
print("Are you playing the original Wordle or a clone of Wordle? Please type the name of the game you are playing: %s" % game_mode)

# Change what color set to use depending of game mode
while True:
    color_theme = input("What color theme are you using? (light, dark, etc.) Please type the name of the theme you are using: ")
    color_theme_lowered = color_theme.lower()
    color_theme_set_name = game_mode_lowered + "_accepted_color_themes"
    color_theme_set_content = locals()[color_theme_set_name]
    if color_theme_lowered in color_theme_set_content:
        break
    else:
        os.system('cls||clear')
        print("Unknown color theme given: %s\nAvailable color themes in %s color set:\n%s\n" % (color_theme, game_mode, color_theme_set_content))

os.system('cls||clear')
print("Are you playing the original Wordle or a clone of Wordle? Please type the name of the game you are playing: %s" % game_mode)
print("What color theme are you using? (light, dark, etc.) Please type the name of the theme you are using: %s" % color_theme)

# Check if player in playing in hard mode
while True:
    hard_mode = input("Are you playing in hard mode? (y/n): ")
    hard_mode = hard_mode.lower()
    if hard_mode == "y" or hard_mode == "n":
        break
    else:
        os.system('cls||clear')
        print("Unknown answer given: %s\nPlease choose 'y' or 'n'\n" % hard_mode)

os.system('cls||clear')

accepted_colors = locals()["%s_%s_color_set" % (game_mode_lowered, color_theme_lowered)]
accepted_words = locals()["%s_words" % game_mode_lowered]
removed_words = []

# Lowercase all the items in the accepted words list
for item, item_index in zip(accepted_words, range(len(accepted_words))):
    accepted_words[item_index] = item.lower()