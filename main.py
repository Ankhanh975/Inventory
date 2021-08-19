import functools
import getShape
# Hệ tọa độ:
Prefer = {
    1: "Sword",
    2: "Block",
    3: "Apple",
    4: "Fire Ball",
    5: "Iron Golem",
}
Prefer = {
    1: "Sword",
    2: "Block",
    3: "Bow",
    4: "Apple",
    5: "Fire Ball",
    6: "Iron Golem",
    7: "Possion",
}


@functools.total_ordering
class Slot:
    sword = ["wood_sword", "stone_sword", "iron_sword", "diamond_sword"]
    axes = ["wood_axe", "iron_axe", "diamond_axe", "gold_axe"]
    pickaxe = ["wood_pickaxe", "iron_pickaxe",
               "diamond_pickaxe", "gold_pickaxe"]
    block = ["red_wool", "blue_wool", "green_wool", "yellow_wool"]

    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
        self.category = "Block"  # TODO
        self.id = int(None)  # Remove id system since Minecraft 1.10.2(?)
        self.enchanted = False
        self.rank = 1
        # 1 for item don't have category, higher if it has higher value'
        # +0.5 if it's enchanted
        if self.category in ["Sword", "axes", "pickaxe"]:
            self.rank = eval(f"{self.category}.index(self.name)")

        elif self.category == "":
            pass

    def __lt__(self, other):
        # True if self > other, False if self <= other
        if self.category == other.category:
            category = self.category
            if category == "Block":
                return True if self.number > other.number else False
            elif self.category in ["Sword", "axes", "pickaxe"]:
                return True if self.rank > other.rank else False

    def __eq(self, other):
        return True


inputMap = [Slot("None", 1) for x in range(9)]
inputMap = [inputMap for y in range(4)]


class Inventory:
    armor = None

    def __init__(self, myMap: list):
        self.myMap = myMap
        if getShape.getShape(myMap) != (4, 9):
            raise ValueError("Not a Minecraft Inventory setup.")

    def Combine(self, x, y):
        # Performs similar like double click on Slot[x][y]
        # Minecraft will check form left-> right, up-> down,
        # and only touch the most up and most left 64 if nothing else to grab

        if self.myMap[x][y].name == "Air":
            return

        name = self.myMap[x][y].name
        # Second run check for slot "64"
        for Condition in [True, False]:
            for i in range(4):
                for j in range(9):
                    # Tacket form left-> right, up-> down
                    if self.myMap[x][y].number == 64:
                        return
                    elif (i, j) == (x, y):
                        continue
                    elif self.myMap[3-i][j].name != name:
                        continue
                    else:
                        if self.myMap[3-i][j].number != 64:
                            # How many more to fill 64
                            Needed = 64 - self.myMap[x][y].number
                            if self.myMap[3-i][j].number >= Needed:
                                self.myMap[3-i][j].number -= Needed
                                self.myMap[x][y].number += Needed
                            else:
                                self.myMap[3-i][j].number -= self.myMap[3-i][j].number
                                self.myMap[x][y].number += self.myMap[3-i][j].number

    def Swap(self, x1, y1, x2, y2):
        # Similar to LClick Slot[x1][y1] -> LClick Slot[x2][y2] -> LClick Slot[x1][y1]
        # Swap 2 slot

        template = self.myMap[x1][y1]
        self.myMap[x1][y1] = self.myMap[x2][y2]
        self.myMap[x2][y2] = template

    def CountByCategory(self, Category):
        count = 0
        for x in range(9):
            for y in range(4):
                if self.myMap[x][y].Category == Category:
                    count += self.myMap[x][y].number
        return count

    def CountByName(self, name):
        count = 0
        for x in range(9):
            for y in range(4):
                if self.myMap[x][y].name == name:
                    count += self.myMap[x][y].number
        return count

    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        for i in range(4):
            for j in range(9):
                name = self.myMap[i][j].name
                n = self.myMap[i][j].number

                if len(name) >= 7 and len(name) <= 18:
                    fName = "{:^9}".format(name[0:len(name)//2])
                    sName = "{:^9}".format(name[len(name)//2: ])
                elif len(name) < 7:
                    fName = "{:^9}".format(name)
                    sName = "{:^9}".format("")
                else:
                    name = name[0:18]
                    fName = "{:^9}".format(name[0:len(name)//2])
                    sName = "{:^9}".format(name[len(name)//2: ])

                out=f''' ___________ \n 
                        |           |\n
                        | {fName  } |\n
                        | {sName  } |\n
                        |           |\n
                        |________{n}_|\n'''
            

        return out

outputMap = inputMap

for x in range(9):
    for y in range(4):
        if inputMap[x][y].type == "Block":
            outputMap
