from random import randint

game = True
solution = randint(1,10)
while game:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > solution:
        print("Too high, try again!")
    elif guess < solution:
        print("Too low, try again!")
    elif guess == solution:
        print("You guessed it! You won!")
        break
    play_again = input("Do you want to keep playing? (y/n): ")
    if play_again == 'y':
        game = True
    else:
        game = False