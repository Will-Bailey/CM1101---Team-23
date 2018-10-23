from player import *
from gameparser import *
from suspects import *
from map import *
from weapons import *
import random

def introduction():
    intro()

    player_name = input("Enter your name: ")

    age_verification(player_name)
    
    current_room = rooms["Lobby"]    

def main():

    correct_accusation = False
    generate_mystery()
    display_room(current_room)

    while True:

        command = ask_for_command()

        execute_command(command)

        #Victory condition
        if correct_accusation == True:
            print("Congratulations")
            break
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
    global mystery
    mystery = {
        "suspect": random.choice(list(suspects)),
        "weapon" : random.choice(list(weapons)), 
        "room": random.choice(list(rooms)[1:])
    }
    init_clues(mystery)
    generate_clues(mystery)

def generate_clues(mystery):
    ###This function is responsible for generating the correct clues to solve the
    ###mystery given to it and then asigning each of them to a room.

    rooms[mystery["room"]]["clue"] = clues["room"]
    clue_list = list(clues)[1:]

    for room in rooms:
        if room != "Lobby" and rooms[room]["clue"] == "":
            random_clue = random.choice(clue_list)
            rooms[room]["clue"] = clues[random_clue]
            clue_list.remove(random_clue)

def ask_for_command():

    print("\nWhat do you want to do?  (Type HELP for list of commands)")
    user_command = input("...")

    input_normalised = normalise_input(user_command)

    return input_normalised

def display_help(exits): #red_herrings needed

    print("\nYou can use commands:\n")
    
    for direction in exits:
        print_exit(direction, destination(exits, direction))

    #for item in red_herrings:
    #    print("CHECK " + item["id"].upper() +  " to inspect " + item["name"] + ".")

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
        display_help(current_room["exits"])
        print("OPEN NOTEBOOK to open notebook")

    elif command == ["open", "notebook"]:
        display_notebook()

    elif command == ["make", "accusation"]:
        make_accusation()

    else:
        print("This makes no sense.")

def make_accusation():
    accusation = {
    "suspect": "",
    "weapon": "",
    "room": ""
    }
    print("Who are you going to accuse?")
    print("The suspects you have highlighted are:")
    for suspect in suspects:
        if suspect["notebook_status"] == "highly suspicious":
            print(suspect["name"])
    accusation["suspect"] = normalise_input(input("..."))
    print("\n")
    print("What weapon do you think they used?")
    print("The weapons you have highlighted are:")
    for weapon in weapons:
        if weapon["notebook_status"] == "highly suspicious":
            print(weapon["name"])
    accusation["weapon"] = normalise_input(input("..."))
    print("\n")
    print("Which room do you think the murder took place in?")
    print("The rooms you have highlighted are:")
    for room in rooms:
        if room["notebook_status"] == "highly suspicious":
            print(room["name"])
    accusation["room"] = normalise_input(input("..."))
    print("\n")
    if accusation == mystery:
        corret_accusation = True

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

def display_notebook():

    while execute_notebook != "close":
        print('''\nYou opened your notebook, which section do you want to turn to?

0) Close (to close notebook)
1) Suspects
2) Weapons
3) Rooms
4) Clues

(Use number key or page name)''')
        execute_notebook(normalise_input(input("...")))
    return

def execute_notebook(command):
    #Displays the notebook for the player to change the suspicion on any of the mystery elements or to look at any clues that they've previously discovered
    #The player should input which section they'd like to view, Suspects, Weapons, Rooms or clues
        if 0 == len(command):
            return

        if command[0] == "suspects" or command[0] == "1":
            notebook_suspects()
            return
        
        elif command[0] == "weapons" or command[0] == "2" :
            notebook_weapons()
            return

        elif command[0] == "rooms" or command[0] == "3":
            notebook_rooms()
            return

        elif command[0] == "clues" or command[0] == "4":
            notebook_clues()
            return

        if command[0] == "close" or command[0] == "0":
            print("You have closed the notebook.")
            main()

        else:
            print("This makes no sense.")
            return

