#from items import *
from map import rooms
from gameparser import *

#inventory = [item_id, item_laptop, item_money]

# Start game at the Lobby
current_room = rooms["lobby"]
#player_name = ""

def age_verification(name):

    while True:

        try:
            print("How old are you?\n")
            player_age = int(input("..."))

            if player_age < 0 or player_age > 100:
                print("Please enter age between 1-100")
                continue

            elif player_age >= 13:
                #Welcome
                print_welcome(name)

            else:
                print("You are too young to play this game.")
                quit()
            break
        
        except ValueError:
            print("You did not enter a valid number.")

def print_welcome(name):

    print("Welcome " + str(name.title()) + ", ")

    
