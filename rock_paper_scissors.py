import random


moves = ['rock','paper','scissors']



def winning_scenario_player(player,computer):
    """Sets winning scenario for each possible player win."""
    if player.lower() == 'rock' and computer == 'scissors':
        print(f"Rock smashes scissors,You win!\n")
        return "win"
    elif player.lower() == 'paper' and computer == 'rock':
        print(f"Paper covers rock,You win!\n")
        return "win"
    elif player.lower() == 'scissors' and computer == 'paper':
        print(f"Scissors cuts paper,You win!\n")
        return "win"

def winning_scenario_computer(computer,player):
    """Sets winning scenario for each possible computer win."""
    if computer == 'rock' and player == 'scissors':
        print(f"Rock smashes scissors,You lose.\n")
        return "win"
    
    elif computer == 'paper' and player == 'rock':
        print(f"Paper covers rock,You lose.\n")
        return "win"
    elif computer == 'scissors' and player == 'paper':
        print(f"Scissors cuts paper,You lose.\n")
        return "win"
    



def player_choice():
    while True:
        choice = input(f"Enter in your choice:(rock,paper,scissors): ")
        if choice.lower() in moves:
            return choice.lower()
        elif choice.lower() == 'q':
            return choice.lower()
        else:
            print(f"Enter either 'rock','paper',or 'scissors'")



def computer_choice():
    choice = random.choice(moves)
    return choice



def main():
    p_score = 0
    c_score = 0
    valid_inputs = ['y','n']
    while True:
        p_choice = player_choice()
        c_choice = computer_choice()

        if p_choice.lower() == c_choice.lower():
            print(f"Draw.Try again!\n")
        elif p_choice.lower() == 'q':
            print(f"Thank you for using this program!")
            break
        else:
            if winning_scenario_player(p_choice,c_choice) == 'win':
                p_score += 1
                print(f"Player score:{p_score} ,Computer score:{c_score}")
                if p_score >2:
                    print("You won the game!")
                
            elif winning_scenario_computer(c_choice,p_choice) == 'win':
                c_score += 1
                print(f"Player score:{p_score} ,Computer score:{c_score}")
                if c_score >2:
                    print(f"Computer won the game!")
            if p_score > 2 or c_score > 2:
                user_input = input(f"\nWould you like to continue using the program?(Y/N): ")
                p_score = 0
                c_score = 0
                if user_input in valid_inputs:
                    if user_input.lower() == 'y':
                        continue
                    elif user_input.lower() == 'n':
                        break
                else:
                    print(f"Invalid input,please try again")
            else:
                continue


if __name__ == "__main__":
    main()