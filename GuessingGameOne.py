import random

guessNum = input("guess the number")
randedNum = random.choice(1,9)

if guessNum < randedNum:
    print("too low")
elif guessNum > randedNum:
    print('too high')
else:
    print('correct!')