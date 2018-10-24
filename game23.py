from player import *
from gameparser import *
from suspects import *
from map import *
from weapons import *
from TitleASCII import *
import random

def new_game():
    introduction()
    main()
    
def introduction():
    
    global player_name
    title()
    print("Enter your name:")
    player_name = input("...")

    age_verification(player_name)
    #intro()
    
    current_room = rooms["lobby"]
    global correct_accusation
    correct_accusation = False
    global found_clues
    found_clues = []
    generate_mystery()
    global attempts_remaining
    attempts_remaining=5
 
def intro():

    #Intro
    scroll_text("\n\nRing Ring,", 0.04)
    time.sleep(0.4)
    scroll_text("\nRing Ring,", 0.04)
    time.sleep(0.4)
    scroll_text("\n" + """A rusty voice at the other end of the line grunts,
'Hello? Is this Inspector """ + player_name.title() +  "?'.\n", 0.03)
    time.sleep(0.5)
    scroll_text("""You answer, huskily, 'It certainly is'.\n""", 0.03)
    time.sleep(0.5)                
    scroll_text("'Professor Parker has been murdered in Morebrandt mansion and we need your help!'",0.03)
    time.sleep(0.7)
    scroll_text("\n'We have all 6 suspects gathered in the lobby, and all the rooms are available for inspection'.",0.03)
    time.sleep(0.9)
    scroll_text("\n'We are counting on you to bring the killer to justice'.\n", 0.03)
    time.sleep(0.4)

def main():
    display_room(current_room)
    
    while True:

        command = ask_for_command()

        execute_command(command)

        #Victory condition

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

    random_clue_list = list(clues)
    random_room_list = list(rooms)
    random_clue_list.remove("room")
    random_room_list.remove("lobby")
    random_room_list.remove(mystery["room"])
    
    random.shuffle(random_clue_list)
    random.shuffle(random_room_list)

    for n in range(0,4):
        rooms[random_room_list[n]]["clue"] = clues[random_clue_list[n]]

def ask_for_command():

    print("\nWhat do you want to do?  (Type HELP for list of commands)")
    user_command = input("...")

    input_normalised = normalise_input(user_command)

    return input_normalised

def display_help(exits):

    print("\nYou can use commands:\n")
    
    for direction in exits:
        print_exit(direction, destination(exits, direction))

    #for item in details:
    #    print("CHECK " + item.upper() +  " for closer inspection.")
    print("CHECK + <object> for closer inspection.")
    print("ACCUSE to make accusation.")
    print("OPEN NOTEBOOK to open notebook")
    
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

    elif command[0] == "check":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("inspect what?")

    elif command[0] == "help":
        display_help(current_room["exits"])

    elif command == ["open", "notebook"]:
        display_notebook()

    elif command == ["accuse"]:
        make_accusation()
        

    else:
        print("This makes no sense.")

def make_accusation():
    comparison_mystery = {}
    global attempts_remaining
    for element in mystery:
    	comparison_mystery.update({element: normalise_input(mystery[element])})

    accusation = {
    "suspect": "",
    "weapon": "",
    "room": ""
    }
    while True:
        a=input("""\nTo make an accusation you need to find out:
• The suspected killer
• The supected murder weapon
• The room of the murder
\nThere will be consequences if you get the case incorrect
\nAre you sure you want to make an accusation.(Yes/No):\n...""")
        if normalise_input(a)==["yes"] or normalise_input(a)==["y"] or normalise_input(a)==["yeah"]:
            print("\nWho are you going to accuse?")
            print("\nThe suspects you have highlighted are:")
            while True:
                for suspect in suspects:
                    if suspects[suspect]["notebook_status"] == "highly suspicious":
                        print(suspect["name"])
                    suspect_accused = normalise_input(input("..."))
                    if "".join(normalise_input(suspect_accused)) in list(suspects):
                        accusation["suspect"] = suspect_accused
                        print("\nWhat weapon do you think they used?")
                        print("\nThe weapons you have highlighted are:")
                        while True:
                            for weapon in weapons:
                                if weapons[weapon]["notebook_status"] == "highly suspicious":
                                    print(weapons[weapon]["name"])
                            weapon_accused = normalise_input(input("...")) 
                            if "".join(normalise_input(weapon_accused)) in list(weapons):
                                    accusation["weapon"] = weapon_accused
                                    print("\nWhich room do you think the murder took place in?")
                                    print("\nThe rooms you have highlighted are:")
                                    while True:
                                        for room in rooms:
                                            if rooms[room]["notebook_status"] == "highly suspicious":
                                                print(rooms[room]["name"])
                                            room_accused = normalise_input(input("...")) 
                                            if " ".join(room_accused) in list(rooms):
                                                accusation["room"] = room_accused
                                                if accusation == comparison_mystery:
                                                    game_won()
                                                else:
                                                    print("\nYour accusation doesn't make sense.\n")
                                                    attempts_remaining-=1
                                                    incorrect_accusations()
                                                    if attempts_remaining==0:
                                                        game_over()
                                                        
                                                    else:
                                                        main()
                                            else:
                                                print("Please enter a valid room")
                            else:
                                print("Please enter a valid weapon name")
                    else:
                        print("Please enter a valid name")
        elif normalise_input(a)==["no"] or normalise_input(a)==["n"] or normalise_input(a)==["nah"]:
            main()
        else:
            print("Please answer Yes or No")
            
