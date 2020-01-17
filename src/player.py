# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room
        self.inv = []
    def __str__(self):
        return f"Player name: {self.player_name}, {self.current_room}"
    def print_inv(self):
        return f"{self.inv}"

    # Add item to player's inventory.
    #def add_inv(self):
        # Add the item to the players inventory.
        #added_item = inv.append(item)
        #print(added_item, "was picked up.")
        #return f"Updated inventory: {self.inv}"
    # Remove item from player's inventory.
    #def rem_inv(self):
        # Remove the item from the player's inventory.
        #removed_item = inv.remove(item)
        #print(removed_item, " was dropped.")
        #return f"Updated inventory: {self.inv}"