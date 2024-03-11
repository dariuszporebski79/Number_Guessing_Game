from random import randint


computer_number = randint(1, 100)
while True:
    while True:
        try:
            player_number = input("Guess the number: ")
            player_number = int(player_number)
            break
        except Exception:
            print("It's not a number!")
    if player_number < computer_number:
        print("Too small!")
    elif player_number > computer_number:
        print("Too big!")
    else:
        print("You won")
        break
