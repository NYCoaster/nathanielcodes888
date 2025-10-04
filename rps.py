import random
playerselection = input ('Please Pick a Number. Rock is 0, Paper is 1, and Scissors is 2')
botselection = random.randint(0,2)
if botselection == 0 and playerselection == '2':
    print ('You lost bot picked rock')
elif botselection == 0 and playerselection == '1':
    print ('You won bot picked rock')
elif botselection == 0 and playerselection == '0':
    print ('You tied bot picked rock')
elif botselection == 1 and playerselection == '0':
    print ('You lost bot picked paper')
elif botselection == 1 and playerselection == '2':
    print ('You won bot picked paper')
elif botselection == 1 and playerselection == '1':
    print ('You tied bot picked paper')
elif botselection == 2 and playerselection == '1':
    print ('You lost bot picked scissors')
elif botselection == 2 and playerselection == '0':
    print ('You won bot picked scissors')
elif botselection == 2 and playerselection == '1':
    print ('You tied bot picked scissors')
again = input ('Do you want to play again')

while again := 'y':
    import random
    playerselection = input ('Please Pick a Number. Rock is 0, Paper is 1, and Scissors is 2')
    botselection = random.randint(0,2)
    if botselection == 0 and playerselection == '2':
        print ('You lost bot picked rock')
        again = input ('Do you want to play again')
    elif botselection == 0 and playerselection == '1':
        print ('You won bot picked rock')
        again = input ('Do you want to play again')
    elif botselection == 0 and playerselection == '0':
        print ('You tied bot picked rock')
        again = input ('Do you want to play again')
    elif botselection == 1 and playerselection == '0':
        print ('You lost bot picked paper')
        again = input ('Do you want to play again')
    elif botselection == 1 and playerselection == '2':
        print ('You won bot picked paper')
        again = input ('Do you want to play again')
    elif botselection == 1 and playerselection == '1':
        print ('You tied bot picked paper')
        again = input ('Do you want to play again')
    elif botselection == 2 and playerselection == '1':
        print ('You lost bot picked scissors')
        again = input ('Do you want to play again')
    elif botselection == 2 and playerselection == '0':
        print ('You won bot picked scissors')
        again = input ('Do you want to play again')
    elif botselection == 2 and playerselection == '1':
        print ('You tied bot picked scissors')
        again = input ('Do you want to play again')