def editing_within_notebook(page):

    while True:
        
        yes_no_input = input("Would you like to edit the " + str(page)+ " list? (Yes/No):" "\n" "...")
        yes_or_no = normalise_input(yes_no_input)
        
        if yes_or_no == ['yes'] or yes_or_no == ['yeah'] or yes_or_no == ['y']:
            while True:
                player_command = input("What would you like to do to the " + str(page) + " list? (type 'Help' for help):" "\n" "...")
                normalised_command = normalise_input(player_command)

                if 0 == len(normalised_command):
                    continue
                
                elif normalised_command == ['help']:
                    notebook_display_help(page)
                    continue

                elif normalised_command[0] == "highlight":
                    if len(normalised_command) > 1:
                        suspicion_highlight(normalised_command[1])
                    else:
                        print("Highlight what?\n")

                elif normalised_command[0] == "cross":
                    if len(normalised_command) > 1:
                        suspicion_lowlight(normalised_command[1])
                    else:
                        print("Cross what?\n")

                elif normalised_command[0] == "reset":
                    if len(normalised_command) > 1:
                        suspicion_reset(normalised_command[1])
                    else:
                        print("Reset what?\n")

                elif normalised_command[0] == "close":
                    print("You have closed the notebook.")
                    main()

                else:
                    print("This makes no sense.\n")


        elif yes_or_no == ['no'] or yes_or_no == ['nah'] or yes_or_no == ['n']:
            display_notebook()
            break
        else:
            print("That is not a valid input. Please answer with Yes or No" + "\n")

def notebook_display_help(page):

    print("You can use commands:\n")
    print("HIGHLIGHT + \'" + page + "_name\'")
    print("CROSS + \'" + page + "_name\'")
    print("RESET + \'" + page + "_name\'")
    print("CLOSE to close notebook\n")

def notebook_suspects():
    # Displays the list of suspects sorted by their suspicion level
    print("\n\tLIST OF SUSPECTS\n")
    for suspicion in ["highly suspicious", "neutral", "unlikely"]:
        printed = False
        print("-" + suspicion.upper() + "-\n")
        for suspect in suspects:
            if suspects[suspect]["notebook_status"] == suspicion:
                for key in suspects[suspect]:
                    if key != "notebook_status":
                        print(key.title() + ": " + str(suspects[suspect][key]))
                        printed = True
                print()
        if printed == False:
            print("   None")
            print()
    editing_within_notebook("suspects")
    return

def notebook_weapons():
    # Displays the list of weapons sorted by their suspicion level

    highlighted = False
    print("\nYou open your notebook to the weapons section the list reads:")
    print("\n\tLIST OF WEAPONS\n")
    
    for weapon in weapons:
        print(weapons[weapon]["name"] + ": " + weapons[weapon]["description"])
        print()
        if weapons[weapon]["notebook_status"] == "highly suspicious":
            highlighted = weapon
    if highlighted != False:
        print("You have highlighted " + weapons[highlighted]["name"] + " as the murder weapon")
    editing_within_notebook("weapons")

def notebook_rooms():
    # Displays the list of rooms sorted by their suspicion level

    highlighted = False
    print("\nYou open your notebook to the rooms section the list reads:")
    print("\n\tLIST OF ROOMS\n")
    for room in rooms:
        print(rooms[room]["name"] + ": " + rooms[room]["description"])
        print()
        if rooms[room]["notebook_status"] == "highly suspicious":
            highlighted = room
    if highlighted != False:
        print("You have highlighted " + rooms[highlighted]["name"] + " as the room the murder took place.")
    editing_within_notebook("rooms")

def notebook_clues():
    # Displays the list of clues previously discovered by the player
    print("\n\tLIST OF CLUES\n")
    for clue in discovered_clues:
        pass

