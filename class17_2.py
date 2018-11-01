""" 
Write a class called RockGuitars() that has attributes: 'guitarist' and 'guitar'. 
It has a constructor with three parameters, self, guitarist and guitar. 
The default value of guitarist and guitar should be empty string.

The class should have __str__ method to return a string for output using this format: "{:<20s} {:<20s}". 
Lastly, it has the following method to set guitarist and guitar:

    set_entry(guitarist, guitar): both 'guitarist' and 'guitar' are strings.  
    'guitar" has the default value as the empty string.  
"""
class RockGuitars:
    def __init__(self,guitarist="",guitar=""):
        self.guitarist = guitarist
        self.guitar = guitar
    def __str__(self):
        return "{:<20s} {:<20s}".format(self.guitarist,self.guitar)
    def set_entry(self,guitarist,guitar=""):
        self.guitarist = guitarist
        self.guitar = guitar
        
def main():
    tinna = RockGuitars("KolTinna","Fendy")
    tinna.set_entry("NotKolfinna", "Not a Fendy")
    print(tinna)

    kolfinna = RockGuitars("Sjafnaðargata","Dixie")
    kolfinna.set_entry("Jólfinna","Hondo")
    print(kolfinna)
    

main()