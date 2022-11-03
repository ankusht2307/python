import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'


def get_choices():

  player_choice = input('Enter a choice (rock, paper, scissors): ')
  options = [rock, paper, scissors]
  computer_choice = random.choice(options)
  choices = {'player': player_choice, 'computer': computer_choice}
  return choices


def check_win(player, computer):
  print(f"You chose {player} and computer chose {computer}")
  if player == computer:
    return "It's a tie"
  elif player == paper:
    if computer == rock:
      return 'Paper wraps rock. You win!'
    else:
      return 'Scissors cut paper. You loose'
  elif player == rock:
    if computer == scissors:
      return 'Rock smashes scissors. You win!'
    else:
      return 'Paper wraps rock. You loose'
  elif player == scissors:
    if computer == paper:
      return 'Scissors cut paper. You win!'
    else:
      return 'Rock smashes scissors. You loose'


choices = get_choices()

result = check_win(choices['player'], choices['computer'])
print(result)