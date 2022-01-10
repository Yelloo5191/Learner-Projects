#! python3
# Arithmetic Quiz
import operator, random

# define possible operations and empty questions dict
operators = {operator.add: "+", operator.sub: "-", operator.mul: "*", operator.floordiv: "/"}
questions = {}
score = 100

# loop 10 times
for x in range(10):

    # choose a random operator, two random numbers from 1-100, then add the data to questions dict
    operator = random.choice(list(operators.keys()))
    num1, num2 = random.randint(0,100), random.randint(0,100)
    answ = operator(num1, num2)
    questions[(operator, num1, num2)] = answ

# start a loop over each question
ques = 0
while ques != 10:

    # randomly pick a question
    question = random.choice(list(questions.keys()))
    print(f"Solve {question[1]} {operators[question[0]]} {question[2]}")
    res = input("> ")

    # try/except block is for empty responses/responses with letters or other non-numeric characters
    try:
        if int(res) == questions[question]:

            print("Correct.")
        
        else:

            score -= 10
            print("Incorrect. -10 Points.")
    except:
        # if the input is invalid, go back to the beginning of the loop
        # note that this doesn't remove the question from the quiz, it can pop up again anytime until the user provides a valid input
        print("Invalid response. Question skipped for now.")
        continue
    
    ques += 1
    questions.pop(question) # remove the question from the dict so that it's not randomly chosen again
    
print(f"Quiz complete. Your score: {score}")