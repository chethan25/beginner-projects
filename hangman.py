import random
import string
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O] |
 /|\ |
 / \ |
    ===''']

words = {'Colors': 'red orange yellow green blue indigo violet white black brown'
         .split(),
         'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoidchevron'
         'pentagon hexagon septagon octagon'.split(),
         'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry'
         'banana cantaloupe mango strawberry tomato'.split(),
         'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle'
         'fish frog goat leech lion lizard monkey moose mouse otter owl panda'
         'python rabbit rat shark sheep skunk squid tiger turkey turtle weasel'
         'whale wolf wombat zebra'.split()}


def getRandomWord(wordDict):
    # This function returns a random string from the passed dictionary
    # of lists of strings and its key
    # First randomly select a key from the dictionary
    wordKey = random.choice(list(wordDict.keys()))
    # Second randomly select a key from the dictionary
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(missedLetters, correctLetters, secretWord):
    # This function prints missed letters and correctly guessed letter
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter player entered
    while True:
        guess = input('\nGuess a letter. ').lower()
        if len(guess) != 1:
            print('Please enter a single letter. ')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again. ')
        elif guess not in set(string.ascii_lowercase):
            print('Please enter a LETTER. ')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again;
    # otherwise it returns False.
    print('Do you want to play again? (yes or no) ')
    return input().lower().startswith('y')


print('H A N G M A M')
difficulty = ' '
while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print(f'The secret word is in the set: {secretSet}')
    displayBoard(missedLetters, correctLetters, secretWord)
    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Yes! The secret word is {secretWord}! You have won!')
            print(f'You took {len(missedLetters) + len(correctLetters)}'
                  f' attempts to guess the word ')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f'You have run out of guesses!')
            print(f'After {len(missedLetters)} missed guesses'
                  f' and {len(correctLetters)} correct guesses, the word was'
                  f' "{secretWord}"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is
    # done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
