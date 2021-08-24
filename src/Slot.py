import functools
@functools.total_ordering
class Slot:
    sword = ["wood_sword", "stone_sword", "iron_sword", "diamond_sword"]
    axes = ["wood_axe", "iron_axe", "diamond_axe", "gold_axe"]
    pickaxe = ["wood_pickaxe", "iron_pickaxe", "gold_pickaxe", "diamond_pickaxe"]
    block = ["red_wool", "blue_wool", "green_wool", "yellow_wool"]
    resource = ["iron_ingot", "gold_ingot", "diamond", "emerald"]
    possion = ["Speed", "Jump", "Invisible"]
    tools = ["shears"]
    tools += sword + axes + pickaxe 

    rank = 1 # Design for compare slot of same category
    enchanted = False
    fullStack = 64

    def __init__(self, name: str = "Air", number: int = 1, enchanted: bool = False):
        self.name = name
        self.number = number
        
        # self.id = int(0)  # Remove id system since Minecraft 1.10.2(?)
        self.enchanted = enchanted
        self.SetRank()
        self.SetCategory()


        if self.category in ["sword", "axes", "pickaxe"]:
            self.fullStack = 1


    
    def __lt__(self, other):
        # True if self > other, False if self <= other
        if self.category == other.category:
            category = self.category
            if category == "Block":
                return True if self.number > other.number else False
            elif self.category in ["Sword", "axes", "pickaxe"]:
                return True if self.rank > other.rank else False

    def Load(self):
        pass
    def __eq__(self, other):
        return True
        
# def SetCategory(self):
#     self.category = name  # TODO
#     for x in (
#         "sword", 
#         "axes", 
#         "pickaxe", 
#         "block", 
#         "resource", 
#         "possion",):
#         if self.name in eval(f"self.{x}"):
#             self.category = x
#             return
#     self.category = "None"

# def SetRank(self):
#     # 1 for item don't have category, higher if it has higher value'
#     # +0.5 if it's enchanted
#     # For sword this number is damage


#     if self.category in ["sword", "axes", "pickaxe"]:
#         self.rank = eval(f"{self.category}.index(self.category)")

#     elif self.category == "":
#         pass

#     if self.enchanted:
#         self.rank += 0.5