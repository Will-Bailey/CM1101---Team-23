from suspects import *
#from map import * #Awaiting dictionary
#from weapons import * #Awaiting dictionary
import random

def main():

    #Intro
    print("""
            Game Title

            Intro.....

            """)

    player_name = input("Enter your name: ")

    while True:

        try:
            
            player_age = int(input("How old are you? "))

            if player_age < 0 or player_age > 100:
                print("Please enter age between 1-100")
                continue

            elif player_age >= 13:
                #Welcome
                print("\nWelcome " + player_name +",")
                print("blah blah blah")

            else:
                print("You are too young to play this game!")
                quit()
            break
        
        except ValueError:
            print("You did not enter a valid number.")
                  
    current_room = rooms["Lobby"]


    display_room(current_room)

    while True:

        command = menu(current_room["exits"], current_room["items"], inventory)

        execute_command(command)

        #Victory condition
        if whatever:
            print("Congratulations")
            break
        #Game over
        elif life == 0:
            print("Game over")
            break

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
        if room[name] != "lobby" and room[clue] = "":
            room[clue] = clues[random.choice(list(clues)[1:])]

def menu(exits, room_items, inv_items):

    print_menu(exits, room_items, inv_items)

    user_command = input("...")

    input_normalised = normalise_input(user_command)

    return input_normalised

def print_menu(exits, room_items, inv_items):


    print("You can:")
    
    for direction in exits:
        print_exit(direction, destination(exits, direction))

    for items in room_items:
        print("\nTAKE" + items["id"].upper() + " to add " + items["name"] + " in your inventory.")
        print("CHECK" + items["id"].upper() + " to inspect " + items["name"] + ".")

    for items in inv_items:
        print("\nUSE" + items["id"].upper + " to use " + items["name"] + ".")

    print("\nSTATUS to check your stats.")

    print("\nWhat is your command?")

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

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])            
        else:
            print("Use what?")

    elif command[0] == "status":
        if len(command) > 1:
            execute_status(command[1])

    elif command[0] == "talk to":
        if len(command) > 1:
            execute_talk_to(command[1])

    else:
        print("This makes no sense.")

def execute_go(direction):
    
    display_room(current_room)
           
def execute_take(item_id):

def execute_drop(item_id):

def execute_check(item_id):

def execute_use(item_id):

def execute_talk_to(suspect):

def execute_status():

def display_room(room):

    print("\n" + room["name"].upper() + "\n\n" + room["description"] + "\n")

def print_room_items(room):

    if room["items"] != []:
        print("There is " + items_list(room["items"]) + " here.\n")

def show_present_person(suspect):

    if room["suspects"] != []:
        print(list_of_suspects(room["suspects"]) + " is in the room.")
        
def print_inventory_items(items):

    if items == []:
        print("You inventory is empty")
    else:
        print("You have " + items_list(items) + ".\n")

def items_list(items):

    lists = []

    for item in items:
        lists.append(item.get("name"))

    return ", ".join(lists)
              
if __name__ == "__main__":
    
    main()