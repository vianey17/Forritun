""" 
Write a Python program using a for loop that, 
given the number n as input, prints the first n odd numbers starting from 1.

For example if the input is:
4

The output will be:
1
3
5
7
"""

num = int(input("Input an int: "))
for i in range(1,num*2,2):
    print(i)




