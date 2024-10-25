import random
MAX_BET = 100
MIN_BET = 1
MAX_LINES = 3
ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
        
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def check_winnings(): 

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != 2:
                print(column[row], end=" | ")
            else:
                print(column[row], end= "")
        print()

def deposit():
    while True:
        try:
            amount = int(input(f"What would you like to deposit $"))
            if amount > 0:
                print(f"${amount} deposited.")
                break
            else:
                print(f"Aount must be greater than 0")
        except ValueError:
            print(f"Enter in only numbers please\n")
    
    return amount

def get_bet():
    while True:
        try:
            amount = int(input(f"What would you like to bet on each line? $"))
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        except ValueError:
            print(f"Enter in only numbers please\n")
    
    return amount

def get_number_of_lines():
    while True:
        try:
            lines = int(input(f"Enter the number of lines you would like to bet on (1-{MAX_LINES})? "))
            if 0 < lines <=MAX_LINES:
                print(f"You've chosen to bet on {lines} lines")
                break
            else:
                print(f"Enter in a number from (1-{MAX_LINES})")
        except ValueError:
            print(f"Enter in a number from (1-{MAX_LINES})")
    
    return lines



def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough in your balance to bet this amount, current balance: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()