import random

pc_num = random.randint(1, 3)

while True:
    try:
        player_num = int(input("Guess a number from 1 to 3: "))
        if player_num < 1 or player_num > 3:
            print("Input must be from 1 to 3.")
        elif player_num != pc_num:
            print("Sorry! You lose.")
        elif player_num == pc_num:
            print("You win!")
            break
    except ValueError:
        print("Invalid input. Enter an integer.")




