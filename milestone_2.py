import random

word_list = ["Apple", "Pear", "Orange", "Banana", "Grape"]
print(word_list)

def word():
    word_list = ["Apple", "Pear", "Orange", "Banana", "Grape"]
    return random.choice(word_list)

print(word)
