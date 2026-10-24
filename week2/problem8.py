a = input("Choose(rock/paper/scissors): ")
b = input("Choose(rock/paper/scissors): ")
choice = ["rock","paper","scissors"]
if (a == "rock" and b == "scissors") or (a == "paper" and b == "rock") or (a == "scissors" and b == "paper"):
    print("Player 1 wins")
elif (a == "rock" and b == "paper") or (a == "paper" and b == "scissors") or (a == "scissors" and b == "rock"):
    print("Player 2 wins")
elif a == b:
    print("It's a tie")
else:
    print("Error.Your input migh be wrong")