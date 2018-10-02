""" 
This program reads a file called 'test.txt'. You are required to write two functions 
that build a wordlist out of all of the words found in the file and print all of the 
unique words found in the file. Remove punctuations using 'string.punctuation' and 'strip()' 
before adding words to the wordlist.

Write a function build_wordlist() that takes a 'file stream' as an argument and reads the contents, 
builds the wordlist after removing punctuations, and then returns the wordlist. 
Another function find_unique() will take this wordlist as a parameter and return another wordlist 
comprising of all unique words found in the wordlist. 
"""

#build_wordlist() function goes here
def build_wordlist(file):
    word_list = []
    for line in file:
        word_list += line.split()
    return word_list

#find_unique() function goes here
def find_unique(word_list):
    new_list = []
    for word in word_list:
        if word not in new_list:
            new_list.append(word)
    return new_list

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()