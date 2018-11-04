""" 
Implement the class Sales which has a private member variable which 
contains sales data. Implement the member functions needed for the 
following program to run: 
the program writes out:

Average sales: 199.81
Average sales: 186.33

"""
def read_data_from_file(textfile):
    rawdata = open(textfile,"r")
    file_contents = []
    for line in rawdata:
        file_contents.append(float(line))
    return file_contents

class Sales(object):
    def __init__(self,data):
        self.data = []
        for i in data:
            self.data.append(i)
    
    def get_average(self):
        return sum(self.data)/len(self.data)

    def add_sale(self,new_sale):
        self.data.append(new_sale)

def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()