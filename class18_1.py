""" Write a class 'Pair' that initializes two values 'v1' and 'v2' to '0' by default. 
It should print the values in this form: "Value 1: 20, Value 2: 30". 
When two objects of this class are added together using the '+' operator, 
the result is 'v1' of object 1 gets added to 'v1' of object 2 and 'v2' of 
object 1 gets added to 'v2' of object 2.

For example:
a = Pair(20,30)
print(a)
Value 1: 20, Value 2: 30
b = Pair(40,50)
c=a+b
print(c)
Value 1: 60, Value 2: 80 
"""
class Pair(object):

    def __init__(self, v1=0,v2=0):
        self.v1 = v1
        self.v2 = v2
    
    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.v1,self.v2)

    def __add__(self,other):
        new_v1 = self.v1 + other.v1
        new_v2 = self.v2 + other.v2
        return "Value 1: {}, Value 2: {}".format(new_v1,new_v2)

def main():
    obj1 = Pair(2,3)
    obj2 = Pair(4,5)
    c = obj1 + obj2
    
    print(obj1)
    print(obj2)
    print(c)

main()
