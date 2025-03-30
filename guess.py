from random import randint


solution = randint(1,10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > solution:
        print("Too high, try again!")
    elif guess < solution:
        print("Too low, try again!")
    elif guess == solution:
        print("You guessed it! You won!")
        play_again = input("Do you want to keep playing? (y/n): ")
        if play_again == 'y':
            solution = randint(1, 10)
        else:
            print("Thanks for playing!")
            break