""" 
Write a function merge_lists that takes two lists as arguments, 
merges them into a third list without duplicates and returns 
the third list sorted.
The elements of each list are strings. 
"""
def merge_lists(list_1,list_2):
    new_list = []
    for element in list_1:
        if element not in new_list:
            new_list.append(element)
    for element in list_2:
        if element not in new_list:
            new_list.append(element)
    new_list.sort()
    return new_list

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
