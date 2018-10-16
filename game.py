from suspects import *
#from map import * #Awaiting dictionary
#from weapons import * #Awaiting dictionary
import random

def generate_mystery():
    ### This function should randomly generate a dictionary (called "mystery")
    ###that uses the terms "murder_suspect", "murder_weapon" and "murder_room"
    ###as keys and randomly picks a room, suspect and weapon from the respective
    ###dicitonaries and asigns them as values. Once it has done this, the
    ###function should then call the generate_clues function to finish off the
    ###setup.
    mystery = {
        "murder_suspect": random.choice(list(suspects))
        #"murder_weapon": random.choice(list(weapons)) #Awaiting dictionary
        #"murder_room": random.choice(list(room)) #Awaiting dictionary
    }
    generate_clues(mystery)


def generate_clues(mystery):
    ###This function is responsible for generating the correct clues to solve the
    ###mystery given to it and then asigning each of them to a room. There are 5

    clues = {
        "room": """On closer inspection of the room, you notice a splatter of
                      blood on the wall and below it a puddle of yet more blood.
                      clearly this is the room in which the murder took place""",
        "witness": "",
        "clothes" : "",
        "hair": "",
        "weapon": ""
        
        }

    if suspects[mystery[murder_suspect]]["build"] == "tall":
        clues["build"] = """ """ ###A string about interviewing a witness of some kind who claims they saw a sillhouette of the murderer and that they were TALL
    else:
        clues["build"] = """ """ ###A string about interviewing a witness of some kind who claims they saw a sillhouette of the murderer and that they were short

    if suspects[mystery[murder_suspect]]["sex"] == "male":
        clues["clothes"] = """ """ ###A string about finding a scrap of MENS clothing clearly belonging to the murderer
    else:
        clues["clothes"] = """ """ ###A string about finding a scrap of WOMENS clothing clearly belonging to the murderer
        
    if suspects[mystery[murder_suspect]]["hair"] == "blonde":
        clues["hair"] = """ """ ###A string about finding a lock of BLONDE clearly belonging to the murderer
    else:
        clues["hair"] = """ """ ###A string about finding a lock of BLACK clearly belonging to the murderer

    clues["weapon"] = """ """ ###A string about finding the murder weapon using mystery["weapon"]
    clues["room"] = """ """ ###A string about finding a bloodstain in the murder room using mystey["room"]

    for room in rooms:
    	if room[name] =! "lobby"