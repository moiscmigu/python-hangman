
import random


answerList = ['world', 'look', 'hello', 'goodbye']

random.shuffle(answerList)


answer = list(answerList[0])

print("This is the word: ", answer)

display = []

display.extend(answer)
for i in range(len(display)):
    display[i] = "_"


print("display after loop: ", display)

print(" ".join(display))
print()


count = 0

while count < len(display):
    guess = input("Please guess a letter: ")

    guess = guess.lower()
    print(count)

    for i in range(len(answer)):

        if answer[i] == guess:
            display[i] = guess
            count += 1


    print(" ".join(display))
    print()


print("Well done you've guessed the word")