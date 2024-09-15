import random

#to use emojis implement key-value pairs
emojis = {'r':'🪨', 'p':'📃', 's':'✂'}
while True:
    player_choice = (input("enter rock(r) paper(p) or scissors(s) ")).lower()
    option = ('r', 'p', 's')
    if player_choice not in ('r', 'p', 's'):
        print("invalid choice")
        continue #to jump back to the beginning of the  while loop
        # and ask the user to  enter the choice again

    comp_choice = random.choice(option)
    print(f'you choose {emojis[player_choice]}')
    print(f'computers choice :{emojis[comp_choice]}')

    if player_choice == comp_choice:
        print("its a tie")
    elif (
            (player_choice == 'p' and  comp_choice == 'p') or \
            (player_choice == 's' and comp_choice == 'p')or \
            (player_choice == 'r' and  comp_choice == 's')
        ):
        print("you win!!")

    else:
        print("you lost")

    con = input('do you want to continue :(y/n): ').lower()#you cannot use continue as
    # it is a reserved keyword in python
    if con == 'n':
        print("thank you for playing")
        break