def incorrect_accusations():
    if attempts_remaining==4:
        print("The case seems to be more complicated than you think, the residents of Morebrandt are giving you some space to try to piece the puzzle together.")
    elif attempts_remaining==3:
        print("The residents of Morebrandt are starting to look a bit more worried, but even the best detectives make mistakes. Right?")
    elif attempts_remaining==2:
        print("People are getting more and more nervous as you can't seem to make sense of the clues you have.")
    elif attempts_remaining==1:
        print("What little hope that remained of the Morebrandt residents has completely vanished, everyone is panicking. You feel as though you have 1 more attempt at finding the killer.")  
    
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
                    if len(normalised_command) > 1 and normalised_command[1:3]==['dining', 'room']:
                        suspicion_change((" ".join(normalised_command[1:3])), "highly suspicious")
                    elif len(normalised_command) > 1:
                        suspicion_change(normalised_command[1], "highly suspicious")
                    else:
                        print("Highlight what?\n")

                elif normalised_command[0] == "cross":
                    if len(normalised_command) > 1 and normalised_command[1:3]==['dining', 'room']:
                        suspicion_change((" ".join(normalised_command[1:3])), "unlikely")
                    elif len(normalised_command) > 1:
                        suspicion_change(normalised_command[1], "unlikely")
                    else:
                        print("Cross what?\n")

                elif normalised_command[0] == "reset":
                    if len(normalised_command) > 1 and normalised_command[1:3]==['dining', 'room']:
                        suspicion_change((" ".join(normalised_command[1:3])), "neutral")
                    elif len(normalised_command) > 1:
                        suspicion_change(normalised_command[1], "neutral")
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
    print("\nYou open your notebook to the weapons section the list reads:")
    print("\n\tLIST OF WEAPONS\n")
    for suspicion in ["highly suspicious", "neutral", "unlikely"]:
        printed = False
        print("-" + suspicion.upper() + "-\n")
        for weapon in weapons:
            if weapons[weapon]["notebook_status"] == suspicion:
                print("Weapon Name:\n" + weapons[weapon]["name"])
                print("Weapon Description:\n" + weapons[weapon]["description"] + "\n")
                printed = True
                print()
        if printed == False:
            print("   None")
            print()
    editing_within_notebook("weapons")
    return
    
def notebook_rooms():
    # Displays the list of rooms sorted by their suspicion level
    print("\nYou open your notebook to the weapons section the list reads:")
    print("\n\tLIST OF ROOMS\n")
    for suspicion in ["highly suspicious", "neutral", "unlikely"]:
        printed = False
        print("-" + suspicion.upper() + "-\n")
        for room in rooms:
            if rooms[room]["notebook_status"] == suspicion:
                print("Room Name: " + rooms[room]["name"])
                print("Room Description: " + rooms[room]["description"] + "\n")
                printed = True
        if printed == False:
            print("   None")
            print()
    editing_within_notebook("rooms")
    return

def notebook_clues():
    # Displays the list of clues previously discovered by the player
    print("\n\tLIST OF CLUES\n")
    if found_clues != []:
        for explored_room in found_clues:
            print("You explored the " + explored_room["name"] + " and investigated the " + explored_room["clue"]["detail"].upper() + ".")
            print(explored_room["clue"]["closer inspection"])
            print()
    else:
        print("You are yet to find any useful clues.")
    
