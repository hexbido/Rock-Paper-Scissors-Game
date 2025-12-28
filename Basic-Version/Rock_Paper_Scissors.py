import random

# --------------------------------[ Game Initialization ]-----------------------------------

print("Welcome To 'Rock - Paper - Scissors' Game!")

# Get Player Input And Capitalize It To Match The Logic (R, P, S)
player = input("Please Enter Your Movement ('R' For Rock - 'P' For Paper - 'S' For Scissors) : ").capitalize()

# --------------------------------[ Computer Selection ]-----------------------------------

# Define The Available Moves List
pc = ["R", "P", "S"]

# Let The Computer Pick A Random Move From The List
pc_choice = (random.choice(pc))

# --------------------------------[ Display Choices ]-----------------------------------

# Show Both Moves To The User
print("Player Played: " + player)
print("The PC Played  : " + pc_choice)

# --------------------------------[ Win Logic & Results ]-----------------------------------

# Check For A Tie First
if player == pc_choice: 
    print("This is A Tie!")

# Check Winning Conditions For The Player
elif player == "R" and pc_choice == "S":
    print("You Win | User Won!")

elif player == "P" and pc_choice == "R":
    print("You Win | User Won!")

elif player == "S" and pc_choice == "P":
    print("You Win | User Won!")

# If Neither Tie Nor Player Win, The Computer Wins
else:
    print("You Lose | PC Won.")