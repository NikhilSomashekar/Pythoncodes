import random
#x = None
random_number = random.randint(1,10)
while True:
    x = int(input("Guess a number between 1 and 10: "))
    if x > random_number:
        print("Too high, try again!")
    elif x < random_number:
        print("Too low, try again!")
    else:
        print("You guessed it! You won!")
        p = input("Do you want to keep playing? (y/n) ")
        if p == "y":
            random_number = random.randint(1,10)
            x = None
        else:
            print("Thanks for playing. Bye!")
            break

    