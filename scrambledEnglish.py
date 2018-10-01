""" 
Scrambled English
Hints: 
- Don't bother scrambling words < 4 letters long
- The string.split() method is good for creating a list of words from a string
- The string.strip() method is useful to remove the end of line characters
- To scramble a string, convert it to a list, use random.shuffle from the random module
to scramble the string, and then use the join string method to convert back to a string: ".join(list)

A simple way to get some text to work with is to simply put it in a long string. (note the backlash continuation char: \)
    text = "Four score and seven years ago \
            our fathers brought for a nation \
            on this continent. "
Alternatively, you could use a modification of the word-list driver from the word puzzle programming project above to read a file.
To read a file named someFile.txt into one long string:
        getWordString() function

Optionally, add the capability to handle punctuation in the middle of words, eg a hyphen in a word. Scramble on either side
of the hyphen. 
"""

import random
import string

def get_word_string(file):

    return_list = []
    try:
        temp_file = open(file, "r")

        for line in temp_file:
            line_list = line.split()
            return_list.extend(line_list)
    except FileNotFoundError:
        print("File {} not found".format(file))
    return return_list

def scramble_string(paragraph):
    count = 0
    scrambled_paragraph = ''
    scrambled_word= ''
    while count < len(paragraph):
        
        word = paragraph[count].split()  # ['currentWord']
        word = word[0].strip(",").strip('.').strip("\"")
        
        if len(word) <= 4:
            scrambled_word = word
            scrambled_paragraph += scrambled_word + " "
        
        elif len(word) > 4:
            letters = list(word) # ['w','o','r','d']
        
            first_letter = ""
            last_letter = ""
            
            first_letter = letters[0]
            last_letter = letters[-1]
            to_scramble = letters[1:-1]
            
            random.shuffle(to_scramble)
            scrambled_word = ''.join(first_letter) + ''.join(to_scramble) + ''.join(last_letter) + " "
            
            scrambled_paragraph += scrambled_word
        
        count += 1
    return scrambled_paragraph


# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)