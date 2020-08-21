import random
player_wins = 0
computer_wins = 0
winning_score = 3
while player_wins < winning_score and computer_wins < winning_score:
    print(f'Player score: {player_wins} Computer score: {computer_wins}')
    print("...Rock Paper Scissors...")
    p1 = input("Enter your choice : ").lower()
    if p1 == 'quit' or p1 == 'q':
        break
    n = random.randint(1,3)
    choiceList = ['rock', 'paper', 'scissors']
    if p1 in choiceList:
        if n == 1:
            p2 = 'rock'
        elif n == 2:
            p2 = 'paper'
        else:
            p2 = 'scissors'
        print("Computer chose : ", p2)
        if not p1:
            print("something went wrong")
        elif p1 == p2:
            print("it's a tie")
        elif p1 == 'rock' and p2 == 'scissors':
                print("Player wins")
                player_wins += 1
        elif p1 == 'scissors'and p2 == 'paper':
                print("Player 1 wins")
        elif p1 == 'paper'and p2 == 'rock':
                print("Player wins")  
                player_wins += 1
        else:
                print("Computer wins")
                computer_wins += 1
    else:
        print("Enter a valid input please")
if player_wins > computer_wins:
    print('Conngrats, you won!')
elif player_wins == computer_wins:
    print("It's a tie!!!")
else:
    print('Oops, Computer won :p')
print(f'Final scores... Player score: {player_wins} Computer score: {computer_wins}')