import csv

""" A given text file (.csv) contains data about closing prices for each business day 
of the year 2018 for a given stock in a stock exchange.  
The data is in two columns and the format is the following:

2018-12-31;529.09

2018-12-28;506.64

Write a Python program which asks the user for a name of a file 
in the format shown above and prints out average prices for each month. 
The averages should be printed using two decimal digits after the 
fractional point. If the input file cannot be opened, the program 
writes out an error message and quits. Note that the function that 
reads the file data is neither allowed to do any calculations nor 
printing anything out.

The following, which you HAVE TO use, is given in the implementation:

The start of the main program and the function open_file() 
which returns a file stream or None.
"""

def open_file():
    '''
    Prompts the user for a file name.
    Returns the corresponding file stream or None if file not found
    '''
    try:
        file_name = input("Enter file name: ")
        file_stream = open(file_name)
        return file_stream
    except FileNotFoundError:
        print("File not found!")
        return None

class Month_Values(object):
        def __init__(self,year,month,day):
                self.__prices = []
                self.year = year
                self.month = month
                self.day = day

        def average(self):
                total = 0
                for value in self.__prices:
                        total += value
                average = total / len(self.__prices)
                return average

def read_to_class(file_stream):
        """
        I need to make a class for every month
        I then add the values to a list within each class.
        I can then make a method that returns the average
        for that month.
        I realize this would've been more practical in
        a dictionary, but I can't remember the syntax
        at the moment and there really isn't much time
        dedicated to this test.
        """
        reader = csv.reader(file_stream)
        date_strings = []
        date_classes = []
        for line in reader:
                year, month, day = line[0].split("-")
                day = day[0:2]
                date_strings.append(year + month)
                date = Month_Values(year,month,day)
                if date not in date_classes:
                        date_classes.append(date)
                        date.date = (year + month)
                # I'd have added an additional line here that would've
                # appended the money value to the list in the class.
                # Only if the month/year variables in this loop matched those
                # in the class.



def main():
    file_stream = open_file()
    classes = read_to_class(file_stream)
    for each in classes:
            # This is where the average method would be called
            print("{} {:.2f}".format(each.date,each.average()))

    
main()