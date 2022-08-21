import os
import random
import time
from ascii_arts import arts, artname

#----CODE STARTS HERE------
isRepeat = True
while isRepeat:
# ----------------INTRO--------------------------
    os.system("cls||clear")

    print("🔍🔍 ASCII - 1 - WORD 🔍🔍\n\n")
    print("Welcome player! 👋👋\n")
    time.sleep(0.5)
    print("In this game, you have to guess the ASCII ART logos. 🎨")
    time.sleep(0.5)
    print("First, you have to choose three difficulty levels that can determine how many lives you will have. ")
    time.sleep(0.5)
    print("Each wrong guess can lose your life, so be careful! ❗❗❗")
    print("\nPress ENTER to start the game")

    input()
    os.system("cls||clear")
    t = 5
    while t:
            timer = "{:02d}".format(t)
            print("The game starts in: ",timer, end="\r")
            time.sleep(1)
            t -= 1
    # -----------------------------------------------

    # ---------------GAME START----------------------

    # Choosing random ascii art from ascii_arts.py
    index = random.randint(0,10)
    art = arts[index]
    art_name = artname[index].upper()
    lives = 0

    os.system("cls||clear")

    # ------------CHOOSING DIFFICULTY LEVEL-----------
    while lives == 0:
        print("Which DIFFICULTY level do you prefer?")
        print("EASY = 10 Lives (Press 1)")
        print("NORMAL = 7 Lives (Press 2)")
        print("HARD: 4 Lives (Press 3)")
        difficulty = input("\nEnter your choice: ")

        if difficulty == "1":
            lives = 10
        elif difficulty == "2":
            lives = 7
        elif difficulty == "3":
            lives = 4
        else:
            os.system("cls||clear")
            print("Please enter valid input (1-3)\n")

    msg = ""

    while lives > 0:
        print(art)
        print(msg)
        guess = input("Enter your guess: ").upper()
        if guess == art_name:
            break
        else:
            lives -= 1
            os.system("cls||clear")
            msg = f"Wrong Guess, you have {lives} lives left 🤕"

    if lives == 0:
        print(f"Sorry, you ran out of lives. \nThe name of logo was: {art_name}")
    else:
        print("Congratulations! You guessed it! 🎉🎊")

    tryAgain = ''

    while tryAgain != 'Y' and tryAgain != 'N':
        tryAgain = input("Do you want to play again? [Y / N]: ").upper()
        
        if tryAgain == 'Y':
            continue
        elif tryAgain == 'N':
            isRepeat = False
        else:
            os.system("cls||clear")
            print("Invalid input! Please try again")