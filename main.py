import random

possibility = ['Stone', 'Paper', 'Scissors']

x = input('1) Stone\n2)Paper\n3)Scissors\n\nChoose:')

if x == 1 or x.lower() == 'stone':
    n = random.randint(0,2)
    are = possibility[n]
    print('Opponent: ' + are)

    if are == 'Stone':
        print('DRAW')

    if are == 'Scissors':
        print('YOU WIN')

    if are == 'Paper':
        print('YOU LOSE')

if x == 2 or x.lower() == 'paper':
    n = random.randint(0,2)
    are = possibility[n]
    print('Opponent: ' + are)

    if are == 'Stone':
        print('YOU WIN')

    if are == 'Scissors':
        print('YOU LOSE')

    if are == 'Paper':
        print('DRAW')

if x == 3 or x.lower() == 'scissors':
    n = random.randint(0,2)
    are = possibility[n]
    print('Opponent: ' + are)

    if are == 'Stone':
        print('YOU LOSE')

    if are == 'Scissors':
        print('DRAW')

    if are == 'Paper':
        print('YOU WIN')