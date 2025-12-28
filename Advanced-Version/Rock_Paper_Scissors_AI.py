import random

# --------------------------------[ Configuration & Rules ]-----------------------------------

# Define The Game Options (Short Code : Full Name)
options = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

# Define Winning Rules Logic (Key Beats Value)
# Example: Rock ('R') Beats Scissors ('S')
winning_rules = {
    "R": "S",
    "P": "R",
    "S": "P"
}

# Create A List Of Keys For The Computer To Choose From Randomly
option_keys = list(options.keys())

# --------------------------------[ Helper Functions ]-----------------------------------

def get_player_choice():
    """
    Handles user input and ensures validation.
    """
    while True:
        # Get Input And Normalize To Uppercase
        choice = input("Enter Your Move (R, P, S) Or 'Q' To Quit: ").upper()
        
        # Validate: Check If Choice Is In Options Or Is The Quit Command
        if choice == 'Q' or choice in options:
            return choice
        
        print("Invalid Choice! Please Enter 'R', 'P', Or 'S'.")

def show_results(player_move, computer_move, game_count):
    """
    Displays the choices and determines the winner using dictionary lookup.
    """
    # Retrieve Full Names From The Options Dictionary
    player_name = options[player_move]
    computer_name = options[computer_move]

    print(f"\nPlayer Chose: {player_name}")
    print(f"Computer Chose: {computer_name}")

    # 1. Check For Tie
    if player_move == computer_move:
        print("Result: It's A Tie!")
    
    # 2. Check If Player Wins Using The 'winning_rules' Dictionary
    elif winning_rules[player_move] == computer_move:
        print(f"Result: You Win! ({player_name} Beats {computer_name})")
    
    # 3. Otherwise, Computer Wins
    else:
        print(f"Result: You Lose! ({computer_name} Beats {player_name})")

    print(f"----------------- Game {game_count} -----------------")

# --------------------------------[ Main Game Loop ]-----------------------------------

def play_game():
    
    print("Welcome To 'Rock - Paper - Scissors' Game!")
    game_count = 0

    while True:
        # Step 1: Get Validated Player Choice
        player_choice = get_player_choice()
        
        # Check For Exit Condition
        if player_choice == 'Q':
            print("\nGoodbye! Thanks For Playing.")
            break

        # Step 2: Increment Round Counter
        game_count += 1
        
        # Step 3: Computer Picks A Random Move
        computer_choice = random.choice(option_keys)
        
        # Step 4: Calculate And Show Results
        show_results(player_choice, computer_choice, game_count)

# --------------------------------[ App Execution ]-----------------------------------

if __name__ == "__main__":
    play_game()