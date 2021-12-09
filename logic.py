import random # built-in libary
# user-defined import
from options import options
import score_keeper as sk

def init():
  cpu_selection = options[random.randint(0, 2)] # generate random numbers between 0 and 2
  user_selection = input('\nmake your choice...\n\'rock\', \'paper\', or \'scissors\'\n>>> ')

  def proceed():
    if user_selection == cpu_selection:
      print('it\'s a tie!!!')
    elif user_selection == 'rock' and cpu_selection == 'paper':
      print('\npaper covered rock')
      print('I win!...and you lose')
      sk.add_cpu_score()
    elif user_selection == 'paper' and cpu_selection == 'rock':
      print('\npaper covered rock')
      print('you win!')
      sk.add_user_score()
    elif user_selection == 'rock' and cpu_selection == 'scissors':
      print('\nrock smashed scissors')
      print('you win!')
      sk.add_user_score()
    elif user_selection == 'scissors' and cpu_selection == 'rock':
      print('\nrock smashed scissors')
      print('I win!...and you lose')
      sk.add_cpu_score()
    elif user_selection == 'paper' and cpu_selection == 'scissors':
      print('\nscissors cut paper')
      print('I win!...and you lose')
      sk.add_cpu_score()
    elif user_selection == 'scissors' and cpu_selection == 'paper':
      print('\nscissors cut paper')
      print('you win!')
      sk.add_user_score()

  if user_selection != 'rock' and user_selection != 'paper' and user_selection != 'scissors':
    invalid = True
    while invalid == True:
      print('\ninvalid selection!!!')
      user_selection = input('\nmake your choice...\n\'rock\', \'paper\', or \'scissors\'\n>>> ')
      if user_selection == 'rock' or user_selection == 'paper' or user_selection == 'scissors':
        invalid = False
    proceed()
  elif user_selection == 'rock' or user_selection == 'paper' or user_selection == 'scissors':
    proceed()

  continueOrNot = input('\ndo you wish to continue? (\'y\' or \'n\')\n>>> ')
  if continueOrNot == 'y' or continueOrNot == 'Y':
    init()
  else:
    print('\nthe score-line is:\nCPU:', sk.get_cpu_score(), '\nYOU:', sk.get_user_score())

