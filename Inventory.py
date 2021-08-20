import getShape
import functools
import win32api
import win32con

allItem = ['apple_golden', 'arrow', 'bow_standby', 'bucket_water',
           'compass', 'diamond', 'diamond_axe', 'diamond_pickaxe',
           'diamond_sword', 'emerald', 'ender_pearl', 'fireball',
           'gold_axe', 'gold_ingot', 'gold_pickaxe', 'iron_axe',
           'iron_ingot', 'iron_pickaxe', 'iron_sword', 'stone_axe',
           'stone_pickaxe', 'stone_sword', 'wood_sword', "wood_axe", "wood_pickaxe",
           "red_wool", "blue_wool", "green_wool", "yellow_wool"]


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


def add2D(this, other):
    out = this.split('\n')
    Z = other.split('\n')

    for x in range(min(len(out), len(Z))):
        out[x] += Z[x] + "\n"

    return ''.join(out)


class Inventory:
    PosOfEachSlot = [[(671, 577), (746, 581), (819, 582), (891, 585), (955, 579), (1039, 581), (1084, 582), (1174, 580), (1241, 575)],   
                    [(676, 634), (741, 639), (815, 644), (908, 636), (964, 638), (1043, 648), (1115, 648), (1174, 648), (1243, 645)],  
                    [(665, 716), (751, 723), (813, 719), (908, 718), (959, 724), (1032, 714), (1108, 724), (1187, 736), (1232, 727)],  
                    [(674, 813), (742, 811), (823, 806), (890, 810), (967, 818), (1029, 823), (1103, 819), (1171, 818), (1236, 815)]] 
    armor = None

    def __init__(self, myMap: list, armor=None):
        if getShape.getShape(myMap) != (4, 9):
            raise ValueError("Not a Minecraft Inventory setup.")
        self.myMap = myMap
        self.armor = armor
        self.history = []

    def Combine(self, x, y):
        # self.history.append(f"combined at {x}, {y}")
        self.history.append(["Combined", x, y])

        # Performs similar like double click on Slot[x][y]
        # Minecraft will check form left-> right, up-> down,
        # and only touch the most up and most left 64 if nothing else to grab

        if self.myMap[x][y].name in ["Air", "None"]:
            return

        name = self.myMap[x][y].name
        # Second run check for slot "64"
        for Condition in [False, True]:
            for i in range(4):
                for j in range(9):
                    # Tacket form left-> right, up-> down
                    if self.myMap[x][y].number == 64:
                        return
                    elif (3-i, j) == (x, y):
                        continue
                    elif self.myMap[3-i][j].name != name:
                        continue
                    else:
                        if self.myMap[3-i][j].number != 64 or Condition:
                            # How many more to fill 64
                            Needed = 64 - self.myMap[x][y].number
                            if self.myMap[3-i][j].number >= Needed:
                                self.myMap[x][y].number += Needed
                                self.myMap[3-i][j].number -= Needed
                            else:
                                self.myMap[x][y].number += self.myMap[3-i][j].number
                                self.myMap[3 -
                                           i][j].number -= self.myMap[3-i][j].number

    def Swap(self, x1, y1, x2, y2):
        # self.history.append(f"Swap {x1}, {y1} with {x2}, {y2}")
        self.history.append(["Swap", x1, y1, x2, y2])
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

    def CountByStack(self, name, mode=['Name', "Category"][0]):
        # How many slots a item/Category take, how many is minimum needed
        def toStack(num: int, fullStack=64):
            if num < 0:
                raise ValueError("Don't support negative numbers")
            # print (f"num: {(num)}, fullStack: {fullStack} and filled in: {(num-1)//fullStack+1} stack")
            return (num-1)//fullStack+1

        mode = mode.lower()
        count = 0
        if mode == "name":
            for x in range(9):
                for y in range(4):
                    if self.myMap[x][y].name == name:
                        count += self.myMap[x][y].number

            count = toStack(count, self.myMap[x][y].fullStack)
        elif mode == "category":
            for x in eval(f"Slot.{name}"):
                count += self.CountByStack(x, "Name")
        return count

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        Table = ""
        for i in (3, 2, 1, 0):

            out = " \n\n\n\n\n\n"
            for j in range(9):
                name = self.myMap[i][j].name
                n = "{:^2}".format(self.myMap[i][j].number)

                if len(name) >= 7 and len(name) <= 18:
                    fName = "{:^9}".format(name[0:len(name)//2])
                    sName = "{:^9}".format(name[len(name)//2:])
                elif len(name) < 7:
                    fName = "{:^9}".format(name)
                    sName = "{:^9}".format("")
                else:
                    name = name[0:18]
                    fName = "{:^9}".format(name[0:len(name)//2])
                    sName = "{:^9}".format(name[len(name)//2:])

                thisCell = f'''\
 ___________ 
|           |
| {fName  } |
| {sName  } |
|           |
|________{n}_|'''
                out = add2D(out, thisCell)

            Table += out
            # print("out:",out)
            # print("thisCell:",thisCell)

        return Table+"\n"

    def perform(self):
        def ClickAt(x: int, y: int):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            getShape.Sleepp(0.005)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        for x in range(self.history):
            if x[0] == "Combined":
                pass
            elif x[0] == "Swap":
            # Similar to LClick Slot[x1][y1] -> LClick Slot[x2][y2] -> LClick Slot[x1][y1]
                ClickAt(self.PosOfEachSlot[x[1]][x[2]]) 
                ClickAt(self.PosOfEachSlot[x[3]][x[4]]) 
                ClickAt(self.PosOfEachSlot[x[1]][x[2]]) 
            

