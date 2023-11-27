computer_wins = 0
user_wins = 0
play_again = 'y'

# prompt the user to play again
#play_again = input('Would you like to play again? (y/n): ')
# if the user wants to play again, repeat the game
while play_again == 'y':
    # prompt the user to enter on of the following values: 'rock', 'paper', or 'scissors', ignoring case, and warn the user if an invalid value was entered
    user_choice = input('Please enter one of the following values: rock, paper, or scissors: ')
    # convert the user's choice to lowercase
    user_choice = user_choice.lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print('Invalid value entered')
        continue
    # randomly select one of the values: 'rock', 'paper', or 'scissors' for the computer
    import random
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    # display the user's choice and the computer's choice
    print('You chose: ' + user_choice)
    print('The computer chose: ' + computer_choice)
    # determine the winner and display the result and count the number of wins for the user and the computer
    if user_choice == computer_choice:
        print('It\'s a tie!')


    elif user_choice == 'rock' and computer_choice == 'paper':
        print('The computer wins!')
        computer_wins += 1
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
        user_wins += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
        user_wins += 1
    elif user_choice == 'paper' and computer_choice == 'scissors':
        print('The computer wins!')
        computer_wins += 1
    elif user_choice == 'scissors' and computer_choice == 'rock':
        print('The computer wins!')
        computer_wins += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
        user_wins += 1
    print('The user has won ' + str(user_wins) + ' times')
    print('The computer has won ' + str(computer_wins) + ' times')
    # prompt the user to play again
    play_again = input('Would you like to play again? (y/n): ')