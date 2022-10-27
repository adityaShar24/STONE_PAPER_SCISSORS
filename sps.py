import random
sps = ["S", "P", "SC"]


def play():
    value = random.choice(sps)
    user = input("let's start the game!  ")
    if value == user:
        print("DRAW!")
    elif user == "P" and value == "S":
        print("USER WINS")
    elif user == "P" and value == "SC":
        print("USER LOST")
    elif user == "SC" and value == "P":
        print("USER WINS")
    elif user == "S" and value == "P":
        print("USER LOST")
    elif user == "S" and value == "SC":
        print("USER WINS")
    elif user == "SC" and value == "S":
        print("USER LOST")
    print(value)
    play()


play()
