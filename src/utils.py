def read_words():
    try:
        with open("../data/wordlist.txt", "r") as file:
            return {word.strip() for word in file}
    except FileNotFoundError:
        print("Error: File 'wordlist.txt' not found.")
        raise
    except Exception as e:
        print(f"Error reading file 'wordlist.txt': {e}")
        raise


def display_game(chosen_word, used_letters, mistakes):
    guessed_word = "".join(letter if letter in used_letters else "_" for letter in chosen_word)
    print("--------------------")
    print(f"Mistakes: {mistakes}")
    print(f"Word: {guessed_word}")
    print(f"Used letters: {' '.join(sorted(used_letters))}")
