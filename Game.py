import random


player1_score = 0
player2_score = 0

print("Let's begin the Rock Paper Scissor Game\n")
player1 = input("Enter your name: ")

for i in range(1, 6):
    print("\nROUND", i, "\n")

    print(player1, "choose: Rock(1), Scissor(2), or Paper(3)")
    player1_choice = int(input())

    if 1 <= player1_choice <= 3:
        player2_choice = random.randint(1, 3)

        if player2_choice == 1:
            print("Computer chose: Rock(", player2_choice, ")")
        elif player2_choice == 2:
            print("Computer chose: Scissor(", player2_choice, ")")
        elif player2_choice == 3:
            print("Computer chose: Paper(", player2_choice, ")")

        if player1_choice == player2_choice:
            player1_score += 0
            player2_score += 0
        else:
            if (player1_choice == 1 and player2_choice == 3) or \
                    (player1_choice == 2 and player2_choice == 1) or \
                    (player1_choice == 3 and player2_choice == 2):
                player1_score += 1
            else:
                player2_score += 1


        print("\nSCORE")
        print(player1_score, ":", player2_score, "\n")
    else:
        print("Wrong Input. Try Again :)\n")
        i -= 1

if player1_score > player2_score:
    print("GAME OVER --", player1, "won :)")
elif player2_score > player1_score:
    print("GAME OVER -- Computer won :(")
else:
    print("It's a tie :)")