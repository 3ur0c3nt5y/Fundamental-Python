from random import choice

chocolates = ['milk', 'white', 'dark', 'caramel', 'mint']
rooms = {}
guesses = 2

for room in range(1, len(chocolates) + 1):
    random_chocolate = choice(chocolates)
    rooms[room] = random_chocolate
    chocolates.remove(random_chocolate)
    
print('Welcome to the Caramel Chocolate Adventure Game!')
print('Select a room 1 through 5 to go through the')
print('different rooms as your goal find the room with the caramel ')
print('chocolate.')
print('You get two guesses.')
print('If you type and room number and if the caramel chocolate ')
print('is in that room you win!')
print('Let the games begin!')

game_is_on = True
while game_is_on:
    try:
        room_number = int(input('Enter Room (1, 2, 3, 4, 5): '))
        if room_number < 1 or room_number > 5:
            print('Enter 1, 2, 3, 4 or 5 only!')
            break
    except ValueError:
        print('Enter valid room number!')
        break

    if guesses <= 1:
        print('Sorry about that.  Please try again.')
        game_is_on = False
    elif rooms[room_number] == 'caramel': 
        print('You found the caramel chocolate!  Great job!')
        game_is_on = False
    else:
        print('Sorry this room has {0} chocolate.'.format(rooms[room_number]))
        guesses -= 1      
  