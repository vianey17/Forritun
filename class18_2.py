""" 
Write a class MyString() such that it has a method that gives 
the difference between the size of strings when the '-' (subtraction) 
operator is used between the two objects of the class. Additionally, 
implement a method that returns True if object 1 is greater than object 2 
and False otherwise when the (>) (greater than) operator is used. 
Object 1 is greater than object 2 if the string it stores is longer 
than the string stored in object 2.

For example:

obj1 = MyString('this is a string')
obj2 = MyString('this is another one')

print(obj1 > obj2)
False

print(obj1-obj2)
3
"""
class MyString(object):
    def __init__(self,string1):
        self.string1 = string1        
    
    def __sub__(self,other):
        return len(self.string1) - len(other.string1)
    
    def __gt__(self,other):
        return len(self.string1) > len(other.string1)

def main():
    stringy = MyString("hello")
    string2 = MyString("baby")
    c = stringy > string2
    print(c)

main()