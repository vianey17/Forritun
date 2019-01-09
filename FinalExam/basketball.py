"""
In this assignment, you need to implement the class BasketballPlayer and two stand-alone functions
so that the given skeleton program runs correctly.  The class contains two instance 
variables (attributes): number (a number for the player) and points (the points scores by the player).

The class BasketballPlayer contains four methods.  What follows is a description for only one of them:

    shoot_ball(): This method selects randomly whether the player makes or does not make a shot (50% chance).
    Use random.randint(a,b) to determine if the player does make the shot.  If the players makes the shot,
    he/she accumulates two points, else 0.  The function returns the added points.

Note:

    The class Team is given - you do NOT need to implement any other functionality in that class.
    randint(a,b): Generates a random integer N in the range a <= N <= b.
    The main program reads a number from the user in order to initialize (seed) the random number generator,
    with random.seed()

"""

import random

TEAM_SIZE = 5
GAME_LENGTH = 48

class BasketballPlayer(object):
    def __init__(self,jersey,score=0):
        self.jersey = jersey
        self.score = score
    def shoot_ball(self):
        coin_flip = random.randint(1,11)
        if coin_flip % 2 == 0:
            self.score += 2
        return self.score
    def return_score(self):
        return self.score
    def __ge__(self,other):
        return self.score > other.score

class Team:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = BasketballPlayer(i+1) # i+1 is the number for the player
            self.__team.append(player)

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE-1)
        self.__points += self.__team[random_index].shoot_ball()

    def get_player_with_highest_score(self):
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
        return highest_player

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        for player in self.__team:
            the_str += str(player)
        return the_str


def print_winner(team_a, team_b):
    ''' You need to implement this function. Print out:
        which team won (if tie, print "Tie!")
    '''
    team_a_score = team_a.get_points()
    team_b_score = team_b.get_points()
    if team_a_score > team_b_score:
        print("{} are the winners!".format(team_a.get_name()))
    elif team_a_score < team_b_score:
        print("{} are the winners!".format(team_b.get_name()))
    else:
        print("Tie!")

def print_scores(team_a, team_b):
    ''' You need to implent this function.  Print out:
        how many points each team scored
        the scoring of each player in each team
        the highest scoring player in each team  
    '''
    team_a_score = 0
    team_b_score = 0
    for player in team_a.team:
        team_a_score += player.return_score
    print(team_a_score)
    for player in team_b.team:
        team_b_score += player.return_score
    print(team_a_score)

def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()    
        team_b.play_offence()
        
def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def main():
    # You are not allowed to change this main function
    random_seed()
    chicago_bulls = Team("Chicago Bulls")
    la_lakers = Team("LA Lakers")

    play(chicago_bulls, la_lakers)
    print_winner(chicago_bulls, la_lakers)
    print_scores(chicago_bulls, la_lakers)

main()