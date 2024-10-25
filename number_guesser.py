import random
import time
print(f"Random number guesser")
print(f"Enter 'q' to quit at any time")

while True:
    rand = random.randint(1,10)
    print(f"\nIm thinking of a number between 1-10,try to guess it")
    try:
        ans = int(input(f"Answer: "))
        if ans < 1 or ans > 10:
            print(f"Enter a number between 1-10")
            continue
    except ValueError:
        print(f"Enter in a number please")
        continue
    print(f"\nYour answer: {ans}")
    print(f"Number: {rand}\n")

    if ans == rand:
        print(f"\nYou guessed correctly!")
        cont = input(f"Play again?(Y/N)")
        if cont == 'y':
            continue
        else:
            break
    else:
        print(f"You failed :(")
        cont = input(f"Play again?(Y/N) ")
        if cont == 'y':
            continue
        else:
            break