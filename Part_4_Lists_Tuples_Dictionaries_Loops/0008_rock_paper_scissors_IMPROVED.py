import random

rules = {
  'Rock': {
    'Rock': 'Draw!',
    'Paper': 'Player Wins!',
    'Scissors': 'Computer Wins!'},
  'Paper': {
    'Rock': 'Computer Wins!',
    'Paper': 'Draw!',
    'Scissors': 'Player Wins!'},
  'Scissors': {
    'Rock': 'Player Wins!',
    'Paper': 'Computer Wins!',
    'Scissors': 'Draw!'}
}

game_is_running = True
while game_is_running:
  player_choice = input('What do you choose ({})? '.format(', '.join(rules.keys())))
  player_choice = player_choice.capitalize()

  if player_choice == 'Rock' or player_choice == 'Paper' or player_choice == 'Scissors':
    computer_choice = random.choice(list(rules.keys()))
  else:
    print('Please enter a valid response!')
    break

  print('Computer chose {0} and player chose {1}.'.format(computer_choice, player_choice))
  print('Computer - {0}'.format(computer_choice))
  print('Player - {0}'.format(player_choice))
  print(rules[computer_choice][player_choice])
  
  game_is_running = False