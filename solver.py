import pprint

# solver.py
def solve(bo): #solve function implements the backtracking algorithm for solving Sudoku puzzles. The function takes a 9x9 Sudoku board represented as a list of lists, and returns the solved board or False if no solution exists
    """
    Solves a sudoku board using backtracking 
    :param bo: 2s list of ints
    :return: solution
    """
    find = find_empty(bo) #this function find_empty is being called in the solve function
    if find:
        row, col = find
    else: 
        return True
    
    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i
            
            if solve(bo):
                return True
            
            bo[row][col] = 0
    
    return False


def valid(bo, pos, num): #valid function checks whether a given move is valid by checking whether the given number already exists in the row, column, or 3x3 box containing the cells specified by 'pos'
    """
    Returns if the attempted move is valid 
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
              return False
        
    # Check Col
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False
    
    # Check box
    
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True


def find_empty(bo): 
    """
    Finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
            
    return None


def print_board(bo):
    """
    prints the board
    :param bo: 2d lists of ints
    :return: None
    """

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

                if j == 8:
                    print(bo[i][j], end="\n")
                else:
                    print(str(bo[i][j]) + " ", end="")

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

pp = pprint.PrettyPrinter(width=41, compact=True)
solve(board)
pp.pprint(board)