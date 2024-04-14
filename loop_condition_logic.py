# Loop Condition Logic
#Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. 
#You will create loops with different conditions to see how they influence the behavior of the loop.
#Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true 
#(an infinite loop). Ask the user a series of questions until their answer triggers a break statement.
#Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration
# you print which iteration it is on. (use a control variable)


while True:
    game = input('Whats your favorite game? ')

    if game == 'league of legends':
        print('PLEASE UN-INSTALL!')
        break
    elif game == 'genshin impact':
        print('Id tell you too play a differant game but you spent all your money on pulls')
        break
    elif game == 'harvest moon':
        print ('all the animals are so fluffy !')
        break
    elif game == 'elden ring':
        print('YOU DIED')
        break
    else:
        print('ATLEAST ITS NOT LEAGUE!')






alist = ['1', '2', '3','4','5']
index = 0

while index < len(alist):
    print('iteration', alist[index])
    index += 1