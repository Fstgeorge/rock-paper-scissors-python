print("Made by Fabian St. George. Visit fabianstgeorge.me for more info.")
print("version 1.0")
loose = ("The compter wins")
win = ("You Win")
lives = 5
score = 0
drew = 0
computer_lives = 7
while True:
    print("To being fill in the below information.")
    username = input("Please enter your username:")
    password = input("Please enter your password:")
    searchfile = open("accounts.csv", "r")
    for line in searchfile:
        if username and password in line:
            print("ROCK! PAPER! or SCISSOR!")
            print("ROCK!! PAPER!! or SCISSOR!!")
            print("ROCK!!! PAPER!!! or SCISSOR!!!")
            print("Access Granted")
            print("Lives Rules")
            print("You start with", lives, "lives")
            print("If you loose you loose a live.")
            print("If you draw the lives stay the same.")
            print("--------------------------------------------")
            print("MAKE SURE YOU DON'T USE CAPITALS")
            print("--------------------------------------------")
            print("To see a list of rule type rules")
            print("--------------------------------------------")
            print("The computer has lives as well.")
            print("Can you beat the computer?")
            print("Good LUCK!!")
            print("--------------------------------------------")
            while True:
                rps = input("Rock, Paper, Scissors?")
                import random

                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)
                # Rock if statments
                if rps == "rock" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives -= 1
                if rps == "rock" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score += 1
                # Paper if statments
                if rps == "paper" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    score += 1
                if rps == "paper" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    lives -= 1
                # Scissor if statments
                if rps == "scissors" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    score += 1
                if rps == "scissors" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    lives -= 1
                # dupclicates
                if rps == "rock" and computer == "rock":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1
                if rps == "paper" and computer == "paper":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1
                if rps == "scissors" and computer == "scissors":
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew += 1
                # System
                if rps == "rules":
                    print("*************************************************")
                    print("Rule")
                    print("*************************************************")
                    print("-Rock looser against Paper")
                    print("-Rock beats Scissors")
                    print("-Paper beats Rock")
                    print("-Paper looses against Scissors")
                    print("-Scissors beat Paper")
                    print("-Scissors looses against Rock")
                    print("*************************************************")
                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print(score)
                if rps == "display drew":
                    print(drew)
                # Lives
                if lives == 0 or rps == "test":
                    print("Thanks for playing.")
                    print("You have run out of lives")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit.")
                    import time

                    time.sleep(900)
                if computer_lives == 0:
                    print("Thanks for playing.")
                    print("You have run out of lives")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit.")
                    import time

                    time.sleep(900)
                # exit
                if rps == "exit":
                    break
        else:
            print("Your username or password is incorrect.")
            print("---------------------------------------")
