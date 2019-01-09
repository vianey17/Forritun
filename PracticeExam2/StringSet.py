"""
You need to write the class StringSet, which contains a set of strings 
(a set only contains one instance of each element). A main program which tests the class is given. 
You should also create a standalone function which takes a StringSet instance and a name of a 
file as parameters. The function should read the content of the file and store it in the StringSet.

The main program reads two documents, doc1.txt and doc2.txt, constructs two string sets which 
contains the words (strings) from these documents, and writes them out. The program then constructs 
the union of the two documents and writes it out. Thereafter, the program reads in a query from 
the file query.txt and writes it out. Then the size of the query is written out along with 
how many words of the query appear in the union. You can assume that all the files do not 
contain any punctuation characters.

Several conditions regarding StringSet that you need to fulfill:

    The class has a single constructor – a default constructor.
    The class stores its strings in a private list (not a S et)
    The class has a __str__ for writing out the contents of a set.
    The class has a method which overloads the + operator for constructing the union of two sets.

"""
class StringSet(object):
    def __init__(self):
        self.__words = []
    
    def __str__(self):
        return " ".join(self.__words)
    
    def add(self,word):
        if word not in self.__words:
            self.__words.append(word)
    
    def __getitem__(self,key):
        return self.__words[key]
    
    def __add__(self,other):
        union = StringSet()
        union.__words = self.__words
        for word in other.__words:
            union.add(word)
        return union

    def size(self):
        return len(self.__words)
    
    def at(self,index):
        return self.__words[index]
    
    def find(self,word):
        return word in self.__words


def read_file(StringSet,file_name):
    with open(file_name) as file_data:
        for line in file_data:
            for word in line.split():
                StringSet.add(word)

def main():
    doc1 = StringSet()
    doc2 = StringSet()
    query = StringSet()

    read_file(doc1, "doc1.txt")
    read_file(doc2, "doc2.txt")

    print("Doc1: ", doc1)
    print("Doc2: ", doc2)

    the_union = doc1 + doc2
    print("Union: ", the_union)

    read_file(query, "query.txt")
    print("Query:", query)

    count = 0
    for i in range(query.size()):
        if the_union.find(query.at(i)):
            count += 1
    
    print("Query size: ", query.size() )
    print("Found in union: ", count)

    for word in the_union:
        print(word)

main()