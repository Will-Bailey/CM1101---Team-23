room_study = {
 "name": "Study",
 "description": """You are now in the study, the lights are off and the blinds are down.""",
 "exits": {"east": "Lobby", "secret": "Kitchen"},
 "red herrings": {
 "The monitor of the computer has been left on, illuminating the desk and it's contents.": "On further inspection Logan Paul's suicide forest video had been left on pause.",
 "A cup of pens have been knocked over.": "You can't investigate this.",
 "A desk drawer has been left open.": "Looking closely you see a pair of pink fluffy handcuffs."
 },
 "details": ["computer", "pens", "drawer"],
 "clue": "",
 "notebook_status": "neutral"

}
room_lobby ={
 "name": "Lobby",
 "description": """You are in the lobby, the suspects await your decision. """,
 "exits": {"north": "Conservatory", "east": "Dining Room", "west": "Study"},
 
 "clue": "",
 "notebook_status": "neutral"
}
room_conservatory = {
 "name": "Conservatory",
 "description": """You are now in the conservatory, you feel a breeze.""",
 "exits": {"south": "Lobby", "east": "Kitchen"},
 "red herrings": {
 "There appears to be blood stains down the window which has been left slightly ajar to your left.": "As you move closer you see a dead rook lying on the patio outside.",
 "A vase in the far right corner has smashed on the ground.": "You suspect the breeze has caused it to fall.",
 "The radio has been left on.": "It hasn't been tuned and is static hum and crackle sound is coming from it."
 },
 "details": ["window", "vase", "radio"],
 "clue": "",
 "notebook_status": "neutral"
}
room_diningroom = {
 "name": "Dining Room",
 "description": """You are now in the dining room.""",
 "exits": {"west": "Lobby", "north": "Kitchen"},
 "red herrings": {
 "You see candles on the window sill.": "As you move you move closer you see some smoke is still rising from them.",
 "Moving towards the candles something catches your eye on the wall.": "Upon further inspection there appears to be 3 deep scratches.",
 "An open box is on the table.": "A game of cluedo has been left out."
 },
 "details": ["candles", "wall", "box"],
 "clue": "",
 "notebook_status": "neutral"
}
room_garage = {
 "name": "Garage",
 "description": """You step into the garage, a strange and pungent smell hits you.""",
 "exits": {"west": "Kitchen"},
 "red herrings": {
 "There is a dent in the bonnet of a 1961 Ferrari 250 GT California SWB Spider": "The dent appears to be the size of a adult male's back and the bottom of the windscreen has a crack in it.",
 "The garage door has been left slightly open.": "Upon further inspection the door has been left open 0.52m high.",
 "A strange smell is coming from the boot of the Ferrari.": "You open the boot and see a dead deer."
 },
 "details": ["bonnet", "door", "smell"],
 "clue": "",
 "notebook_status": "neutral"
}
room_kitchen = {
 "name" : "Kitchen",
 "description": """You have now entered the kitchen, burnt bacon is still in the frying pan.""",
 "exits": {"south": "Dining Room", "secret": "Study", "west": "Conservatory", "east": "Garage"},
 "red herrings": {
 "You see charcoal-crispy burnt bacon in the frying pan.": "As you move closer you can feel the heat coming from the frying pan.",
 "There is a red puddle on the countertop.": "Upon further investigation it smells of Chateau Margaux 1787.",
 "It appears there is a knife missing from the knife block.": "With further investigation you see it has been left on the chopping board."
 },
 "details": ["pan", "countertop", "knife"],
 "clue": "",
 "notebook_status": "neutral"
}

rooms = {
    "Lobby": room_lobby,
    "Study": room_study,
    "Conservatory": room_conservatory,
    "Dining Room": room_diningroom,
    "Garage": room_garage,
    "Kitchen": room_kitchen
}

