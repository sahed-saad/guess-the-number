import random

name = input('Before you proceed, enter your name: ')
print(f'Welcome {name}!\nThis is a number guessing game.\nYou only have 5 attempts!\nGuess the correct number between the range that you will specify within the next few prompts.')

lower_limit = int(input('Enter the lower limit for the range: '))
upper_limit = int(input('Enter the upper limit for the range: '))

if int(upper_limit) > int(lower_limit):
    #proceed with the game
    print(f'The system will randomly select a number between {lower_limit} and {upper_limit}.\nTry your best to guess that number!')



else:
    print('The upper limit must be greater than the lower one.')


