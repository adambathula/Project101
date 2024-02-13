import random

response = "y"

while response == "y":
    # Generating a random number between 1 and 6
    num = random.randint(1, 6)
    
    # Printing the dice representation based on the random number
    if num == 1:
        print("---------")
        print("|       |")
        print("|   *   |")
        print("|       |")
        print("---------")
    elif num == 2:
        print("---------")
        print("| *     |")
        print("|       |")
        print("|     * |")
        print("---------")
    elif num == 3:
        print("---------")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("---------")
    elif num == 4:
        print("---------")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("---------")
    elif num == 5:
        print("---------")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("---------")
    else:  # num == 6
        print("---------")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("---------")

    # Prompting the user to continue or exit
    response = input("Do you want to roll the dice again? (y/n): ").lower()

print("Goodbye! Thanks for playing.")