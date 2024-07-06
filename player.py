class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def __str__(self):
        return f"{self.name} with inventory: {', '.join(self.inventory)}"
