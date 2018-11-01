"""
Design a class called Sentence that has a constructor that takes a string representing the sentence as input.  
The class should have the following methods:

get_first_word(): returns the first word as a string
get_all_words(): returns all words in a list.
replace(index, new_word): Changes a word at a particular index to "new_word".
For example, if sentences is "I'm going back", then replace(2, "home") results in "I'm going home".  
If the index is not valid, the method does not do anything. 
"""

class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence.split()
    
    def get_first_word(self):
        return self.sentence[0]
    
    def get_all_words(self):
        return self.sentence
    
    def replace(self,index,new_word):
        try:
            self.sentence[index] = new_word
        except:
            pass
    
def main():
    user_input = input("Give me a sentence to work with")
    sentence = Sentence(user_input)
    print(sentence.get_first_word())
    print(sentence.get_all_words())
    sentence.replace(2,"sweet")
    print(sentence.sentence)

    

main()


