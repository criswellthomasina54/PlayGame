class Scene:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def __str__(self):
        return f"{self.name}: {self.description}\nItems: {', '.join([item.name for item in self.items])}"
