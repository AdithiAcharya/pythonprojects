import random
count = 0
while True:
    a = input("enter your choice (y/n)").lower()
    if a == 'y':
        roll = input("enter the number of times you want to roll thw die")
        for i in range(int(roll)):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            count += 1
            print(f'({die1} , {die2})')

    elif a == 'n':
        print("thank you for playing the game ")
        print(f"the total number  of counts is {count}")
        break

    else:
        print("invalid choice")
