

import random

answerList = ['toy', 'plane', 'bannana', 'wedding',
              'computer', 'christmas']

random.shuffle(answerList)

answer = list(answerList[0])


display = []

display.extend(answer)

for i in range(len(answer)):

    display[i] = "_"



print(" ".join(display))

correctAnswerCount = 0

while correctAnswerCount < len(answer):
    print("Correct answerCount: {}/{} \n".format(correctAnswerCount, len(answer)))
git 
    guess = input("Please enter a letter: ").lower()

    for i in range(len(answer)):

        if answer[i] == guess:
            display[i] = guess
            correctAnswerCount += 1



    print(" ".join(display))
    print("=============================")

print("Nice job, you guessed the word!")