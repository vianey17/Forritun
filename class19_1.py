""" 
Implement the class Circle which has a private member variable for radius. 
Implement the member functions needed for the following program to run: 
Radius of circle: 3.0
Area: 28.27
Perimeter: 18.85

Area: 50.27
Perimeter: 25.13
"""
import math

class Circle(object):
    def __init__(self,radius):
        self.radius = int(radius)
    def __str__(self):
        area = math.pi * self.radius**2
        perimeter = 2*math.pi*self.radius
        return "Area: {:.2f}\nPerimeter: {:.2f}".format(area,perimeter)
    
    def set_radius(self,newrad):
        self.radius = newrad
    
    def get_radius(self):
        return self.radius

def main():   
    radius = input("Radius of circle: ")        
    circle = Circle(radius)
    print(circle)

    circle.set_radius(circle.get_radius() + 1.0)   
    print(circle)

main()