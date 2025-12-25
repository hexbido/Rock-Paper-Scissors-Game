import random

print("Welcome To 'Rock - Paper - Scissors' Game!")
player = input("Please Enter Your Movement ('R' For Rock - 'P' For Paper - 'S' For Scissors) : ").capitalize()
pc = ["R", "P", "S"]
pc_choice = (random.choice(pc))

print("Player Played: " + player)
print("The PC Played  : " + pc_choice)

if player == pc_choice: 
    print("This is A Tie!")
    
elif player == "R" and pc_choice == "S":
    print("You Win | User Won!")

elif player == "P" and pc_choice == "R":
    print("You Win | User Won!")

elif player == "S" and pc_choice == "P":
    print("You Win | User Won!")

else:
    print("You Lose | PC Won.")