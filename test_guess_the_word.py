# Peter Bodjanac
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import WORDS, display_word, process_guess, select_word


# Test that the random word comes from the word list
def test_select_word():
    word = select_word()

    assert word in WORDS


# Test a correct letter guess
def test_correct_guess():
    guessed_letters = set()

    result = process_guess("python", guessed_letters, "p")

    assert result is True
    assert "p" in guessed_letters


# Test an incorrect letter guess
def test_incorrect_guess():
    guessed_letters = set()

    result = process_guess("python", guessed_letters, "z")

    assert result is False
    assert "z" not in guessed_letters


# Test that repeated letters are all shown
def test_repeated_letters():
    guessed_letters = {"a"}

    result = display_word("banana", guessed_letters)

    assert result == "_ a _ a _ a"


# Test that letters can be guessed in any order
def test_letters_in_any_order():
    guessed_letters = {"n", "b"}

    result = display_word("banana", guessed_letters)

    assert result == "b _ n _ n _"
