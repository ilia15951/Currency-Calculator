import random
Rock = '1'
Paper = '2'
Scissors = '3'
print('Welcome to Rock, Paper Scissors! The game of all kids to decide on something. \nIn this game you will have to beat the computer once. \n(Psst if it\'s a draw the start the program again! ;D)\nSo how to play. Well, it\'s simple. Pick 1 for Rock, 2 for Paper and 3 for Scissors. \nSo Rock beats Scissors. Scissors cuts Paper and Paper covers Rock. Got it Lets play')
player=int(input('Please enter number 1 = Rock, 2 = Paper, 3 = Scissors: '))

if player<1 or player>3 or player==9:
   player=int(input('Invalid number. Please enter number 1 = Rock, 2 = Paper, 3 = Scissors: '))
   if player<1 or player>3:
       print('Well, now you can\'t play this game because you are mucking around. Next time DON\'T!')
elif player==9:
    exit()
else:
   computer=random.randint(1, 3)
   print(player,computer)
   print('Remember Rock = 1, Paper = 2 and Scissors = 3')
   if player==1 and computer==1 or player==2 and computer==2 or player==3 and computer==3:
       print('It\'s a draw. =l Restart the game if you want to.')
   if player==1 and computer==2 or player==2 and computer==3 or player==3 and computer==1:
       print('Computer wins! You lose. Sorry. =(')
   if player==1 and computer==3 or player==2 and computer==1 or player==3 and computer==2:
       print('You have won. Well done. =D')