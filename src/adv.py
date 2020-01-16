from room import Room
from player import Player

# Declare all the rooms.

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link the rooms together.

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Define valid directions for the game.

valid_directions = ["n", "e", "s", "w"]

# Helper function

def room_mover(input):
    if where_to == "n":
        if new_player.current_room.name == "Outside Cave Entrance":
            new_player.current_room = room['foyer']
        elif new_player.current_room.name == "Foyer":
            new_player.current_room = room['overlook']
        elif new_player.current_room.name == "Narrow Passage":
            new_player.current_room = room['treasure']
        else:
            print("Unable to go North from here.")
            print("----------------------------------------------------------------------")
            print("----------------------------------------------------------------------")
    
    elif where_to == "e":
        if new_player.current_room.name == "Foyer":
            new_player.current_room = room['narrow']
        else:
            print("Unable to go East from here.")
            print("----------------------------------------------------------------------")
            print("----------------------------------------------------------------------")

    elif where_to == "s":
        if new_player.current_room.name == "Foyer":
            new_player.current_room = room['outside']
        elif new_player.current_room.name == "Grand Overlook":
            new_player.current_room = room['foyer']
        elif new_player.current_room.name == "Treasure Chamber":
            new_player.current_room = room['narrow']
        else:
            print("Unable to go South from here.")
            print("----------------------------------------------------------------------")
            print("----------------------------------------------------------------------")

    elif where_to == "w":
        if new_player.current_room.name == "Narrow Passage":
            new_player.current_room = room['foyer']
        else:
            print("Unable to go West from here.")
            print("----------------------------------------------------------------------")
            print("----------------------------------------------------------------------")

# Welcome and define player's name.
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

player_name = input("Welcome to the adventure! What is your name?: ")

print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

# Make a new player object that is currently in the 'outside' room.

new_player = Player(player_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    # Print the new player's current room name.

    print(f"You are currently at {new_player.current_room.name}.")

    # Print the new player's current room description.

    print(f"About: {new_player.current_room.description}")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    
    # Ask the player what direction they would like to go using input.

    where_to = input("""What direction would you like to go?
    (Note: Please enter n, e, s or w. You can also enter q to quit the game.): """)
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    
    # Use the user's input to determine if it's a valid move.
    # Define all of the valid inputs and use to compare to user's input.
    # If valid input, change the player's location based on the room they are in.
    # If not a valid input, return an error message to the user.
    
    # Check that input is a valid direction.
    if where_to in valid_directions:
        room_mover(where_to)

    # If the user enters "q", quit the game.    
    elif where_to == "q":  
        break

    # If the move can't be made, return an error message.    
    else:
        print("That's an invalid entry. Please try again.")