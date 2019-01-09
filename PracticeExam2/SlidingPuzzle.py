"""
Write a Python program which allows a user to play "Sliding Puzzle" which contains a 4x4 board
of numbered tiles from 1-15. One of the cells is empty (denoted by a zero)
and does not contain a tile. The initial position is input from the keyboard, for example:


5 3 13 7 14 10 0 11 1 4 6 8 12 9 2 15

 

... which denotes the following initial position:

5	3	13	7
14	10		11
1	4	6	8
12	9	2	15


In each round of the game, the user inputs a single number in the range 0-15. 
If the number is 0 the program quits, while all other numbers denote a slide for 
the given cell into the empty space. For example, if a user inputs 10 in the 
initial position above then that cell slides into the empty cell to the right. 
The next position will thus become:

5	3	13	7
14		10	11
1	4	6	8
12	9	2	15

If a number is input which cannot be translated into a sliding move (e.g. 5 in the initial position)
then the previous position shall be shown unchanged. The purpose of the game is to arrange the 
numbers in ascending order, i.e. to achieve the following final position:

1	2	3	4
5	6	7	8
9	10	11	12
13	14	15

In the example above, the first line is input (the initial positions) and lines 
containing a single number are also input. Everything else is output. Note that a 
tab character is between the numbers when the current position of the game is displayed.

"""
import random

DIM = 4
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    numbers = input().split(" ")
    numbers = [int(number) for number in numbers]
    #numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #random.shuffle(numbers)
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()

# Your code goes here...
def get_current_pos(puzzle_board,player_move):
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == player_move:
                return (i,j)


def get_player_move(puzzle_board):
    try: 
        player_move = int(input())
        if player_move == QUIT:
            quit()
        else:
            return player_move
    except:
        display(puzzle_board)
        return get_move(puzzle_board)

def play(puzzle_board,player_move):
    current_pos = get_current_pos(puzzle_board,player_move)
    new_pos = get_new_pos(puzzle_board,current_pos)
    if new_pos != None:
        update_board(puzzle_board,current_pos,new_pos,player_move)

def get_new_pos(puzzle_board,current_pos):
    i, j = current_pos
    if j > 0 and puzzle_board[i][j-1] == EMPTYSLOT:
        return (i,j-1)
    if j < DIM-1 and puzzle_board[i][j+1] == EMPTYSLOT:
        return (i,j+1)
    if i > 0 and puzzle_board[i-1][j] == EMPTYSLOT:
        return (i-1,j)
    if i < DIM-1 and puzzle_board[i+1][j] == EMPTYSLOT:
        return (i+1,j)
    return None


def update_board(puzzle_board,current_pos,new_position,player_move):
    """
    Commits changes to puzzle_board
    """
    current_i,current_j = current_pos
    new_i,new_j = new_position
    puzzle_board[current_i][current_j] = EMPTYSLOT
    puzzle_board[new_i][new_j] = player_move


def check_win(puzzle_board):
    sorted_list = []
    board_list =[]
    for i in range(DIM):
        for j in range(DIM):
            board_list.append(puzzle_board[i][j])
    sorted_list = board_list.copy()
    sorted_list.sort()
    if sorted_list == board_list:
        print("You win!")
        return False
    else:
        return True


def main():
    puzzle_board = initialize_board()
    display(puzzle_board)  # Prints board
    keep_going = True
    while keep_going == True:
        player_move = get_player_move(puzzle_board)  # Gets player move and handles except errors
        play(puzzle_board,player_move)  # Changes puzzle board based on player input
        display(puzzle_board)  # Prints updated puzzle board
        keep_going = check_win(puzzle_board)  # Checks if numbers are in order and returns True/False

main()
