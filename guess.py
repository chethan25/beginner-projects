# This is a guess the number game
import random

guessesTaken = 0

myName = input('Hello! What is your name? ')

number = random.randint(1, 20)
print(f'Well, {myName} I am thinking of a number between 1 and 20.')

for guessesTaken in range(5):
    guess = int(input('Take a guess. '))

    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    elif guess == number:
        break

if guess == number:
    print(
        f'Good job, {myName}! You guessed my number in {guessesTaken+1}\
 guesses')

if guess != number:
    print(f'Nope, The number I was thinking of was {number}.')
