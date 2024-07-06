from player import Player
from scenes import Scene

class Game:
    def __init__(self):
        self.player = Player("Hero")
        self.current_scene = Scene("Starting Point")
    
    def start(self):
        print(f"Welcome to the game, {self.player.name}!")
        self.main_loop()
    
    def main_loop(self):
        while True:
            print(f"You are at {self.current_scene.name}.")
            action = input("What do you want to do? ")
            if action.lower() in ['quit', 'exit']:
                print("Thank you for playing!")
                break
            else:
                print(f"You chose to {action}.")
                # 根据玩家输入执行相应的动作

