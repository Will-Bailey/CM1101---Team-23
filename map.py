room_study = {
 "name": "Study",
 "description": """Study description""",
 "exits": {"east": "Lobby", "secret": "Kitchen"}
}
room_lobby ={
 "name": "Lobby",
 "description": """Lobby description""",
 "exits": {"north": "Conservatory", "east": "Lounge", "northeast": "Dining Room"}
}
room_conservatory = {
 "name": "Conservatory",
 "description": """Conservatory description""",
 "exits": {"south": "Lobby"}
}
room_diningroom = {
 "name": "Dining Room",
 "description": """Dining Room description""",
 "exits": {"southwest": "Lobby", "northeast": "Kitchen"}
}
room_lounge = {
 "name": "Lounge",
 "description": """Lounge description""",
 "exits": {"west": "Lobby", "north" : "Kitchen"}
}
room_kitchen = {
 "name" : "Kitchen",
 "description": """Kitchen description""",
 "exits": {"southwest": "Dining Room", "secret": "Study"}
}

rooms = {
    "Lobby": room_lobby,
    "Study": room_study,
    "Conservatory": room_conservatory,
    "Dining Room": room_diningroom,
    "Lounge": room_lounge,
    "Kitchen": room_kitchen
}
 
