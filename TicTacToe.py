import string

def makeBoard(dimension):
    # generates board with specified dimensions 
    # and returns dictionary with keys/values
    
    board_length = dimension**2
    board_numbers = dict()
    
    for i in range(1,board_length+1):
        board_numbers[i] = i
    return board_numbers
    
def print_board(dictionary,dimension):
    # function: receives dictionary and prints it out in tic-tac-toe format
    # No return value    
    to_print = []
    counter = 1
    # iterate through dictionary values and 
    # print out rows of len(dimension) using a counter
    for key in dictionary:

        if type(dictionary[key]) == str:   
            to_print.append('{:>{width}s}'.format(dictionary[key],width=5))
        if type(dictionary[key]) == int:
            to_print.append('{:>{width}d}'.format(dictionary[key],width=5))
        if counter != dimension:            
            counter +=1
        elif counter == dimension:
            print(''.join(map(str, to_print)))
            to_print = []
            counter = 1
      
def play(dictionary,player_id,player_input):
    # function receives dictionary and updates its values based on player input
    # returns updated dictionary
    
    if str(dictionary[player_input]).isdigit(): # if the current cell contents are a digit, space is free
        dictionary[player_input] = player_id   
        return dictionary
    else: 
        print("Illegal move")
        player_input = int(input(player_id + " position: "))
        play(dictionary,player_id,player_input)
        return dictionary

def switch_player(player_id):
    if player_id == "X":
        player_id = "O"
        return player_id
    if player_id == "O":
        player_id = "X"
        return player_id

def win(dictionary,dimension,player_id):
       
    compare_to = '' 
    counter = 0
    # Ranges/steps for each of the three ways to win
    # win by rows, win by columns, win by diagonal
    
    # Check win by rows
    for i in range(1,((dimension**2)+1)-(dimension-1),dimension):
        # compares all values in row to the first,
        # if the number of times the values are the same equals the dimension
        # of the board, then the player wins. Otherwise, the counter resets
        # and starts comparing values in the next row.

        compare_to = dictionary[i] 
        
        for j in range(i,i+dimension):
            if dictionary[j] == compare_to:
                counter += 1
                if counter >= dimension:
                    print("Winner is:", player_id)
                    return False
            else:
                counter = 0

    # Check win by columns using same algorithm
    compare_to = '' 
    counter = 0
    for j in range(1,dimension+1): 
        compare_to = dictionary[j]
        for i in range(j,j+(dimension*(dimension-1))+1,dimension): 
            if (dictionary[i] == compare_to) and str(dictionary[i]).isalpha():
                counter +=1
                if counter >= dimension:
                    print("Winner is:", player_id)
                    return False
            else:
                counter = 0

    # Check win by diagonal to the right -->
    counter = 0
    for i in range(1,(dimension**2)+1, dimension+1):     
        
        if dictionary[i] == dictionary[1]:
            counter += 1
            if counter == dimension:
                print("Winner is:", player_id)
                return False
        else:
            counter = 0
    # and to the left <--
    counter=0
    for i in range(dimension,(dimension**2)+2-dimension, dimension-1):
        if dictionary[i] == dictionary[dimension]:
            counter += 1
            if counter == dimension:
                print("Winner is:", player_id)
                return False
        else:
            counter = 0
    # Check draw
    counter = 0
    for i in range(1,len(dictionary)+1):
        if str(dictionary[i]).isalpha():
            counter += 1
            if counter == len(dictionary):
                print("Draw!")
                return False
        else:
            counter = 0
    return True
def getDimension():
    # Handles all errors with invalid dimension input
    try:
        dimension = int(input("Input dimension of the board: "))
        if dimension < 3:
            print("Input must be at least 3")
            return getDimension()
        else:
            return dimension
    except ValueError:
        print("Invalid input")
        return getDimension()
def getMove(player_id,dimension):
    try:
        player_input = int(input(player_id + " position: "))
        if player_input > (dimension**2):
            print("Illegal move")
            return getMove(player_id,dimension)
        else:
            return player_input
    except ValueError:
        print("Invalid input")
        return getMove(player_id,dimension)

def main():
    dimension = getDimension()
    dictionary = makeBoard(dimension)
    print_board(dictionary,dimension)    
    player_id = "X"
    keepGoing = True
    while keepGoing:
        player_input = getMove(player_id,dimension)
        dictionary = play(dictionary,player_id,player_input)
        print_board(dictionary,dimension)
        keepGoing = win(dictionary,dimension,player_id)
        player_id = switch_player(player_id)

main()