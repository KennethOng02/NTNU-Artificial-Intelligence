import random

row = random.randint(4, 8)
col = random.randint(4, 8)

with open("input.txt", "w") as f:
    f.write(f'{row} {col}\n')
    for i in range(row):
        for j in range(col):
            f.write(f'{random.randint(0, 1)} ')
        f.write(f'\n')
        