import random

#to use emojis implement key-value pairs
emojis = {'r':'🪨', 'p':'📃', 's':'✂'}
option = ('r', 'p', 's')
def get_player_choice():
    while True:
        player_choice = (input("enter rock(r) paper(p) or scissors(s) ")).lower()

        if player_choice not in ('r', 'p', 's'):
            print("invalid choice")
            continue  # to jump back to the beginning of the  while loop
            # and ask the user to  enter the choice again
        else:
            return player_choice
def display_choices(player_choice, comp_choice):
    print(f'you choose {emojis[player_choice]}')
    print(f'computers choice :{emojis[comp_choice]}')
def winner(player_choice, comp_choice):
    if player_choice == comp_choice:
        print("its a tie")
    elif (
            (player_choice == 'p' and comp_choice == 'r') or \
            (player_choice == 's' and comp_choice == 'p')or \
            (player_choice == 'r' and comp_choice == 's')
        ):
        print("you win!!")

    else:
        print("you lost")
def play_game():
    while True:
        user_choice =  get_player_choice()

        comp_choice = random.choice(option)
        display_choices(user_choice, comp_choice)
        winner(user_choice, comp_choice)


        con = input('do you want to continue :(y/n): ').lower()#you cannot use continue as
        # it is a reserved keyword in python
        if con == 'n':
            print("thank you for playing")
            break

play_game()
