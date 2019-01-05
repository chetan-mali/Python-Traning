"""
Hangman Letter Game App -
    We are going to make a “Hangman Letter” game
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game
"""
import random
import time

lifeline =3
Word_list = ["apple","banana","orange","coconut","strawberry","lime","grapefruit","lemon","kumquat","blueberry","melon"]
random_word = random.choice(Word_list)
print(random_word)
guess_word=[]
for char in random_word:
    guess_word.append("_")
while lifeline>0:
    character = input("Enter character :")
    if character.lower() =='quit':
        break
    elif character in random_word and character not in guess_word:
        for index in range(len(random_word)):
            if character == random_word[index]:
                guess_word[index]=character
    else:
        print("Wrong guess")
        time.sleep(1)
        lifeline-=1
    print(guess_word)
    if ''.join(guess_word)==random_word:
        print("You Win !!!")
        break

else:
    print("You Loss !!")





