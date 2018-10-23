room_study = {
 "name": "Study",
 "description": """You are now in the study, the lights are off and the blinds are down.""",
 "exits": {"east": "lobby", "secret": "kitchen"},
 "red herrings": {
 "The monitor of the COMPUTER has been left on, illuminating the desk and it's contents.": "On further inspection Logan Paul's suicide forest video had been left on pause.",
 "A cup of PENS have been knocked over.": "A knocked over cup of pens... nothing interesting about this",
 "A desk DRAWER has been left open.": "Looking closely you see a pair of pink fluffy handcuffs."
 },
 "details": ["computer", "pens", "drawer"],
 "clue": "",
 "notebook_status": "neutral"

}
room_lobby ={
 "name": "Lobby",
 "description": """You are in the lobby, the suspects await your decision. """,
 "exits": {"north": "conservatory", "east": "dining room", "west": "study"},
 "details": [],
 "clue": "",
 "notebook_status": "neutral"
}
room_conservatory = {
 "name": "Conservatory",
 "description": """You are now in the conservatory, you feel a rough breeze.""",
 "exits": {"south": "lobby", "east": "kitchen"},
 "red herrings": {
 "There appears to be blood stains down the WINDOW, which has been left slightly ajar to your left.": "As you move closer you see a dead rook lying on the patio outside.",
 "A VASE in the far right corner of the room has smashed onto the ground.": "You suspect the breeze has caused it to fall.",
 "The RADIO has been left on.": "It hasn't been tuned and a static hum and crackle sound is coming from it."
 },
 "details": ["window", "vase", "radio"],
 "clue": "",
 "notebook_status": "neutral"
}
room_diningroom = {
 "name": "Dining Room",
 "description": """You are now in the dining room.""",
 "exits": {"west": "lobby", "north": "kitchen"},
 "red herrings": {
 "You see CANDLES on the window sill.": "As you move you move closer you can see that some smoke is rising from them.",
 "Moving towards the candles something catches your eye on the WALL.": "Upon further inspection there appears to be 3 deep scratches.",
 "An open BOX is on the table.": "A game of cluedo has been left out."
 },
 "details": ["candles", "wall", "box"],
 "clue": "",
 "notebook_status": "neutral"
}
room_garage = {
 "name": "Garage",
 "description": """You step into the garage, a strange and pungent smell hits you.""",
 "exits": {"west": "kitchen"},
 "red herrings": {
 "There is a dent in the BONNET of a 1961 Ferrari 250 GT California SWB Spider": "The dent appears to be the size of a adult human's back and the bottom of the windscreen has a crack in it.",
 "The garage DOOR has been left slightly open.": "Upon further inspection the door has been left open 0.52m high.",
 "A strange SMELL is coming from the boot of the Ferrari.": "You open the boot and see a dead deer."
 },
 "details": ["bonnet", "door", "smell"],
 "clue": "",
 "notebook_status": "neutral"
}
room_kitchen = {
 "name" : "Kitchen",
 "description": """You have now entered the kitchen, burnt bacon is still in the frying pan.""",
 "exits": {"south": "dining room", "secret": "study", "west": "conservatory", "east": "garage"},
 "red herrings": {
 "You see charcoal-crispy burnt bacon in the frying PAN.": "As you move closer you can feel the heat coming from the frying pan.",
 "There is a red puddle on the COUNTERTOP.": "Upon further investigation it smells of Chateau Margaux 1787.",
 "It appears there is a knife missing from the KNIFE block.": "With further investigation you see it has been left on the chopping board."
 },
 "details": ["pan", "countertop", "knife"],
 "clue": "",
 "notebook_status": "neutral"
}

rooms = {
    "lobby": room_lobby,
    "study": room_study,
    "conservatory": room_conservatory,
    "dining room": room_diningroom,
    "garage": room_garage,
    "kitchen": room_kitchen
}