def suspicion_highlight(subject):
    edited = False
    for element in [weapons, suspects, rooms]:
        if subject in element:
            element[subject]["notebook_status"] = "highly suspicious"
            edited = True
            if element == weapons:
                notebook_weapons()
            elif element == suspects:
                notebook_suspects()
            elif element == rooms:
                notebook_rooms()
    if edited != True:
        print("You can't highlight that\n")

def suspicion_lowlight(subject):
    edited = False
    for element in [weapons, suspects, rooms]:
        if subject in element:
            element[subject]["notebook_status"] = "unlikely"
            edited = True
            if element == weapons:
                notebook_weapons()
            elif element == suspects:
                notebook_suspects()
            elif element == rooms:
                notebook_rooms()
    if edited != True:
        print("You can't cross off that\n")
    notebook_suspects()

def suspicion_reset(subject):
    edited = False
    for element in [weapons, suspects, rooms]:
        if subject in element:
            element[subject]["notebook_status"] = "neutral"
            edited = True
            if element == weapons:
                notebook_weapons()
            elif element == suspects:
                notebook_suspects()
            elif element == rooms:
                notebook_rooms()
    if edited != True:
        print("You can't reset that\n")
    notebook_suspects()

def show_status():
    pass

def display_room(room):

    print("\n" + room["name"].upper() + "\n\n" + room["description"] + "\n")
    
    if room != rooms["Lobby"]:
        clue_number = random.randint(0, 3)
        print(clue_number)
        if clue_number == 0:
            print(room["clue"]["first look"])
        position = 1
        for red_herring in room["red herrings"]:
            print(red_herring)
            if position == clue_number:
                print(room["clue"]["first look"])
            position = position + 1

def init_clues(mystery):
    global clues
    clue_room = {
        "detail": "stain",
        "first look": "There's a smalll red stain on the floor just visible behind the open door.",
        "closer inspection": "As you look more closely you notide discover a larger puddle of blood. Clearly this must be the room in which the murder was committed.",
    }

    clue_witness = {
        "detail": "butler",
        "first look": "The BUTLER is in this room, tidying up",
        "closer inspection": """You ask the butler if he saw anything he replys in a frail, voice "I did,"" he replys "I saw the silhouette of a person dragging off what looked like a body earlier. I couldn't tell who it was but they were definitely a """ + suspects[mystery["suspect"]]["build"] +""" person. I'm sorry bu that's all I know." You thank the butler""" 
    }

    clue_clothes = {
        "detail": "fabric",
        "first look": "Snagged on the door, you spot a scrap of FABRIC.",
        "closer inspection": "As you look closer at the farbic, you notice spots of blood on what must be a scrap of clothing. You also notice that the scrap is from " + suspects[mystery["suspect"]]["sex"] + "'s clothing."
    }

    clue_hair = {
        "detail": "scuff",
        "first look": "There's a SCUFF on the wall, it looks like someone scraped against the wall, carrying something heavy.",
        "closer inspection": "You look more carefully and realise that the mark was clearly form the killer on there way past, dragging the body. There are drips of blood and you also find a lock of hair, snagged on a nail that the killer must have brushed past on their way. The hair is clearly " + suspects[mystery["suspect"]]["hair colour"] + "."
    }

    clue_weapon = {
        "detail": "rug",
        "first look": "There's something vaugley shiny sticking out from under a RUG.",
        "closer inspection": "You peel back teh corner of the rug and find a blood stained " + mystery["weapon"] + ". The killer must have used this to commit the murder and then hidden it here."
    }


    clues = {
        "room": clue_room,
        "witness": clue_witness,
        "clothes": clue_clothes,
        "hair": clue_hair,
        "weapon": clue_weapon
    }

def execute_inspect(detail):
    if detail == current_room["clue"]["detail"]:
        print(current_room["clue"]["closer inspection"])
    elif detail in current_room["details"]:
        detail_number = current_room["details"].index(detail)
        print(current_room["red herrings"][list(current_room["red herrings"])[detail_number]])
    else:
        print("You can't inspect that.")

if __name__ == "__main__":
    introduction()
    main()
