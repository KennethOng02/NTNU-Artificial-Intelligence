# How to run

## make sure to have the input stored in 'input.txt' file
## then run

### $ python3 ids.py

## the output is written in 'output.txt'

import sys
import time

class Puzzle:
    def __init__(self, board):
        self.board = board
        self.tile_num = len(self.board)
        self.target = [0] * self.tile_num
        self.solution = []
        self.visited = []
        self.max_depth = sys.maxsize
        self.check_valid(self.board)
    
    def check_valid(self, board):
        for germ in board:
            if germ not in [1, 0]:
                print("Invalid input format")
                exit()
        return 

    def count_germ(self, board):
        germ_num = 0
        for germ in board:
            if germ == 1:
                germ_num += 1
        return germ_num

    def is_target(self, board):
        return board == self.target

    def mutate(self, board, idx):
        new = [0] * self.tile_num
        for i in range(self.tile_num):
            if i != idx:
                if board[i] == 1:
                    if i - 1 >= 0:
                        new[i - 1] = 1
                    if i + 1 < self.tile_num:
                        new[i + 1] = 1
        return new

    def is_visited(self, board):
        for arr in self.visited:
            if arr == board:
                return True
        return False

    def dls(self, board, depth):
        if depth == 0:
            return self.is_target(board)

        for i in range(self.tile_num):
            new = self.mutate(board, i) # generate new state

            if self.is_visited(new): # check for repeated state
                continue
            self.visited.append(new)

            found = self.dls(new, depth - 1)
            if found:
                self.solution.append(i + 1)
                return found

            self.visited.pop() # remove trail

        return False

    def iddfs(self):
        self.visited.append(self.board)
        for i in range(self.max_depth):
            print(f'i: {i}')
            found = self.dls(self.board, i)
            if found:
                self.solution.reverse()
                return True, self.solution
        return False, []

if __name__ == "__main__":
    try:
        with open("input.txt", "r") as f:
            input = f.read().strip()
            board = [int(x) for x in input.split(" ")];

        b = Puzzle(board)

        start = time.time()

        found, solution = b.iddfs()

        end = time.time()

        if found:
            with open("output.txt", "w") as f:
                f.write(f'Total run time = {end - start} seconds.\n')
                f.write(f'An optimal solution has {len(solution)} moves:\n')
                for move in solution:
                    f.write(f'{move} ')
        else:
            print("No solution found")

    except FileNotFoundError:
        print("Unable to find 'input.txt' file")
