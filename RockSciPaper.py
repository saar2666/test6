import random

moves = ['rock', 'paper', 'scissors']

player1 = random.choice(moves)
player2 = random.choice(moves)

print(player1)
print(player2)


def compare(u1, u2):
    if u1 == u2:
        print("its a tie!")
    elif u1 == 'rock' and u2 == 'scissors':
        print('u1 wins!')
    elif u1 == 'rock' and u2 == 'paper':
        print('u2 wins!')
    elif u1 == 'scissors' and u2 == 'paper':
        print('u1 wins!')
    elif u1 == 'scissors' and u2 == 'rock':
        print('u2 wins!')


compare(player1, player2)
