from player import *
from items import *
from gameparser import *
from suspects import *
from map import *
#rooms = {}#from map import * #Awaiting dictionary
weapons = {}#from weapons import * #Awaiting dictionary
import random
def introduction():
    intro()

    player_name = input("Enter your name: ")

    age_verification(player_name)
    
    current_room = rooms["Lobby"]    

def main():

    display_room(current_room)

    while True:

        command = ask_for_command(current_room["exits"], current_room["items"], inventory)

        execute_command(command)

        #Victory condition
        #if whatever:
        #    print("Congratulations")
        #    break
        #Game over
        #elif life == 0:
        #    print("Game over")
        #    break

def generate_mystery():
    ### This function should randomly generate a dictionary (called "mystery")
    ###that uses the terms "suspect", "weapon" and "room"
    ###as keys and randomly picks a room, suspect and weapon from the respective
    ###dicitonaries and asigns them as values. Once it has done this, the
    ###function should then call the generate_clues function to finish off the
    ###setup.
    mystery = {
        "suspect": random.choice(list(suspects))
        #"weapon": random.choice(list(weapons)) #Awaiting dictionary
        #"room": random.choice(list(room)) #Awaiting dictionary
    }
    generate_clues(mystery)

def generate_clues(mystery):
    ###This function is responsible for generating the correct clues to solve the
    ###mystery given to it and then asigning each of them to a room.

    clues = {
        "room": """On closer inspection of the room, you notice a splatter of
                      blood on the wall and below it a puddle of yet more blood.
                      clearly this is the room in which the murder took place""",
        "witness": "" + suspects[mystery[suspect]]["build"] + "", ###A string about interviewing a witness of some kind who claims they saw a sillhouette of the murderer and that they were (tall/short)
        "clothes" : "" + suspects[mystery[suspect]]["sex"] + "", ###A string about finding a scrap of (male/female) clothing clearly belonging to the murderer
        "hair": "" + suspects[mystery[suspect]]["hair"] + "", ###A string about finding a lock of (black/blonde) hair clearly belonging to the murderer
        "weapon": "" + mystery["weapon"] + "" ###A string about finding the murder weapon using mystery["weapon"]    
        }

    rooms[mystery[room]][clue] = clues[room]

    for room in rooms:
        if room[name] != "lobby" and room[clue] == "":
            room[clue] = clues[random.choice(list(clues)[1:])]

def ask_for_command(exits, room_items, inv_items): # Not inv items

    print("\nWhat do you want to do?  (Type HELP for list of commands)")
    user_command = input("...")

    input_normalised = normalise_input(user_command)

    return input_normalised

def display_help(exits, room_items, inv_items):

    print("\nYou can use commands:\n")
    
    for direction in exits:
        print_exit(direction, destination(exits, direction))

    for items in room_items:
        print("CHECK " + items["id"].upper() +  " to inspect " + items["name"] + ".")

    #for item in inv_items:
    #    print("USE " + item["id"].upper() + " to use " + item["name"] + ".")

def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ".")

def move(exits, direction):

    return(rooms[exits[direction]])

def destination(exits, direction): #formerly exit_leads_to

    return rooms[exits[direction]]["name"]

def is_valid_exit(exits, chosen_destination):

    return chosen_destination in exits

def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("inspect what?")

    elif command[0] == "help":
        display_help(current_room["exits"], current_room["items"], inventory)

    elif command == ["open", "notebook"]:
        display_notebook()

    else:
        print("This makes no sense.")

def execute_go(direction):

    global current_room

    exits = current_room["exits"]
    if is_valid_exit(exits, direction):
        current_room = move(exits, direction)
        display_room(current_room)
    else:
        print("You cannot go there.")

def display_details(room):
    #This function combines the 3 red herrings and the clue from a room, randomly inserting the clue to hide it.
    #it then returns the text as one string to be printed after the rooms description. 
    pass

def execute_inspect(detail):
    #This will return the "Closer inspection" text asigned to each red hearing and each clue
    pass

