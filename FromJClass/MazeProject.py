# Backtracking

maze = [[".", ".", ".", "."],
        [".", "X", "X", "X"],
        [".", ".", ".", "X"],
        ["X", "X", ".", "."]]

def print_maze(maze):
    for row in maze:
        row_print = ""
        for value in row:
            row_print += value + " "
        print(row_print)

print(maze)
print_maze(maze)

def solve_maze(maze):
    return


solve_maze(maze)

def solve_maze_helper(maze, sol, pos_row, pos_col):
    num_row = len(maze)
    num_col = len(maze[0])