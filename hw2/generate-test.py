import random

n = 8

with open('input.txt', 'w') as f:
    for i in range(n):
        f.write(f'{random.randint(0, 1)} ')
