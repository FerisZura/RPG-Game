import random


# accepts input for a number between 1 and the max number
def integer_input(maxNumber):
    x = 1
    while x == 1:
        userInput = input()
        if userInput.isdigit() == False:
            print("Invalid input")
        elif int(userInput) in range(1, maxNumber + 1):
            return int(userInput)
        else:
            print("Invalid input")


# prints the contents of a list
def print_list(list):
    for i in range(len(list)):
        print("({}) {}".format(i + 1, list[i]))

#prints warning in ascii
def print_warning():
    print(" __          __     _____  _   _ _____ _   _  _____ ")
    print(" \ \        / /\   |  __ \| \ | |_   _| \ | |/ ____|")
    print("  \ \  /\  / /  \  | |__) |  \| | | | |  \| | |  __ ")
    print("   \ \/  \/ / /\ \ |  _  /| . ` | | | | . ` | | |_ |")
    print("    \  /\  / ____ \| | \ \| |\  |_| |_| |\  | |__| |")
    print("     \/  \/_/    \_\_|  \_\_| \_|_____|_| \_|\_____|")
    input("                                                    ")

#prevents overheal
def prevent_overheal(player, healAmount):
    if player.health > player.maxHealth:
            difference = player.maxHealth - player.health  # diff is negative
            player.health = player.maxHealth
            healAmount += difference
    return healAmount
