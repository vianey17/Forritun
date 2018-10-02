""" 
Write a function called 'game_of_eights()' that accepts a list of numbers as an argument 
and then returns 'True' if two consecutive eights are found in the list. 
For example: [2,3,8,8,9] -> True.
The main() function will accept a list of numbers separated by commas from the user and 
send it to the game_of_eights() function. 
The main() function prints out an error message saying 'Error. Please enter only integers.' 
if the list is found to contain any non-numeric characters.  
"""
#game_of_eights() function goes here

def game_of_eights(num_list):
# Takes a list of integers and returns True if it finds 
# two consecutive 8 values in it, False if it doesn't
    
    i = 0
    if num_list.count(8) > 1:
        while i < len(num_list):
            if num_list[i] == 8 and num_list[i+1] == 8:
                return True
            i += 1
    return False

def str_to_int(int_list):
# Takes a list of digits and converts them to
# int's. Returns Value Error if any nondigits
# are present in list.

    for element in range(len(int_list)):
        try:
            int_list[element] = int(int_list[element])
        except ValueError:
            print("Error. Please enter only integers.")
            quit()
    return int_list

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    
    # remainder of main() goes here
    str_to_int(a_list)
    
    print(game_of_eights(a_list))

main()