print("--------------------------------------------")
print("ROCK! PAPER! or SCISSOR! Account Setup")
print("version 1.1")
print("--------------------------------------------")
while True:
    username = input("Please enter your username:  >> ")
    password = input("Please enter your password:  >> ")
    password_confirm = input("Please confirm your password:  ")

    if password != password_confirm:
        print("Your passwords don't match. Please try again.")

    if password == password_confirm:
        print("Your Account has been setup.")
        text_file = open("accounts.txt", "a")
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        break
