import random

def word():
    word_list = ["Apple", "Pear", "Banana", "Grape", "Orange"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        print("\nAttempts left:", attempts)
        print(display_word(word_to_guess, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Oops! That is not a valid input")
            attempts -= 1

        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if attempts == 0:
            print("Game over! The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
