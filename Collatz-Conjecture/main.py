# a program that generates a random number and applies the collatz conjecture rules to it until it reaches 1
# inspired by: https://www.youtube.com/watch?v=094y1Z2wpJg&ab_channel=Veritasium

import random
initial = random.randint(1, 10000) # up to any number should work just may take a long time
print(initial)
while True:
    if initial % 2 == 0: initial //= 2
    else: initial = (initial * 3) + 1
    print(initial)
    if initial == 1: break

