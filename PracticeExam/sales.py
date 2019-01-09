"""
Data in each line belongs to a specific department in a company.
Each line contains a sequence of N sales figures with a single space between the figures.
For example, the third line (for department no. three) contains a sequence of 8 sales figures.
Write a Python program which reads a file like the one above, computes the average
sales figure for each department and displays the result (using one decimal digit
after the fractional point) to the screen. The program should ask the user
for the name of the input file, display an error message and exit if the input file
cannot be opened.  Note that the function that reads the sales data is neither allowed 
to do any calculations nor print anything out. 
"""

def read_file():
    filename = input("Enter file name: ")
    try:
        nested_list = []
        with open(filename) as file_raw:
            for line in file_raw.readlines():
                    line = line.split()
                    for i in range(0,len(line)):
                            line[i] = int(line[i])
                    nested_list.append(line)
        return nested_list

    except FileNotFoundError:
        print("File not found!")
        quit()

def calc_avg(sales_list):
        print("Average sales:")
        for index, data in enumerate(sales_list):
                sum_sales = sum(data)
                count_sales = len(data)
                average = sum_sales/count_sales
                print("Department no. {}: {:<.1f}".format(index+1,average))

def main():
    value_list = read_file()
    calc_avg(value_list)

main()