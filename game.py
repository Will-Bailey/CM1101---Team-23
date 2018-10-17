from suspects import *
#from map import * #Awaiting dictionary
#from weapons import * #Awaiting dictionary
import random

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
    ###mystery given to it and then asigning each of them to a room. There are 5

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
