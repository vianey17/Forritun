""" Project no. 3 in chapter 4 in the textbook.

The input prompt should be "Enter a word: "

Example input/output:

Enter a word: dog
ogday
Enter a word: scratch
atchscray
Enter a word: is
isyay
Enter a word: apple
appleyay
Enter a word: . """

word = input("Enter a word: ")
satt = True
while satt == True:
# For 1st letter is v
    if len(word) <= 1:
        satt = False

    elif len(word) <= 2:
        word = word + "yay"
        print(word)
        word = input("Enter a word: ")

    elif word[0] in ('a', 'e', 'i', 'o', 'u'):
        # apple --> appleyay
        # is --> isyay
        word = word + "yay"
        print(word)
        word = input("Enter a word: ")

    # For 1st letter c, 2nd letter v
    elif word[1] in ('a', 'e', 'i', 'o', 'u'):
        # dog --> ogday
        word = word[1::] + word[0] + "ay"
        print(word)
        word = input("Enter a word: ")

    # For both 1st and 2nd letter c
    elif word[2] in ('a', 'e', 'i', 'o', 'u'):
        # trump --> umptray
        # grumpy --> umpygray
        word = word[2::] + word[0:2] + "ay"
        print(word)
        word = input("Enter a word: ")

    # For first three c
    else: 
        # scratch --> atchscray
        word = word[3::] + word[0:3] + "ay"
        print(word)
        word = input("Enter a word: ")
