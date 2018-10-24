#from items import *
from map import rooms
from gameparser import *

current_room = rooms["lobby"]

def age_verification(name):

    while True:

        try:
            print("How old are you?")
            player_age = int(input("..."))

            if player_age < 0 or player_age > 100:
                print("Please enter age between 1-100")
                continue

            elif player_age >= 13:
                print_welcome(name)

            else:
                print("You are too young to play this game.")
                quit()
            break
        
        except ValueError:
            print("You did not enter a valid number.")

def print_welcome(name):

    print("\nWelcome " + str(name.title()) + ". Please choose difficulty level.")
    print('''
    1) Easy
    2) Medium
    3) Hard
    ''')
    
    difficulty_picked = False
    
    while difficulty_picked == False:

        difficulty = normalise_input(input("Use number key or difficulty name.\n..."))
        
        if difficulty == ["hard"] or difficulty == ["3"]:
            attempts_remaining = 1
            difficulty_picked = True
            
        elif difficulty == ["medium"] or difficulty == ["2"]:
            attempts_remaining = 3
            difficulty_picked = True
            
        elif difficulty == ["easy"] or difficulty == ["1"]:
            attempts_remaining = 5
            difficulty_picked = True
        else:
            print("please enter a valid input\n")
