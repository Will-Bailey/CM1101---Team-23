 room_study = {
 "name": "Study",
 "exits": {"east": "Lobby", "secret": "Kitchen"}

 }
room_lobby ={
 "name": "Lobby",
 "exits": {"north": "Conservatory", "east": "Lounge", "north-east": "Dining Room"}
 }
room_conservatory = {
 "name": "Conservatory",
 "exits": {"south": "Lobby"}
 }
room_diningroom = {
 "name": "Dining Room",
 "exits": {"south-west": "Lobby", "norht-east": "Kitchen"}
 }
room_lounge = {
 "name": "Lounge",
 "exits": {"west": "Lobby", "north" : "Kitchen"}
 }
room_kitchen = {
 "name" : "Kitchen",
 "exits": {"south-west": "Dining Room", "secret": "Study"}
 }

 rooms = {
    "Lobby": room_lobby,
    "Study": room_study,
    "Conservatory": room_conservatory,
    "Dining Room": room_diningroom,
    "Lounge": room_lounge,
    "Kitchen": room_kitchen
}