def display_notebook():

    while execute_notebook != "close":
        print("\nYou opened your notebook, which section do you want to turn to?")
        execute_notebook(normalise_input(input("...")))
    return

def execute_notebook(command):
    #Displays the notebook for the player to change the suspicion on any of the mystery elements or to look at any clues that they've previously discovered
    #The player should input which section they'd like to view, Suspects, Weapons, Rooms or clues
        if 0 == len(command):
            return

        if command[0] == "suspects":
            notebook_suspects()
            return
        
        elif command[0] == "weapons":
            notebook_weapons()
            return

        elif command[0] == "rooms":
            notebook_rooms()
            return

        elif command[0] == "clues":
            notebook_clues()
            return

        if command[0] == "highlight":
            if len(command) > 1:
                suspicion_highlight(command[1])
            else:
                print("Highlight what?")
            return

        if command[0] == "cross":
            if len(command) > 1:
                suspicion_lowlight(command[1])
            else:
                print("Cross out what?")
            return

        if command[0] == "reset":
            if len(command) > 1:
                suspicion_reset(command[1])
            else:
                print("reset what?")
            return

        if command[0] == "close":
            print("You have closed the notebook.")
            main()

        else:
            print("This makes no sense.")
            return
def editing_within_notebook(page):
    a = input("Would you like to edit the " + str(page) + " list?:")
    if normalise_input(a) == ['yes'] or normalise_input(a) == ['yeah'] or normalise_input(a) == ['y']:
        b = input("What would you like to do to the suspects list? (type 'Help' for help):")
        execute_notebook(normalise_input(b))
    

def notebook_suspects():
    # Displays the list of suspects sorted by their suspicion level  
    for suspicion in ["highly suspicious", "neutral", "unlikely"]:
        printed = False
        print("-" + suspicion.upper() + "-")
        for suspect in suspects:
            if suspects[suspect]["notebook_status"] == suspicion:
                for key in suspects[suspect]:
                    if key != "notebook_status":
                        print("Suspect " + key + ": " + str(suspects[suspect][key]))
                        printed = True
                print()
        if printed == False:
            print()
            print("None")
            print()
    editing_within_notebook("suspects")

def notebook_weapons():
    # Displays the list of weapons sorted by their suspicion level
    highlighted = False
    print("\nYou open your notebook to the weapons section the list reads:")
    for weapon in weapons:
        print(weapons[weapon]["name"] + ": " + weapons[weapon][description])
        print("\n")
        if weapons[weapon][notebook_status] != "neutral":
            highlighted = weapon
    if highlighted != False:
        print("You have highlighted " + weapons[highlighted]["name"] + " as the murder weapon")
    editing_within_notebook("weapons")

def notebook_rooms():
    # Displays the list of rooms sorted by their suspicion level
    pass

def notebook_clues():
    # Displays the list of clues previously discovered by the player
    pass

def suspicion_highlight(subject):
    edited = False
    for element in [weapons, suspects, rooms]:
        subject=subject.title()
        if subject in element:
            element[subject]["notebook_status"] = "highly suspicious"
            edited = True
    if edited != True:
        print("You can't highlight that")
    notebook_suspects()

def suspicion_lowlight(subject):
    edited = False
    for element in [weapons, suspects, rooms]:
        subject=subject.title()
        if subject in element:
            element[subject]["notebook_status"] = "unlikely"
            edited = True
    if edited != True:
        print("You can't cross off that")
    notebook_suspects()

def suspicion_reset(subject):
    edited = False
    for element in [weapons, suspects, rooms]:
        subject=subject.title()
        if subject in element:
            element[subject]["notebook_status"] = "neutral"
            edited = True
    if edited != True:
        print("You can't reset that")
    notebook_suspects()

def show_status():
    pass

def display_room(room):

    print("\n" + room["name"].upper() + "\n\n" + room["description"] + "\n")

if __name__ == "__main__":
    introduction()
    main()
