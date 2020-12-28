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
    # Get size of the maze
    num_row = len(maze)
    num_col = len(maze[0])

    # Base Cases

    # Robot is already home
    # list starts 0, num of row 1 2 3 4
    if pos_row == num_row - 1 and pos_col == num_col - 1:
        return sol

    # Out of bounds
    if pos_row >= num_row or pos_col >= num_col:
        return None
    # Is on an obstacle (X)
    if maze[pos_row][pos_col] == "X":
        return None