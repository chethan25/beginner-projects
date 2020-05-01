from random import randint


def game():

    # list of play options
    l = ["Rock", "Paper", "Scissor"]
    # set player to false
    player = False

    while player == False:

        # assign a random play to computer
        computer = l[randint(0, 2)]

        player = input("Pick one among Rock, Paper or Scissor (q for quit): ")
        if player == 'q':
            break
        elif computer == player:
            print("Tie")
        elif player == "Rock":
            if computer == "Paper":
                print(f"You Lose!, {computer} covers {player}")
            else:
                print(f"You Win!, {player} smashes {computer}")
        elif player == "Paper":
            if computer == "Scissor":
                print(f"You Lose!, {computer} cuts {player}")
            else:
                print(f"You Win!, {player} covers {computer}")
        elif player == "Scissor":
            if computer == "Rock":
                print(f"You Lose!, {computer} smashes {player}")
            else:
                print(f"You Win!, {player} cuts {computer}")
        else:
            print("Invalid Input")

        player = False


game()
