import random

options = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}
winning_rules = {
    "R": "S",
    "P": "R",
    "S": "P"
}
option_keys = list(options.keys())

def get_player_choice():

    while True:
        choice = input("Enter Your Move (R, P, S) Or 'Q' To Quit: ").upper()
        if choice == 'Q' or choice in options:
            return choice
        
        print("Invalid Choice! Please Enter 'R', 'P', Or 'S'.")

def show_results(player_move, computer_move, game_count):

    player_name = options[player_move]
    computer_name = options[computer_move]

    print(f"\nPlayer Chose: {player_name}")
    print(f"Computer Chose: {computer_name}")

    if player_move == computer_move:
        print("Result: It's a Tie!")
    elif winning_rules[player_move] == computer_move:
        print(f"Result: You Win! ({player_name} Beats {computer_name})")
    else:
        print(f"Result: You Lose! ({computer_name} Beats {player_name})")

    print(f"----------------- Game {game_count} -----------------")

def play_game():
    
    print("Welcome To 'Rock - Paper - Scissors' Game!")
    game_count = 0

    while True:
        player_choice = get_player_choice()
        
        if player_choice == 'Q':
            print("\nGoodbye! Thanks For Playing.")
            break

        game_count += 1
        computer_choice = random.choice(option_keys)
        show_results(player_choice, computer_choice, game_count)

if __name__ == "__main__":
    play_game()