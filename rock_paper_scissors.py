import time
print("Made by Fabian St. George. Visit fabianstgeorge.me for more info.")
print("version 1.1")
lose = ("The compter wins")
win = ("You Win")
lives = 5
score = 0
drew = 0
computer_lives = 7
password_list = []

while True:
    print("To being fill in the below information.")
    username = input("Please enter your username: \n>> ")
    password = input("Please enter your password: \n>> ")
    searchfile = open("accounts.txt", "r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
            print("--------------------------------------------")
            print("ROCK! PAPER! or SCISSOR!")
            print("ROCK!! PAPER!! or SCISSOR!!")
            print("ROCK!!! PAPER!!! or SCISSOR!!!")
            print("LET'S PLAY!!!!")
            print("--------------------------------------------")
            print("Access Granted")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            print("Welcome to ROCK! PAPER! or SCISSOR!")
            time.sleep(1)
            print("--------------------------------------------")
            print("Lives Rules:")
            print("--------------------------------------------")
            print("You start with", lives, "lives")
            print("If you lose you lose a live.")
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
                rps = input("Rock, Paper, Scissors? \n>> ").lower()
                import random

                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)


                def you_lose(choose):
                    print("The computer choose", choose)
                    print("")
                    print(lose)
                    print("")
                    status()
                    print("")


                def you_win(choose):
                    print("The computer choose", choose)
                    print("")
                    print(win)
                    print("")
                    status()
                    print("")


                def it_a_drew(choose):
                    print("The computer choose", computer)
                    print("")
                    print("You Drew")
                    print("")
                    status()
                    print("")


                def status():
                    print("You have " + str(lives) + " lives.")
                    print("You got " + str(score) + " correct")
                    print("You drew " + str(score) + " times")
                    print("Type 'exit' to leave game. ")


                # Rock if statments
                if rps == "rock" and computer == "paper":
                    you_lose(computer)
                    lives -= 1
                if rps == "rock" and computer == "scissors":
                    you_win(computer)
                    score += 1
                # Paper if statments
                if rps == "paper" and computer == "rock":
                    you_lose(computer)
                    score += 1
                if rps == "paper" and computer == "scissors":
                    you_win(computer)
                    lives -= 1
                # Scissor if statments
                if rps == "scissors" and computer == "paper":
                    you_lose(computer)
                    score += 1
                if rps == "scissors" and computer == "rock":
                    you_win(computer)
                    lives -= 1
                # dupclicates
                if rps == "rock" and computer == "rock":
                    it_a_drew(computer)
                    drew += 1
                if rps == "paper" and computer == "paper":
                    it_a_drew(computer)
                    drew += 1
                if rps == "scissors" and computer == "scissors":
                    it_a_drew(computer)
                    drew += 1
                # System
                if rps == "rules":
                    print("*************************************************")
                    print("Rule")
                    print("*************************************************")
                    print("-Rock loser against Paper")
                    print("-Rock beats Scissors")
                    print("-Paper beats Rock")
                    print("-Paper loses against Scissors")
                    print("-Scissors beat Paper")
                    print("-Scissors loses against Rock")
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
                    stop = input("Press enter to exit. \n>> ")
                    import time

                    time.sleep(900)
                if computer_lives == 0:
                    print("Thanks for playing.")
                    print("You have run out of lives")
                    print("You got", score, "correct")
                    print("You drew", drew, "times")
                    stop = input("Press enter to exit. \n>> ")
                    import time

                    time.sleep(900)
                # exit
                if rps == "exit":
                    break
        else:
            print("Your username or password is incorrect.")
            print("---------------------------------------")
