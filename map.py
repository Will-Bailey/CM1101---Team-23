room_study = {
 "name": "Study",
 "description": """Study description""",
 "exits": {"east": "Lobby", "secret": "Kitchen"},
 "items": []
}
room_lobby ={
 "name": "Lobby",
 "description": """Lobby description""",
 "exits": {"north": "Conservatory", "east": "Lounge", "northeast": "Dining Room"},
 "items": []
}
room_conservatory = {
 "name": "Conservatory",
 "description": """Conservatory description""",
 "exits": {"south": "Lobby"},
 "items": []
}
room_diningroom = {
 "name": "Dining Room",
 "description": """Dining Room description""",
 "exits": {"southwest": "Lobby", "northeast": "Kitchen"},
 "items": []
}
room_lounge = {
 "name": "Lounge",
 "description": """Lounge description""",
 "exits": {"west": "Lobby", "north" : "Kitchen"},
 "items": []
}
room_kitchen = {
 "name" : "Kitchen",
 "description": """Kitchen description""",
 "exits": {"southwest": "Dining Room", "secret": "Study"},
 "items": []
}

rooms = {
    "Lobby": room_lobby,
    "Study": room_study,
    "Conservatory": room_conservatory,
    "Dining Room": room_diningroom,
    "Lounge": room_lounge,
    "Kitchen": room_kitchen
}
 
