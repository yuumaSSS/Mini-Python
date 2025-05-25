# Rock-Paper-Scissors Mini Game

import random

def game():
    validInput = ['rock', 'paper', 'scissors']
    validChoice = ['y', 'n']
    computer = random.choice(validInput)
    play = True

    # Play game
    print('Rock-Paper-Scissors Game\n')
    while play:
        user = input('Your turn: ').lower()

        # User input validation
        while user not in validInput:
            print('Input Is Not Valid!\n')
            user = input('Your turn: ').lower()

        print('Computer choice: ' + computer + '\n')

        # Rules
        if user == computer:
            print('--------')
            print('D R A W')
            print('--------\n')

        elif (user == 'rock' and computer == 'scissors') or\
             (user == 'paper' and computer == 'rock') or\
             (user == 'scissors' and computer == 'paper'):
                print('-----')
                print('W I N')
                print('-----\n')

        else:
            print('-------')
            print('L O S E')
            print('-------\n')

        # Stop game
        choice = input('Play again? (y/N): ').lower()
        while choice not in validChoice:
            print('Input Is Not Valid!\n')
            choice = input('Play again? (y/N): ').lower()
        if choice == 'y':
            pass
        else:
            play = False
            print('\nThanks for playing!')
            print('github.com/yuumaSSS')

if __name__ == '__main__':
    game()
