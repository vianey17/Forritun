""" 
Write a Python program which allows a user to traverse a 5x5 grid until the user wants to quit.
The current position of the user is shown after each move. The user starts in the upper left 
corner on the screen and can at each turn move to the left, right, up or down. The user indicates 
moves by the following letter inputs (all other letters quit the execution of the program):

'l' for left
'r' for right
'u' for up
'd' for down

The user never moves out of the grid. If the user's current position is, for example, in the left-most 
column and inputs 'l' then the user moves to the right-most column. If the user's current position is, 
for example, in the bottom row and inputs 'd' then the user moves to the top row. The current position 
of the user is denoted with 'o' on the screen but other points in the grid are shown as 'x'.

Several functions and constants are given (which you HAVE to use), but you need to implement the main 
program and other necessary functions. """

# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def print_grid(grid):
    to_print = []
    counter = 1
    for box in grid:
        to_print.append(box)
    if counter != DIM:
        counter +=1
    elif counter == DIM:
        print(''.join(map(str, to_print)))
        to_print = []
        counter = 1

# Main program starts here
def main():
    keep_going = True
    grid = initialize_grid()
    print_grid(grid)
    while keep_going:
        move = get_move()
        if move == QUIT:
            quit()
# In your implementation, you have to use the functions and the constants given above
main()