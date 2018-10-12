""" Write a program that asks for name from the user and then asks for a number and stores the two in a dictionary as key-value pair.

The program then asks if the user wants to enter more data (More data (y/n)? ) and depending on user choice, 
either asks for another name-number pair or exits and stores the dictionary key, values in a list of tuples 
and prints a sorted version of the list. 

Note: Ignore the case where the name is already in the dictionary. """
def appendtolist(name_input, num_input,user_list):
    stored_data = dict(Name=name_input,Number=num_input)
    key = stored_data['Name']
    value = stored_data['Number']
    to_append = (key,value)
    user_list.append(to_append)
    return user_list


def main():
    keepGoing = True
    askKeepGoing = ""
    user_list = []
    
    while keepGoing:
        name_input = input("Name: ")
        num_input = input("Number: ")
        user_list = appendtolist(name_input,num_input,user_list)
        
        askKeepGoing = input("More data (y/n)? ")
        if askKeepGoing == "y".lower():
            continue
        elif askKeepGoing == "n".lower():            
            user_list.sort()
            print(user_list)
            keepGoing = False

main()