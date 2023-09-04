#Conner Hufnagel

# The dictionary links a room to other rooms.
# dictionary gives rooms 'doors' and 'items'
rooms = {
    'Entry': {'doors': {'east': 'Main Foyer'}},
    'Main Foyer': {'doors': {'west': 'Entry', 'north': 'Staircase', 'east': 'Dining Room'}},
    'Staircase': {'doors': {'south': 'Main Foyer', 'east': 'Basement'}},
    'Basement': {'doors': {'west': 'Staircase', 'east': 'Dungeon'},
                 'items': {'sack next to a pillar': 'Chestplate'}},
    'Dungeon': {'doors': {'west': 'Basement', 'south': "Lair of Toto"},
                'items': {'sword mounted above the south door': 'Sword'}},
    'Dining Room': {'doors': {'west': 'Main Foyer', 'north': 'Kitchen', 'south': 'Hallway'},
                    'items': {'pile of rubble in the corner': 'Helm'}},
    'Kitchen': {'doors': {'south': 'Dining Room'},
                'items': {'number of drawers and cabinets throughout the room': 'Gauntlets'}},
    'Hallway': {'doors': {'north': 'Dining Room', 'east': 'Master Bedroom', 'west': 'Guest Bedroom'},
                'items': {'chest in the center of the hallway': 'Shield'}},
    'Master Bedroom': {'doors': {'west': 'Hallway'}},
    'Guest Bedroom': {'doors': {'east': 'Hallway'},
                      'items': {'closet to your left': 'Greaves'}},
    "Lair of Toto" : {'doors': {'north': 'Dungeon'}}
}
#create status function
def show_status():
    print(f'You are in the {currentRoom}')
    print(f'Inventory: {player_inventory}')
    for key in rooms[currentRoom]['doors']:
        print(f'There is a door to the {key.capitalize()}')
    if 'items' in rooms[currentRoom]:
        for key in rooms[currentRoom]['items']:
            print(f'You see a {key}.')
    print('. . .')

#create list for player inventory
player_inventory = []
#create list for directions for feedback on incorrect direction selections
valid_directions = ['north', 'south', 'east', 'west']

# start player in Entry
currentRoom = 'Entry'
user_command = 'start'

# print a main menu and the commands
#deleted exit command
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -"
      "\nYou have been taken to Toto's Castle by Toto's minions. But they stole your armor and weapon!"
      "\nYou had 5 pieces of armor and a sword. Find your equipment, find Toto's lair, and slay them!"
      "\nCommands: North, South, East, West, Search, Help")

# loop forever
while currentRoom != 'Lair of Toto':
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - -')
    #display player status
    show_status()
    #get player command input
    user_command = input('What should you do?\n')
    user_command = user_command.lower()
    #player can request the command menu again
    if user_command == 'help':
        print("You can enter the following commands: North, South, East, West, Search, Help")
        continue
    #player can search rooms that have strange things in them to find items
    if user_command == 'search' and 'items' in rooms[currentRoom]:
        #when player searches correct room, add item to inventory, remove searcheable object
        for key in rooms[currentRoom]['items']:
            print(f"You find your {rooms[currentRoom]['items'][key]}")
            player_inventory.append(rooms[currentRoom]['items'][key])
            rooms[currentRoom].pop('items')
        continue
    #when player inputs a valid move direction, allow them through the door
    if user_command in rooms[currentRoom]['doors']:
        currentRoom = rooms[currentRoom]['doors'][user_command]
        print(f'You move through the door into the {currentRoom}.')
    else:
        #if the player puts in a direction with no door, tell them to go another direction
        if user_command in valid_directions:
            print("You can't go that way. Try a different direction.")
            continue
        if user_command == 'search':
            print("There's nothing here!")
            continue
        #otherwise, invalid
        else:
            print('Invalid move')
#loop breaks once player enters lair of toto room. program checks win/loss condition
#win condition
if len(player_inventory) == 6:
    print("You enter Toto's lair, armed to the teeth and ready to vanquish your foe."
          "\nToto is defeated."
          "\nCONGRATULATIONS! YOU WIN!")
#loss condition
else:
    print("You enter Toto's lair. But you are ill equipped to fight!"
          "\nYou are slain in battle."
          "\nGAME OVER")