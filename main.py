import words
import random
import time

hidden_word = random.choice(words.words)
word = list(hidden_word)
underscore = []
strike = 0


def hide_word():
    i = 1
    numOfletters = len(hidden_word)

    while i <= numOfletters:
        i += 1
        underscore.append("_")


def search_for_letter():
    global strike
    uLetters = len(word)
    print("The word has " + str(len(word)))
    while uLetters > 0:
        letter = input("Enter a letter: ")
        time.sleep(0.5)
        for i in range(len(word)):
            if letter == word[i]:
                underscore.pop(i)
                underscore.insert(i, letter)
                print(underscore)
                uLetters -= 1
        if letter not in word:
                    strike +=1
                    print("You have " + str(strike) + " strikes")
                    if strike == 10:
                        quit()
    print("Congratulations!")

hide_word()

search_for_letter()
