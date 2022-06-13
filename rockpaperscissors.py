#! python

import random


cpuScore = 0
userScore = 0

while True :
    while True :
        print('Pick an option :')
        user = int(input("\n R = 1, P = 2, S = 3 \n"))
        if user != 1 and user != 2 and user != 3 :
            print('Input is invalid, Try again!')
        else :
            cpu = random.choice(range(1,3))
            break
    # R = Rock = 1
    # P = Paper = 2
    # S = Scissors = 3

    #Rules of the game
    #   Rock (1) wins Scissors (3)
    #   Paper (2) wins Rock (1)
    #   Scissors (3) wins Paper (2)

    if user == cpu :
        print('Game as a Tie')
    elif user == 1 and cpu == 2 :
        cpuScore += 1
        print('cpu Wins!')
    elif user == 1 and cpu == 3 :
        userScore += 1
        print('User Wins!')
    elif user == 2 and cpu == 1 :
        cpuScore += 1
        print('cpu Wins!')
    elif user == 2 and cpu == 3 :
        userScore += 1
        print('User Wins!')
    elif user == 3 and cpu == 1 :
        cpuScore += 1
        print('cpu Wins!')
    elif user == 3 and cpu == 2 :
        userScore += 1
        print('User Wins!')
    
    
    print('Current User Score: ', userScore)
    print('Current CPU Score: ', cpuScore,'\n')
