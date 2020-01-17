# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
    def __str__(self):
        return f"Location: {self.name}, About: {self.description}"
    def print_items(self):
        return f"Items: {self.items}"
    
    # Remove item from room.
    #def rem_item(self):
        #rem_item = items.remove(item)
        #print(rem_item, " was removed.")
        #return f"{self.items}"
    # Add item to room.
    #def add_item(self):
        #a_item = items.append(item)
        #print(a_item, " was added." )
        #return f"{self.items}"            