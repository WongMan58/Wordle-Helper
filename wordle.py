from re import L


def read_file(file_to_read):
    with open(file_to_read, "r") as f:
        return f.read().split()

possible_words = read_file("data/possible_words.txt")
removed_words = []

for i in range(6):
    user_word = input("What word did you put in?: ")
    print("\033c")
    user_word_data = []
    if user_word not in removed_words:
        removed_words.append(user_word)
        for user_letter, user_letter_pos in zip(user_word, range(len(user_word))):
            user_letter_color = input("What color was the letter %s ?: " % user_letter)
            if user_letter_color == "gray":
                for word in possible_words:
                    if word not in removed_words and user_letter in word:
                        user_letter_have_duplicate = False
                        for word_data in user_word_data:
                            if word_data[0] == user_letter:
                                user_letter_have_duplicate = True
                            if not user_letter_have_duplicate:
                                removed_words.append(word)
                if user_letter_have_duplicate:
                    for word in possible_words:
                        word_split = list(word)
                        user_current_letter_count = 0
                        for letter in word_split:
                            if letter == user_letter:
                                user_current_letter_count += 1
                        if user_current_letter_count > 1:
                            removed_words.append(word)
                user_word_data.append([user_letter, user_letter_color])
            elif user_letter_color == "yellow":
                for word in possible_words:
                    if word not in removed_words and user_letter not in word:
                        removed_words.append(word)
                    if word not in removed_words:
                        word_split = list(word)
                        if word_split[user_letter_pos] == user_letter:
                            removed_words.append(word)
                user_word_data.append([user_letter, user_letter_color])
            elif user_letter_color == "green":
                for word in possible_words:
                    if word not in removed_words and user_letter not in word:
                        removed_words.append(word)
                    if word not in removed_words:
                        word_split = list(word)
                        if word_split[user_letter_pos] != user_letter:
                            removed_words.append(word)
                user_word_data.append([user_letter, user_letter_color])
            else:
                print("Unknown color")
            print(len(removed_words))
    else:
        print("Unknown word.")
    
    words_to_print = []
    for word in possible_words:
        if word not in removed_words:
            words_to_print.append(word)
    
    print("\033c")
    print("WORDS THAT ARE AVAILABLE TO USE: ")
    print(words_to_print)