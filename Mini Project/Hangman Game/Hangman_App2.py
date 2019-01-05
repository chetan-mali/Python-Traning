"""
Hangman Letter Game App -
    challenge 1
    We are going to make a “Hangman Letter” game
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

    Challenge 2
    Screen is messy and rolls ups
    Convert the code into function

"""
import random

def check(character):
    global random_word
    global guess_word
    global lifeline
    if character.lower() =='quit':
        return 0
    elif character in random_word and character not in guess_word:
        for index in range(len(random_word)):
            if character == random_word[index]:
                guess_word[index]=character
    else:
        print("Wrong guess")
        lifeline-=1
    print(' '.join(guess_word))
    if ''.join(guess_word)==random_word:
        print("You Win !!!")
        return 0


lifeline =3
guess_word=[]
Word_list = ["apple","banana","orange","coconut","strawberry","lime",
             "grapefruit","lemon","kumquat","blueberry","melon"]
random_word = random.choice(Word_list)                              #selecting random word from list
[guess_word.append("_") for char in random_word ]
print(" ".join(guess_word))
while lifeline>0:

    character = input("Enter character :")
    x = check(character)
    if x == 0:
        break
else:
    print("You Loss !!")



