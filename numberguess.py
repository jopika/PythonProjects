from random import randint
import time


def main():
    # Code goes here
    randomNum = 0
    randomNum = randint(1,100)
    print(randomNum)

    numGuess = 0
    numGuessHigh = 0
    numGuessLow = 0

    
    finished = 0

    while finished != 1:
        print('Current number of guesses: ', numGuess)
        guess = int(input('What number do you think I am guessing?: '))
        numGuess = numGuess + 1
        if guess == randomNum:
            finished = 1
            print('You guessed it! ' , guess , ' Was the right answer!')
            print('It took you ' , numGuess , ' tries.')
        elif guess > randomNum:
            print('Incorrect, guess was too high.')
            numGuessHigh = numGuessHigh + 1
        else:
            print('Incorrect, guess was too low.')
            numGuessLow = numGuessLow + 1

    print('You guessed', numGuessHigh, 'times too high')
    print('You guessed', numGuessLow, 'times too low')

# # if __name__ == '__main__':
# #     main()

main()
