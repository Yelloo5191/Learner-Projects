import random

score = 0
dscore = 0

print("Enter 3 numbers separated by a comma (' , ')")
user_input = input()
user_input = user_input.replace(" ", "").split(',')

generated_numbers = [random.randint(0, 9), random.randint(0, 9), random.randint(0,9)]

for y, x in enumerate(user_input):
    if int(user_input[y]) == int(generated_numbers[y]):
        dscore += 1
    elif int(user_input[y]) in generated_numbers:
        score += 1

if dscore == 1:
    score += 10
elif dscore == 2:
    score += 100
elif dscore == 3:
    score += 1000

print(f"You ended with {score} points.")
print(f"The numbers were {generated_numbers}")
