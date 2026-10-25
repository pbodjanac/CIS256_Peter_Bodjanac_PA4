# Peter Bodjanac
# CIS256 Fall 2026
# Programming Assignment 4

import random


# List of words that can be used in the game
WORDS = ["python", "banana", "computer", "program", "testing"]


def select_word():
    # Choose a random word from the list
    return random.choice(WORDS)


def process_guess(word, guessed_letters, guess):
    # Check if the guessed letter is in the word
    if guess in word:
        guessed_letters.add(guess)
        return True

    return False


def display_word(word, guessed_letters):
    # Show correct letters and hide letters not guessed yet
    displayed_letters = []

    for letter in word:
        if letter in guessed_letters:
            displayed_letters.append(letter)
        else:
            displayed_letters.append("_")

    return " ".join(displayed_letters)


def play_game():
    word = select_word()
    guessed_letters = set()

    # The player gets six incorrect attempts.
    attempts_left = 6

    print("Welcome to Guess the Word!")
    print("Guess one letter at a time.")

    # Keep playing until the player wins or runs out of attempts
    while attempts_left > 0:
        print()
        print("Word:", display_word(word, guessed_letters))
        print("Attempts left:", attempts_left)

        guess = input("Enter a letter: ").lower().strip()

        # Make sure the player enters only one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if process_guess(word, guessed_letters, guess):
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            attempts_left -= 1

        # Check if all letters in the word have been guessed
        if all(letter in guessed_letters for letter in word):
            print()
            print("Congratulations! You guessed the word:", word)
            return

    print()
    print("You ran out of attempts.")
    print("The word was:", word)


if __name__ == "__main__":
    play_game()
