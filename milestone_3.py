 while True:
        print("\nAttempts left:", attempts)
        print(display_word(word_to_guess, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess! Guess is in the word.")
        else:
            print("Sorry, guess is not in the word. Try again")
            attempts -= 1

        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if attempts == 0:
            print("Game over! The word was:", word_to_guess)
            break
