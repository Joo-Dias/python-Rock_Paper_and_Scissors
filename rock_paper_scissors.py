import random

play = 0
keepPlaying = 0
computer = 0
user = 0

while play != 3:
    print('========================')
    print('Rock, Paper and Scissors')
    print('1 - Play ')
    print('2 - Play Rock Paper Scissors Lizard Spock ')
    print('3 - Exit ')
    print('========================')
    play = int(input(': '))

    if play == 1:
        while keepPlaying != 9:
            print('===================')
            print('Rock Paper Scissors')
            print('===================')

            print('1) ✊ Rock')
            print('2) ✋ Paper')
            print('3) ✌️ Scissors')
            user = int(input('Pick a number: '))
            computer = random.randint(1, 3)

            if user == 1 and computer == 1:
                print('Its a tie!')
            elif user == 1 and computer == 2:
                print('The computer won!')
            elif user == 1 and computer == 3:
                print('The player won!')

            if user == 2 and computer == 1:
                print('The player won!')
            elif user == 2 and computer == 2:
                print('Its a tie!')
            elif user == 2 and computer == 3:
                print('The computer won!')

            if user == 3 and computer == 1:
                print('The computer won!')
            elif user == 3 and computer == 2:
                print('The player won!')
            elif user == 3 and computer == 3:
                print('Its a tie!')
            
            keepPlaying = int(input('Keep playing? 8 - Yes | 9 - No: '))
    
    if play == 2:
        while keepPlaying != 9:
            print('================================')
            print('Rock Paper Scissors Lizard Spock')
            print('================================')

            print('1) ✊ Rock')
            print('2) ✋ Paper')
            print('3) ✌️ Scissors')
            print('4) 🦎 Lizard')
            print('5) 🖖 Spock')
            user = int(input('Pick a number: '))
            computer = random.randint(1, 5)

            if user == 1 and computer == 1:
                print('Its a tie!')
            elif user == 1 and computer == 2:
                print('The computer won!')
            elif user == 1 and computer == 3:
                print('The player won!')
            elif user == 1 and computer == 4:
                print('The player won!')
            elif user == 1 and computer == 5:
                print('The computer won!')

            if user == 2 and computer == 1:
                print('The player won!')
            elif user == 2 and computer == 2:
                print('Its a tie!')
            elif user == 2 and computer == 3:
                print('The computer won!')
            elif user == 2 and computer == 4:
                print('The computer won!')
            elif user == 2 and computer == 5:
                print('The player won!')
            
            if user == 3 and computer == 1:
                print('The computer won!')
            elif user == 3 and computer == 2:
                print('The player won!')
            elif user == 3 and computer == 3:
                print('Its a tie!')
            elif user == 3 and computer == 4:
                print('The player won!')
            elif user == 3 and computer == 5:
                print('The computer won!')

            if user == 4 and computer == 1:
                print('The computer won!')
            elif user == 4 and computer == 2:
                print('The player won!')
            elif user == 4 and computer == 3:
                print('The computer won!')
            elif user == 4 and computer == 4:
                print('Its a tie!')
            elif user == 4 and computer == 5:
                print('The player won!')
            
            if user == 5 and computer == 1:
                print('The player won!')
            elif user == 5 and computer == 2:
                print('The computer won!')
            elif user == 5 and computer == 3:
                print('The player won!')
            elif user == 5 and computer == 4:
                print('The computer won!')
            elif user == 5 and computer == 5:
                print('Its a tie!')

            keepPlaying = int(input('Keep playing? 8 - Yes | 9 - No'))

print('Thanks for playing!')