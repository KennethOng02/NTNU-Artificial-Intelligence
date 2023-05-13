# How to run

## make sure to have the input stored in 'input.txt' file
## then run

### $ python3 ida-star.py

## the output is written in 'output.txt'

import sys
import time

class Puzzle:
    def __init__(self, board):
        self.board = board
        self.tile_num = len(board)
        self.target = [0] * self.tile_num
        self.bound = self.tile_num
        self.visited = []
        self.solution = []
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

    def is_visited(self, board):
        for arr in self.visited:
            if arr == board:
                return True
        return False

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

    def search(self, board, distance, threshold):
        if self.is_target(board):
            return -distance

        f_value = distance + self.heuristic(board)
        if f_value > threshold:
            return f_value

        min = sys.maxsize
        for i in range(self.tile_num):
            new = self.mutate(board, i) # generate new state

            if self.is_visited(new): # check for repeated
                continue
            self.visited.append(new)

            d = self.search(new, distance + 1, threshold) # find estimated distance
            if d < 0:
                self.solution.append(i + 1)
                return d
            elif d < min:
                min = d

            self.visited.pop() # remove trail

        return min # get the best estimated path

    def ida_star(self):
        threshold = self.heuristic(self.board)
        self.visited.append(self.board)
        for i in range(sys.maxsize):
            print(f'i: {i}')
            distance = self.search(board, 0, threshold)
            if distance == sys.maxsize:
                break
            if distance < 0:
                self.solution.reverse()
                return True, self.solution
            threshold = distance
        return False, []

    # calculate estimated remaining path
    def heuristic(self, board): 
        total = self.count_germ(board)
        if board[0] == 1:
            total -= 1
        if board[-1] == 1:
            total -= 1
        return total * 2 - 1

if __name__ == "__main__":
    try:
        with open("input.txt", "r") as f:
            input = f.read().strip()
            board = [int(x) for x in input.split(" ")];

        p = Puzzle(board)

        start = time.time()

        found, solution = p.ida_star()

        end = time.time()

        if found:
            # print(b.solution)
            with open("output.txt", "w") as f:
                f.write(f'Total run time = {end - start} seconds.\n')
                f.write(f'An optimal solution has {len(solution)} moves:\n')
                for move in solution:
                    f.write(f'{move} ')
        else:
            print("No solution found")

    except FileNotFoundError:
        print("Unable to find 'input.txt' file")
