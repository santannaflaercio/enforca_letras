from utils import read_words, display_game
import random

mistakes, used_letters, words = 0, [], read_words()
chosen_word = random.choice(list(words)).lower()

while mistakes < 6 and len(set(chosen_word) - set(used_letters)) > 0:
    display_game(chosen_word, used_letters, mistakes)
    letter = input("Enter a letter: ").lower()

    if not letter.isalpha() or len(letter) != 1 or letter in used_letters:
        print("Please enter a single letter that has not been used yet.")
        continue

    used_letters.append(letter)
    mistakes += letter not in chosen_word
    print("Correct!" if letter in chosen_word else "Incorrect!")

print(f"{'Congratulations, you won!' if mistakes < 6 else f'You lost! The word was {chosen_word}.'}")
