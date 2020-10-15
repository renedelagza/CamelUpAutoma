"""
Automa program for Camel Up!
"""

def bettingTicket():
    x = random.randint(0,4)
    print(" >Take a", color[x], "betting ticket")

def spectatorTile():
    spec = ["CHEERING", "BOOING"]
    x = random.randint(0,4)
    y = random.randint(0,1)
    print(" >Place spectator tile in front of", color[x], "camel, on the", spec[y], "side")

def pyramidRoll():
    print(" >Take a pyramid ticket and ROLL!")

def betOverall():
    x = random.randint(0,1)
    result = ["WINNER", "LOSER"]
    print(" >Place a random bet on the Overall", result[x])
    
import random

overall = 3#This defines how many overall bettings Automa will do
color = ["YELLOW", "RED", "BLUE", "GREEN", "PURPLE"]
function_list = [bettingTicket,bettingTicket,bettingTicket,spectatorTile,spectatorTile,pyramidRoll,pyramidRoll,pyramidRoll,betOverall]
#Change the amount of times an action or function appears on this list to change Automa's behaviour.

while True:
    input('Press ENTER key to take action...\n')
    if overall == 0:
        function_list.remove(betOverall) #Overall bets are limited by the 'overall' variable. Once it reaches 0, the action won't be selected anymore.
        overall -= 1
    for func in random.sample(function_list,1):
        if func == betOverall:
            overall -= 1
        func()
    print('\n\n')

