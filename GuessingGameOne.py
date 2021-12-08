import random
randedNum = random.randint(1, 9)
print randedNum
guessNum = ''

while guessNum != 'exit' and guessNum != randedNum:
    guessNum = input("guess the number: ")
    if guessNum < randedNum:
        print("too low,try again")
    elif guessNum > randedNum:
        print('too high,try again')
    elif guessNum == randedNum:
        print('correct!')
