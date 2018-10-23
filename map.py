room_study = {
 "name": "Study",
 "description": """Study description""",
 "exits": {"east": "Lobby", "secret": "Kitchen"},
 "red herrings": {
 "Study RH 1": "Inspected Study RH 1",
 "Study RH 2": "Inspected Study RH 2",
 "Study RH 3": "Inspected Study RH 3"
 },
 "details": ["detail1", "detail2", "detail3"],
 "clue": "",
 "notebook_status": "neutral"

}
room_lobby ={
 "name": "Lobby",
 "description": """Lobby description""",
 "exits": {"north": "Conservatory", "east": "Lounge", "northeast": "Dining Room"},
 "red herrings": {
 "Lobby RH 1": "Inspected Lobby RH 1",
 "Lobby RH 2": "Inspected Lobby RH 2",
 "Lobby RH 3": "Inspected Lobby RH 3"
 },
 "details": ["detail1", "detail2", "detail3"],
 "clue": "",
 "notebook_status": "neutral"
}
room_conservatory = {
 "name": "Conservatory",
 "description": """Conservatory description""",
 "exits": {"south": "Lobby"},
 "red herrings": {
 "Conservatory RH 1": "Inspected Conservatory RH 1",
 "Conservatory RH 2": "Inspected Conservatory RH 2",
 "Conservatory RH 3": "Inspected Conservatory RH 3"
 },
 "details": ["detail1", "detail2", "detail3"],
 "clue": "",
 "notebook_status": "neutral"
}
room_diningroom = {
 "name": "Dining Room",
 "description": """Dining Room description""",
 "exits": {"southwest": "Lobby", "northeast": "Kitchen"},
 "red herrings": {
 "Dining room RH 1": "Inspected Dining room RH 1",
 "Dining room RH 2": "Inspected Dining room RH 2",
 "Dining room RH 3": "Inspected Dining room RH 3"
 },
 "details": ["detail1", "detail2", "detail3"],
 "clue": "",
 "notebook_status": "neutral"
}
room_lounge = {
 "name": "Lounge",
 "description": """Lounge description""",
 "exits": {"west": "Lobby", "north" : "Kitchen"},
 "red herrings": {
 "Lounge RH 1": "Inspected Lounge RH 1",
 "Lounge RH 2": "Inspected Lounge RH 2",
 "Lounge RH 3": "Inspected Lounge RH 3"
 },
 "details": ["detail1", "detail2", "detail3"],
 "clue": "",
 "notebook_status": "neutral"
}
room_kitchen = {
 "name" : "Kitchen",
 "description": """Kitchen description""",
 "exits": {"southwest": "Dining Room", "secret": "Study"},
 "red herrings": {
 "Kitchen RH 1": "Inspected Kitchen RH 1",
 "Kitchen RH 2": "Inspected Kitchen RH 2",
 "Kitchen RH 3": "Inspected Kitchen RH 3"
 },
 "details": ["detail1", "detail2", "detail3"],
 "clue": "",
 "notebook_status": "neutral"
}

rooms = {
    "Lobby": room_lobby,
    "Study": room_study,
    "Conservatory": room_conservatory,
    "Dining Room": room_diningroom,
    "Lounge": room_lounge,
    "Kitchen": room_kitchen
}
 
