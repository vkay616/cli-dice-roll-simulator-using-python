import random
import time 

def roll():
    return random.randint(1, 6)

counter = input("Type 'roll' to roll a die: ").lower()

if counter == 'roll':
    print('Rolling...')
    time.sleep(1)
    print('Rolled Number: ', roll())
else:
    exit