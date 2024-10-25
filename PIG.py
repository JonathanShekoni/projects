import random


def roll():
    min_number = 1
    max_number = 6
    choice = random.randint(min_number,max_number)
    return choice


while True:
    players = input(f"Enter the amount of people playing (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print(f"There are {players} people playing")
            try:
                max_score = int(input(f"What would you like the max score for the game to be:"))
            except ValueError:
                print(f"Enter in a number")
            break
        else:
            print(f"Enter a number between (2-4)")
    else:
        print(f"Enter a number between (2-4):")


player_scores = [0 for _ in range(players)]
try:
    while max(player_scores) < max_score:
        for player_idx in range(players):
            current_score = 0
            print(f"\nIt's player {player_idx + 1}'s Turn")
            print(f"Your total score is: {player_scores[player_idx]}\n")
            while True:
                has_rolled = input(f"Would you like to roll?(Y): ")
                if has_rolled.lower() != 'y':
                    break
                value = roll()
                if value == 1:
                    print(f"You rolled a 1!")
                    current_score = 0
                    break
                current_score += value
                print(f"Your current score is: {current_score}")
            player_scores[player_idx] += current_score
except NameError:
    pass
try:
    if max_score:
        winner = max(player_scores)
        winning_idx = player_scores.index(winner)

        print(f"\nCongratulations player {winning_idx + 1} won the game with a score of {winner}")
except NameError:
    pass