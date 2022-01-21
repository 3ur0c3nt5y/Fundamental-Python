from random import randint

random_number = randint(1, 9)
print(random_number)

guess = 0
try:
    guess = int(input('Pick a number between 1 and 9: '))
    if guess < 1 or guess > 9:
        print('You did not enter a number between 1 and 9!')
except ValueError:
    print('You did not enter a valid number!')

if random_number == guess:
    print('Correct!')
else:
    print('The number I chose is {0}.'.format(random_number))
