
"""
The main program above uses the class IntList, which you need to implement.
By inspecting the main program you should be able to find out what attributes and 
functions are needed in the class in order for the program to run and produce correct output. 

Note the following:
add()

This function adds an element to the IntList instance if the instance is not full.

When two IntLists are added together a new list is constructed whose size is the 
lesser size of the two lists.
"""
class IntList(object):
    def __init__(self,size):
        self.value_list = []
        self.size = size
    
    def __add__(self,other_list):
        new_list = []
        try:
            for i in self.value_list:
                new_list.append(self.value_list[i] + other_list.value_list[i])
            return new_list
        except IndexError:
            return new_list
        
    
    def __str__(self):
        return str(self.value_list)
    
    def add(self,number):
        if not self.full():
            self.value_list.append(number)
            return self.value_list
    
    def __len__(self):
        return len(self.value_list)
    
    def full(self):
        if len(self.value_list) >= self.size:
            return True
        else:
            return False
    
    def get_size(self):
        return self.size
# Main program starts here
list1 = IntList(5)  # Constructs an IntList that can hold 5 integers
list2 = IntList(12) # Constructs and IntList that can hold 12 integers

for i in range(10):
    list1.add(i)
    list2.add(i)

print(list1)
print(list2)

print("Length of list1 is: {}".format(len(list1)))
print("Length of list2 is: {}".format(len(list2)))

if list1.full():
    print("list1 is full")
if list2.full():
    print("list2 is full")

list3 = list1 + list2
print(list3)

list4 = list2 + list1
print(list4)
