# Nakarin Philangam
# 01/06/2022

player1 = input("Enter R for rock,P for paper, S for scissors: ")
player2 = input("Enter R for rock,P for paper, S for scissors: ")

if player1.upper() == player2.upper():
    print("Tie")
elif player1.upper() == 'R' and player2.upper() == 'P':
    print("Player 2 has won the game")
elif player1.upper() == 'R' and player2.upper() == 'S':
    print("Player 1 has won the game")
elif player1.upper() == 'P' and player2.upper() == 'R':
    print("Player 1 has won the game")
elif player1.upper() == 'P' and player2.upper() == 'S':
    print("Player 2 has won the game")
elif player1.upper() == 'S' and player2.upper() == 'R':
    print("Player 2 has won the game")
elif player1.upper() == 'S' and player2.upper() == 'P':
    print("Player 1 has won the game")
else:
    print("Game canceled because of invalid entry")

