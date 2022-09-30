import os

# read_file function
def read_file(file_to_read):
    with open(file_to_read, "r") as f:
        return f.read().split()

# Load up word list and create removed_words list
possible_words = read_file("data/wordle_words.txt")
removed_words = []
available_colors = ["green", "gray", "grey", "yellow"]

# Clear terminal
os.system('cls||clear')

for i in range(6):
    # Game loop
    user_word_data = []
    while True:
        user_word = input("What word did you put in?: ")
        os.system('cls||clear')
        if user_word not in removed_words and user_word in possible_words:
            break
        elif user_word not in possible_words:
            print("'%s' is not a valid word. Please choose another word" % user_word)
        elif user_word in possible_words and user_word in removed_words:
            while True:
                y_or_n = input("The word you choose '%s' does not exactly fulfill the requirements. Are you sure you want to choose this word? (y/n)" % user_word)
                y_or_n = y_or_n.lower()
                if y_or_n == "y" or y_or_n == "n":
                    break
                else:
                    print("Unknown option choosen. Please try again.")
            if y_or_n == "y":
                break
            elif y_or_n == "n":
                pass
    for user_letter, user_letter_pos in zip(user_word, range(len(user_word))):
        while True:
            user_letter_color = input("What color was the letter '%s': " % user_letter)
            if user_letter_color in available_colors:
                break
            elif user_letter_color not in available_colors:
                print("'%s' is not one of the available color options. Please choose either: 'green', 'gray', 'grey' or 'yellow'.\n" % user_letter_color)
        if user_letter_color == "gray" or user_letter_color == "grey":
            letter_is_duplicate = False
            for letter in user_word_data:
                if letter[0] == user_letter:
                    letter_is_duplicate = True
            if not letter_is_duplicate:
                for word in possible_words:
                    if user_letter in word and word not in removed_words:
                        removed_words.append(word)
            user_word_data.append([user_letter, user_letter_color])
        elif user_letter_color == "yellow":
            for word in possible_words:
                if word not in removed_words:
                    if user_letter not in word:
                        removed_words.append(word)
                    else:
                        word_split = list(word)
                        if word_split[user_letter_pos] == user_letter:
                            removed_words.append(word)
            user_word_data.append([user_letter, user_letter_color])
        elif user_letter_color == "green":
            for word in possible_words:
                if word not in removed_words:
                    if user_letter not in word:
                        removed_words.append(word)
                    else:
                        word_split = list(word)
                        if word_split[user_letter_pos] != user_letter:
                            removed_words.append(word)
            user_word_data.append([user_letter, user_letter_color])
    
    green_count = 0
    for data in user_word_data:
        if data[1] == "green":
            green_count += 1
    if green_count == len(user_word):
        print("Congratulations, you have found the answer to today's Wordle! :)")
        exit(1)

    words_to_print = []
    for word in possible_words:
        if word not in removed_words:
            words_to_print.append(word)
    
    os.system('cls||clear')
    print("WORDS AVAILABLE TO USE:")
    print(words_to_print)