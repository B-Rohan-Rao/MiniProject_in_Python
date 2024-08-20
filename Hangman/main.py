"""
Problem breakdown :-

Generate a random word.
Generate as many blanks as letter in the word.
Ask the user to guess the letter. -------------------
Is the guessed letter in the word?                   |
If yes,                                              |
    fill the corresponding blanks with the letter.   |
    Are all the blanks filled?                       |
    If yes,                                          |
        print the word and end the game.             |
    If no,                                           |
       Ask the user to guess the letter.  <----------
if no,                                               |
    Lose a life.                                     |
    Have they run out of life?                       |
    If yes,                                          |
        print the word and end the game.             |
    If no,                                           |
        Ask the user to guess the letter. <----------


"""
import random
from words import word_list

word = random.choice(word_list).lower()  # Step 1
# print(word)

placeholder = ""
game_over = False
correct = []
live = 6

for i in range(len(word)):  # Step 2
        placeholder += "-"
print(placeholder)    

while not game_over:
    Guess = input("Guess a word :-").lower()  # Step 3
    display = ""
    for letter in word:  # Step 4
        if Guess == letter:
            display += letter
            correct.append(letter)
        elif letter in correct:
            display += letter    
        else:
            display += "_"

    print(display)

    if Guess not in correct:
        live -= 1
        if live == 0:
            game_over = True
            print("You Lose")

    if "_" not in display :
        game_over = True
        print("You won")

print(word)        
