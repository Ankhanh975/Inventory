import functools
@functools.total_ordering
class Slot:
    sword = ["wood_sword", "stone_sword", "iron_sword", "diamond_sword"]
    axes = ["wood_axe", "iron_axe", "diamond_axe", "gold_axe"]
    pickaxe = ["wood_pickaxe", "iron_pickaxe",
               "diamond_pickaxe", "gold_pickaxe"]
    block = ["red_wool", "blue_wool", "green_wool", "yellow_wool"]

    rank = 1
    enchanted = False
    fullStack = 64

    def __init__(self, name: str = "Air", number: int = 1, enchanted: bool = False):
        self.name = name
        self.number = number
        self.category = name  # TODO
        # self.id = int(0)  # Remove id system since Minecraft 1.10.2(?)
        self.enchanted = enchanted

        # 1 for item don't have category, higher if it has higher value'
        # +0.5 if it's enchanted
        if self.category in ["sword", "axes", "pickaxe"]:
            self.rank = eval(f"{self.category}.index(self.category)")

        elif self.category == "":
            pass

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

    def __eq__(self, other):
        return True