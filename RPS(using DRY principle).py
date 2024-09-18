import random

# we use caps to declare constants
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
#to use emojis implement key-value pairs
emojis = {'r':'🪨', 'p':'📃', 's':'✂'}
emojis = {'r':'🪨', 'p':'📃', 's':'✂'}
option = tuple(emojis.keys())
def get_player_choice():
    while True:
        player_choice = (input("enter rock(r) paper(p) or scissors(s) ")).lower()

        if player_choice not in ('r', 'p', 's'):
            print("invalid choice")
            continue  # to jump back to the beginning of the  while loop
            # and ask the user to  enter the choice again
        else:
            return player_choice
def
