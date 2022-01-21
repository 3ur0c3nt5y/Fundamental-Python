from random import randint

random_number = randint(1, 2)

guess = input('Enter A for heads or B for tails: ')
guess = guess.lower()

if random_number == 1 and guess == 'a':
    print('You WON!')
elif random_number == 2 and guess == 'b':
    print('You WON!')
else:
    print('You Lost')
