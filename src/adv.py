from room import Room
from player import Player
from item import Item

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

# Declare all the items.

items = { "frog": Item("Frog", "I'm cooler than I look."),
"goat": Item("Goat", "I bring good luck."),
"hippo": Item("Hippo", "I'm a lot of fun to be around."),
}

# Define valid directions for the game.

valid_directions = ["n", "e", "s", "w"]

# Started with room_mover function to move.

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

# Now use move function to move.

def move(input):
    if input == "n":
        if new_player.current_room.n_to != None:
            new_player.current_room = new_player.current_room.n_to
        else:
            print('Unable to move North from here.')
            print("----------------------------------------------------------------------")

    elif input == "s":
        if new_player.current_room.s_to != None:
            new_player.current_room = new_player.current_room.s_to
        else:
            print('Unable to move South from here.')
            print("----------------------------------------------------------------------")

    elif input == "e":
        if new_player.current_room.e_to != None:
            new_player.current_room = new_player.current_room.e_to
        else:
            print('Unable to move East from here.')
            print("----------------------------------------------------------------------")
    
    elif input == "w":
        if new_player.current_room.w_to != None:
            new_player.current_room = new_player.current_room.w_to
        else:
            print('Unable to move West from here.')
            print("----------------------------------------------------------------------") 

#
# MAIN
#

# Welcome and define player's name.
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

player_name = input("Welcome to the adventure! What is your name?: ")

print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

# Make a new player object that is currently in the 'outside' room.

new_player = Player(player_name, room['outside'])

# Put all items outside to begin.

for item in items:
    new_player.current_room.items.append(item)

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

    # Print the items for the player that are visible in that room.
    # What items are in the current room?

    print("What items are in this room?\n")
    if new_player.current_room.items == []:
        print("There are no items in this room.")
        print("----------------------------------------------------------------------")
    else:
        print(new_player.current_room.print_items())
        print("----------------------------------------------------------------------")
    
    print("What items do you have?\n")
    if new_player.inv == []:
        print("Currently, you don't have any items.")
        print("----------------------------------------------------------------------")
    else:
        print(new_player.print_inv())
        print("----------------------------------------------------------------------")

    action = input("Do you want to take items, drop items or do nothing?\n(Please enter take, drop or nothing.): ")
    print("----------------------------------------------------------------------")
    # Get user input into most normalized format by converting to all 
    # lowercase and stripping white space.
    action = action.lower().strip()

    if action == "take":
        # Check if there are items to take first.
        if new_player.current_room.items == []:
            print("There aren't any items to take.")
            print("----------------------------------------------------------------------")
        else:
            take_item = input("What item would you like to take?: ")
            # Note for refactoring...Could this be turned into a function?
            
            # Normalize user entry.
            take_item = take_item.lower().strip()
            
            # See if item is in the current room.
            if take_item in new_player.current_room.items:
                # Add item to player invenotry.
                new_player.inv.append(take_item)
                print(take_item, " was added to your inventory.")
                print("----------------------------------------------------------------------")                    
                # Remove item from the room.
                new_player.current_room.items.remove(take_item)
            else:
                print("Unable to perform action.")
                print("----------------------------------------------------------------------")

    elif action == "drop":
        # Check if player has any items to drop.
        if new_player.inv == []:
            print("You don't have any items to drop.")
            print("----------------------------------------------------------------------")
        else:
            drop_item = input("What item would you like to drop?: ")
            print("----------------------------------------------------------------------")
            # Note for refactoring...Could this be turned into a function?
            
            # Normalize user entry.
            drop_item = take_item.lower().strip()
            
            # See if item is in the current room.
            if drop_item in new_player.inv:
                # Remove from player inventory.
                new_player.inv.remove(drop_item)
                print(drop_item, " was removed from your inventory.")
                print("----------------------------------------------------------------------")
                # Add item to the room.
                new_player.current_room.items.append(drop_item)
            else:
                print("Unable to perform action.")
                print("----------------------------------------------------------------------")
    
    elif action == "nothing":
        print("Okay, let's keep moving.")
        print("----------------------------------------------------------------------")
    
    else:
        print("You've entered an invalid command.")
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
        move(where_to)

    # If the user enters "q", quit the game.    
    elif where_to == "q":  
        break

    # If the move can't be made, return an error message.    
    else:
        print("That's an invalid entry. Please try again.")
        print("----------------------------------------------------------------------")
        print("----------------------------------------------------------------------")