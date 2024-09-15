import random

guess = random.randint(1,10)

print("welcome to guess game")

while True:
    try:
        num = int(input("enter the number between 1 and 10 "))
        if num < guess:
            print("too low")
        elif num > guess:
            print("too high")
        else:
            print("you guessed the number right")
            break
    except ValueError:
        print("enter a valid  number")
