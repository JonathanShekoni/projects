import random
import time
OPERATORS = ['+','-','*']
MIN = 1
MAX = 12

def generate_problem():
    left = random.randint(MIN,MAX)
    right = random.randint(MIN,MAX)
    operator = random.choice(OPERATORS)

    question = f"{left} {operator} {right}"
    ans = eval(question)
    return question, ans


questions = int(input(f"How many questions would you like to solve? "))
print(f"Your time starts now.")
start_time = time.time()

for _ in range(questions):
    question,answer = generate_problem()
    while True:
        guess = input(f"Question {_+1}. {question} = ")
        if guess == str(answer):
            break


end_time = time.time()
time_taken = round(end_time - start_time,2)
print(f"Finished {questions} questions in {time_taken} seconds.")
    
