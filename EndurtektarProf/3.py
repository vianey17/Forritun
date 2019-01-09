"""
The main program above uses the given class VectorTest, which has been implemented to 
test the class Vector which you need to implement. By inspecting the main program, 
its output and the implementation of VectorTest you should be able to find out what 
attributes and functions are needed in the class Vector in order for the program to 
run and produce correct output. 

The following holds for vectors: 
"""

import math
class VectorTest:
    ''' This is a class for testing the Vector class '''
    def __init__(self, list1, list2):
        self.__v1 = Vector(list1)
        self.__v2 = Vector(list2)
    
    def test_print(self):
        print("v1 and v2: {} {}".format(self.__v1, self.__v2))
    
    def test_length(self):
        print("Length of v1 and v2: {:.2f} {:.2f}".format(self.__v1.length(), self.__v2.length()))
    
    def test_addition(self):
        print("v1 + v2: {}".format(self.__v1 + self.__v2))
    
    def test_scaling(self, scalar):
        self.__v1.scaling(scalar)
        self.__v2.scaling(scalar)
        print("Scaling v1 and v2 by {}: {} {}".format(scalar, self.__v1, self.__v2))

class Vector:
# Your implementation
    def __init__(self,coordinates):
        self.coordinates = coordinates
    
    def length(self):
        total = 0
        for x in self.coordinates:
            total += (x**2)
        length = math.sqrt(total)
        return length
    
    def __ge__(self,other):
        return len(self.coordinates) >= len(other.coordinates)
    def __lt__(self,other):
        return len(self.coordinates) < len(other.coordinates)
    
    def __len__(self):
        return len(self.coordinates)
    
    def __getitem__(self,key):
        return self.coordinates[key]
    
    def __add__(self,other):
        result = []
        if len(self) == 0 or len(other) == 0:
            return result
        if self >= other:
            for i in range(len(other)):
                add = self[i] + other[i]
                result.append(add)
        elif self < other:
            for i in range(len(self)):
                add = self[i] + other[i]
                result.append(add)
        return result
    
    def scaling(self,scalar):
        for i in range(len(self.coordinates)):
            self.coordinates[i] = self[i]*scalar

    def __str__(self):
        string_coordinates = []
        for i in self.coordinates:
            i = str(i)
            string_coordinates.append(i)
        string_coordinates = "[" + ", ".join(string_coordinates) + "]"
        return string_coordinates


# Main program starts here
vtest = VectorTest([2,4], [3,-4])
vtest.test_print()
vtest.test_length()
vtest.test_addition()
vtest.test_scaling(2)

vtest = VectorTest([3,5,-2], [2,-3,4])
vtest.test_print()
vtest.test_length()
vtest.test_addition()
vtest.test_scaling(3)