board_str = "1 0 1 1 0 1 1"
step_str = "4 5 6 2 3 4 5 6"
board = [int(x) for x in board_str.split(' ')]
steps = [int(x) for x in step_str.split(' ')]

tile_num = len(board)

def mutate(board, idx):
    new = [0] * tile_num
    for i in range(tile_num):
        if i != idx:
            if board[i] == 1:
                if i - 1 >= 0:
                    new[i - 1] = 1
                if i + 1 < tile_num:
                    new[i + 1] = 1
    return new

print(board)
for step in steps:
    print(f'Click grid {step}')
    board = mutate(board, step - 1)
    print(board)
