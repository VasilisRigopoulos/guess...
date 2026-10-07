from random import randint
from rich import print

L = 1
R = 100

guessed = []

max_tries = 7
tries = 1

guessed_right = False

number = randint(L,R)



tries_list = ['blue','blue','green','green','yellow','red']

while tries < max_tries:
    print()
    try:
        guess = int(input(f'guess a number inbetween {L} and {R}: '))
    except:
        print('[yellow]INPUT A NUMBER. NOTHING ELSE.')
        continue

    print()
    
    if guess > R or guess < L:
        print('[red]out of bounds man ￣へ￣')
        continue

    if guess in guessed:
        print('[yellow]YOU ALREADY GUESSED THAT NUMBER, HOW CAN YOU FORGET IT???????????????????????')
        print(f'[yellow]FINE, I\'LL HELP YOU. YOU ALREADY GUESSED {guessed}')
        continue
    else:
        guessed.append(guess)

    if guess == number:
        guessed_right = True
        break
    
    print(f'opps, wrong number!, [{tries_list[tries - 1]}]you have {max_tries - tries} left...')

    if guess > number:
        print('guess lower.')
    else:
        print('guess higher.')

    tries += 1

    

if guessed_right: print(f'you guessed right!, it was {number} [white]ヾ(•ω•`)o')
else: print(f'you didnt guess the number. it was {number}')

