""" 
Write a function 'sort_list()' that accepts a list of integers and sorts it. 
The function should not explicitly return this list and yet the list will be 
sorted when printed within main() after being passed to sort_list() as a parameter.

Complete the main() module such that it accepts numbers from the user, 
until a non-digit string is entered (you could use try-except for this), 
and stores them in a list called 'a_list'. 
Hint: Functions have the ability to modify mutable objects in the calling program. 
A 'list' is a mutable object. Read section 8.1.2 in the book.

Example input/output:
2
32
43
12
24
32

Output:
[2, 32, 43, 12, 24, 32]
[2, 12, 24, 32, 32, 43]
"""
#sort_list() function goes here

def sort_list(input_list = ["s","o","r","t"]):
    input_list.sort()

def main():
    #loop to accept integers until a non-digit is entered goes here
    to_append = input()
    a_list = []
    while to_append.isdigit():
        a_list.append(int(to_append))
        to_append = input()
        
        
    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()