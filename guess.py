import random

while True:
    print('Guess a number from 1-20.')
    bot = random.randint(1,20)
    guess = int(input('Number: '))

    print(guess)

    if guess > bot:
        print('Your number is too high')
    elif guess < bot:
        print('Your number is too low')
    elif guess == bot:
        print('You guessed it right!')
    else:
        print('Sorry, that was an invalid answer!')

    print('The correct number is '+ str(bot))

    try_again = int(input("Press 1 to try again, 0 to exit. "))
    if try_again == 0:
        break # break out of the outer while loop
