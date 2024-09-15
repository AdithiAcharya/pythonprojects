import random

while True: #loop
    a = input("roll the dice  (y/n): ").lower()
    if a == 'y':
        #to generate any 2 random numbers  we need to import random module
        die1 = random.randint(1,6) #randint is used to generate any 2 random integers
        die2 = random.randint(1, 6)
        print(f'({die1 } , { die2})')#to  print the 2 numbers using formatted string
    elif a == 'n':
        print("thank you for playing")
        break # to break the given while loop
    else:
        print("invalid")
