

# THIS VERSION WILL TAKE THE EXISTING CODE AND MAKE IT FUNCTIONAL

# IT WILL ALSO CHECK FOR THE TYPE OF ANSWERS THE USER ENTERS AND WILL TELL THEM THAT IT IS INVALID

# WILL SHOW THE LETTERS THAT THEY HAVE USED SO FAR

# WILL GIVE THE USER THE CHANCE TO PLAY AGAIN

# IF THE USER QUITS THEN THE PROGRAM WILL SHOW THEIR STATS AND END THE GAME
#     -STATS
#         -HOW MANY TIMES THEY GUESS
#         -WHAT WORDS THEY GOT RIGHT

import random

answerList = ['toy', 'plane', 'bannana', 'wedding',
                'computer']



def playAgain(stats):

    print(stats["Tries"])

    print("\n It took you {} tries to guess {}".format(stats["Tries"], stats["Words"][0]))

    user = input("Would you like to play again Y/n: ").lower()

    if user != 'y':
        print("Thanks for playing. Bye")

    else:
        game()

def game():

    correctAnswerCount = 0
    answer = random.choice(answerList)


    usedLetters = []

    display = []

    display.extend(answer)


    stats = {
        "Words": [],
        "Tries": 0
    }

    # CONVERT EVERY ELEMENT IN THE DISPLAY LIST TO AN UNDERSOCORE

    for i in range(len(answer)):

        display[i] = "_"


    print("========== \n{}\n==========".format(" ".join(display)))
    print("\nCorrect answerCount: {}/{}".format(correctAnswerCount, len(answer)))



    while correctAnswerCount < len(answer):
        guess = input("Please only choose a letter: ").lower()

        stats["Tries"] += 1



        # CHECK TO SEE IF THE USER ONLY ENTERED ONE LETTER
        if len(guess) == 1:

            usedLetters.append(guess)

            for i in range(len(answer)):
                if guess == answer[i]:
                    display[i] = guess
                    correctAnswerCount += 1

        else:
            guess = input("Please only choose ONE a letter: ").lower()

        print("========== \n{}\n==========".format(" ".join(display)))
        print("\nCorrect answerCount: {}/{} \n ".format(correctAnswerCount, len(answer)))
        print()
        print(" letters used: \n{}".format(" ".join(usedLetters)))

    stats["Words"].append("".join(answer))

    print("Well done you guessed the corrext word")


    playAgain(stats)



game()