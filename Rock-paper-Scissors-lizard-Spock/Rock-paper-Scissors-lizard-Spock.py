# Rock-paper-scissors-lizard-Spock 

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

def name_to_number(name):
#This function convert nunmber to name   
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    else:
        return 4

def number_to_name(number):
#This function convert name to a number
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    else:
        return "scissors"

def rpsls(player_choice): 
    
    print
    print "Player choice: ",player_choice
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    number_to_name(comp_number)
    print "Computer choice: ",number_to_name(comp_number)

    #This code block Rock posibility
    if comp_number==0 and player_number==3:
        print "Computer Wins!"
    elif comp_number==0 and player_number==4:
        print "Computer Wins!"
    elif comp_number==0 and player_number==1:
        print "Player Wins!"
    elif comp_number==0 and player_number==2:
        print "Player Wins!"

    #This code block Spock posibility
    elif comp_number==1 and player_number==4:
        print "Computer Wins!"
    elif comp_number==1 and player_number==0:
        print "Computer Wins!"
    elif comp_number==1 and player_number==2:
        print "Player Wins!"
    elif comp_number==1 and player_number==3:
        print "Player Wins!"

    #This code block Paper posibility
    elif comp_number==2 and player_number==0:
        print "Computer Wins!"
    elif comp_number==2 and player_number==1:
        print "Computer Wins!"
    elif comp_number==2 and player_number==4:
        print "Player Wins!"
    elif comp_number==2 and player_number==3:
        print "Player Wins!"

    #This code block Lizard posibility
    elif comp_number==3 and player_number==2:
        print "Computer Wins!"
    elif comp_number==3 and player_number==1:
        print "Computer Wins!"
    elif comp_number==3 and player_number==0:
        print "Player Wins!"
    elif comp_number==3 and player_number==4:
        print "Player Wins!"

    #This code block Scissors posibility
    elif comp_number==4 and player_number==2:
        print "Computer Wins!"
    elif comp_number==4 and player_number==3:
        print "Computer Wins!"
    elif comp_number==4 and player_number==1:
        print "Player Wins!"
    elif comp_number==4 and player_number==0:
        print "Player Wins!"
        
    #This code togetherness posibility
    elif comp_number==player_number:
        print "There are no winners"   

rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")