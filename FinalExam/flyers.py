"""
Each line holds the name of a traveller and a country the traveller has visited.
The name and the country are seperated by a single space. Note that no traveller has
the same name and each traveller may have visited many countries and even the same
country more than once.

Write a Python program which reads information from the file flights.txt and does the following:

Prints the names of each traveller in alphabetical order.
For each traveller, prints a list of all the countries he/she has travelled to in alphabetical order.
Prints the name of the traveller who has travelled to most contries and the number of countries he/she has travelled to.
NOTE: If many travellers have travelled to the same number of countries you should print the first one of them.

Each traveller should be printed in the following format:

The name of the traveller followed by a colon.
Then each country in a separate line prefixed with a tab character ("\t"). """

def open_file(filename):
    try:
        raw_data = open(filename,"r")
        data_list = []
        for line in raw_data:
            data_list.append(line)
        raw_data.close()
        return data_list
    except FileNotFoundError:
        print("Cannot find file {}".format(filename))

class Traveller(object):
    def __init__(self,name,countries=[]):
        self.name = name
        self.countries = countries
    
    def __str__(self):
        print(self.name + " " + self.countries)
    
    def append_country(self,to_append):
        self.countries.append(to_append)
    
    def return_name(self):
        return self.name
    def return_countries(self):
        return self.countries


def make_travellers(data_list):
    """ 
    To place the names in their own list, we first split them from the 
    list with all the data and then add to the new names list only
    those not already in it. We sort list, then print each entry.
    """ 

    #First create classes with individual travellers

    names = []
    travellers = [] # A LIST OF CLASSES
    for entry in data_list:
        name = entry.split(" ")[0]
        if name not in names:
            names.append(name)
    for each in names:
        temp_class = Traveller(name)
        travellers.append(temp_class)
    return travellers

def assign_countries(travellers,data_list):
    # for every class, compare traveller name to
    # name on data list and append country to class
    # if they match.
    # Then assign country lists to respective traveller classes
    print(data_list)
    for traveller in travellers:
        temp_country_list = []
        for entry in data_list:
            temp_country = entry.split(" ")[1].strip()
            
            temp_name = entry.split(" ")[0]
            if temp_name == traveller.return_name():
                print(temp_name)
                temp_country_list.append(temp_country)
                # Why is this thing only printing Mary??
                
        traveller.append_country(temp_country_list)
        temp_country_list = []
    print(travellers[0].countries)
    for each in travellers:
        print(each.countries)

        #temp_country = entry.split(" ")[1].strip()
        
        #if temp_name not in names:
         #   names.append(temp_name)
        #if temp_country not in countries:
         #   countries.append(temp_country)

def main():
    # funtion that opens file and returns data
    raw_list = open_file("flights.txt")
    travellers = make_travellers(raw_list)
    assign_countries(travellers,raw_list)

main()