def suspicion_change(subject, suspicion):
    edited = False
    for element in [weapons, suspects, rooms]:
        if subject in element:
                element[subject]["notebook_status"] = suspicion
                edited = True
                if element == weapons:
                    notebook_weapons()
                elif element == suspects:
                    notebook_suspects()
                elif element == rooms:
                	notebook_rooms()
        if element == suspects:
            for suspect in suspects:
                for attribute in ["sex", "build", "hair colour"]:
                    if subject == suspects[suspect][attribute]:
                        suspects[suspect]["notebook_status"] = suspicion
                        edited = True
            if edited == True:
                notebook_suspects()

    if edited != True:
        print("You can't edit that\n")

def show_status():
    pass

def display_room(room):

    print("\n" + room["name"].upper() + "\n\n" + room["description"] + "\n")
    
    if room != rooms["lobby"]:
        clue_number = random.randint(0, 3)
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
        "first look": "There's a smalll red STAIN on the floor just visible behind the open door.",
        "closer inspection": """As you look more closely you discover a larger puddle of blood.
Clearly this must be the room in which the murder was committed.""",
    }

    clue_witness = {
        "detail": "butler",
        "first look": "The BUTLER is in this room, tidying up",
        "closer inspection": """You ask the butler if he saw anything.
He replies in a frail voice
'I did, I saw the silhouette of a person dragging off what looked like a body earlier.'
'I couldn't tell who it was but they were definitely a """ + suspects[mystery["suspect"]]["build"] + """ person.'
'I'm sorry but that's all I know.'
You thank the butler""" 
    }

    clue_clothes = {
        "detail": "fabric",
        "first look": "Snagged on the door, you spot a scrap of FABRIC.",
        "closer inspection": """As you look closer at the farbic, you notice spots of blood on what must be a scrap of clothing.
You also notice that the scrap is from """ + suspects[mystery["suspect"]]["sex"] + "'s clothing."
    }

    clue_hair = {
        "detail": "scuff",
        "first look": "There's a SCUFF on the wall, it looks like someone scraped against the wall, carrying something heavy.",
        "closer inspection": """You look more carefully and realise that the mark was clearly form the killer on there way past, dragging the body.
There are drips of blood and you also find a lock of hair, snagged on a nail that the killer must have brushed past on their way.
The hair is clearly """ + suspects[mystery["suspect"]]["hair colour"] + "."
    }

    clue_weapon = {
        "detail": "rug",
        "first look": "There's something vaugley shiny sticking out from under a RUG.",
        "closer inspection": "You peel back teh corner of the rug and find a blood stained " + mystery["weapon"] + """.
The killer must have used this to commit the murder and then hidden it here."""
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
        if current_room in found_clues:
<<<<<<< HEAD
            print(current_room["clue"]["closer inspection"])
            print("\nYou have already added this to your notebook")
=======
            print("\nYou have already inspected " + detail.upper() + " and added clues to your notebook")
>>>>>>> 8386c83771b5cdf8a1542650603c53f52feea960
        else:
            print("\n"+ current_room["clue"]["closer inspection"])
            found_clues.append(current_room)
            print("\nYou've made a note of this in the clues section of your notebook") 
    elif detail in current_room["details"]:
        detail_number = current_room["details"].index(detail)
        print(current_room["red herrings"][list(current_room["red herrings"])[detail_number]])
    else:
        print("You can't inspect that.")

def game_won():
    print("""Congratulations.
Your accusations were correct, and the killer has been brought to justice.""")
    while True:
        restart_game = input("\nWould you like to play again? (Yes/No)\n...")
        if normalise_input(restart_game)==["yes"] or normalise_input(restart_game)==["y"] or normalise_input(restart_game)==["yeah"]:
            new_game()
        elif normalise_input(restart_game)==["no"] or normalise_input(restart_game)==["n"] or normalise_input(restart_game)==["nah"]:
            quit()
        else:
            print("Please answer Yes or No")
            

def game_over():
    print("""Game Over.
The murder of Morebrandt mansion remains unsolved.""")
    while True:
        restart_game = input("\nWould you like to try again? (Yes/No)\n...")
        if normalise_input(restart_game)==["yes"] or normalise_input(restart_game)==["y"] or normalise_input(restart_game)==["yeah"]:
            new_game()
        elif normalise_input(restart_game)==["no"] or normalise_input(restart_game)==["n"] or normalise_input(restart_game)==["nah"]:
            quit()
        else:
            print("Please answer Yes or No")


