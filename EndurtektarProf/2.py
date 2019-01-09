""" 
In this project, you implement the game Rock-Paper-Scissors.  
Your program will allow a user to play the game against the computer. 
The objective of Rock-Paper-Scissors is to defeat the opponent by selecting 
a weapon that defeats his/her choice under the following rules:

    Rock smashes Scissors, so Rock wins.
    Scissors cut Paper, so Scissors win.
    Paper covers Rock, so Paper wins.
    If players choose the same weapon, neither win and the game is a tie

The game consists of the following:

    The program chooses a weapon randomly by using the function random.choice().
    The program asks the user for his/her weapon choice with the prompt 
    “Enter weapon (r/p/s):”. The valid input choices are:
        r (Rock)
        p (Paper)
        s (Scissors)
        q (Quit)

If the user inputs an invalid choice, the program asks the user to make another choice.

    Both weapons are displayed.
    The winner (or tie) is displayed.
    The game continues until the user chooses to quit.
    Finally, the counts of wins for the user and  the computer are printed out 
    as well as the number of ties.

The following, which you HAVE TO use, is given in the implementation:

    The start of the main program, including the function random.seed()
    Several constants (you can add more constants).
    
    Random seed: 9
    Enter weapon (r/p/s): r
    Computer weapon: p
    User weapon: r
    Computer wins!
 """

import random

# Constants
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
QUIT = 'q'

def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def play(score):
    allowed_moves = [ROCK,PAPER,SCISSORS]
    computer_move = random.choice(allowed_moves)
    player_move = input("Enter weapon (r/p/s): ").lower()
    print("Computer weapon: ", computer_move)
    print("User weapon: ", player_move)
    
    if player_move == computer_move:
        print("Tie!")
        score[2] += 1
    elif player_move == ROCK:
        if computer_move == SCISSORS:
            print("User wins!")
            score[0] += 1
        elif computer_move == PAPER:
            print("Computer wins!")
            score[1] += 1
    elif player_move == SCISSORS:
        if computer_move == ROCK:
            print("Computer wins!")
            score[1] += 1
        elif computer_move == PAPER:
            print("User wins!")
            score[0] += 1
    elif player_move == PAPER:
        if computer_move == ROCK:
            print("User wins!")
            score[0] += 1
        elif computer_move == SCISSORS:
            print("Computer wins!")
            score[1] += 1
    if player_move == "q":
        return player_move
    elif player_move not in allowed_moves:
        print("Make another choice")


def main():
    random_seed()
    score = [0,0,0]
    keepgoing = "yes"
    while keepgoing != "q":
        keepgoing = play(score)
    print("User won: ",score[0])
    print("Computer won: ", score[1])
    print("Tie: ", score[2])






main()