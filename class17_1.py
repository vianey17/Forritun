""" 
Write a class Student() such that it has an attribute 'score' (that is initialized with 10) and three methods:

add_score(): adds 10 to the score
decrease_score(): decreases score by 10
__str__(): returns the current score (should return a string)
Example input/output:
p = Student()
print(p)
10

p.add_score()
print(p)
20

p.decrease_score()
print(p)
10 
"""

class Student:
    def __init__(self):
        self.score = 10
    
    def add_score(self):
        self.score += 10
    
    def decrease_score(self):
        self.score -= 10
    
    def __str__(self):
        return str(self.score)

def main():
    tinna = Student()
    tinna.add_score()
    print(tinna)    

main()