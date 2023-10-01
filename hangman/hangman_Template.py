import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []
        print(f"The mystery word has {self.num_letters} characters")
        print(self.word_guessed)

    def check_letter(self, letter):
        letter = letter.lower()
        if letter in self.list_letters:
            print(f"{letter} was already tried")
        elif letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
                    self.num_letters -= 1
            self.list_letters.append(letter)
        else:
            self.num_lives -= 1
            self.list_letters.append(letter)

    def ask_letter(self):
        while True:
            letter = input("Enter a letter: ")
            if len(letter) != 1:
                print("Please, enter just one character")
            else:
                self.check_letter(letter)
                break

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()

    if game.num_letters == 0:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was {game.word}")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
