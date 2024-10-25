import random

def roll():
    """Simulate rolling a die."""
    return random.randint(1, 6)

# Get the number of players
while True:
    players_input = input("Enter the number of players (2-4): ")
    if players_input.isdigit():
        num_players = int(players_input)
        if 2 <= num_players <= 4:
            print(f"There are {num_players} players playing.")
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 4.")
    else:
        print("Please enter a valid number.")

# Initialize player scores
players_scores = {f"Player {i + 1}": 0 for i in range(num_players)}
max_score = 50

# Game loop
while max(players_scores.values()) < max_score:
    for player in players_scores:
        current_score = 0
        print(f"\n{player}'s Turn")
        print(f"Your total score is {players_scores[player]}\n")
        
        while True:
            turn = input("Would you like to roll? (y/n): ")
            if turn.lower() != 'y':
                break
            
            roll_value = roll()
            if roll_value == 1:
                print("You rolled a 1! Turn over.")
                current_score = 0
                break
            else:
                current_score += roll_value
                print(f"You rolled a {roll_value}")
                print(f"Your score for this turn is {current_score}")

        players_scores[player] += current_score
        print(f"Your total score = {players_scores[player]}")

# Determine the winner
max_score = max(players_scores.values())
winning_player = [player for player, score in players_scores.items() if score == max_score]
print(f"{', '.join(winning_player)} is the winner!")
