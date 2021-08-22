import getShape
from Slot import Slot
import win32api
import win32con
from managing import Swap, Combine, __str__, __repr__
import lib.resource
import AI
allItem = ['apple_golden', 'arrow', 'bow_standby', 'bucket_water',
           'compass', 'diamond', 'diamond_axe', 'diamond_pickaxe',
           'diamond_sword', 'emerald', 'ender_pearl', 'fireball',
           'gold_axe', 'gold_ingot', 'gold_pickaxe', 'iron_axe',
           'iron_ingot', 'iron_pickaxe', 'iron_sword', 'stone_axe',
           'stone_pickaxe', 'stone_sword', 'wood_sword', "wood_axe", "wood_pickaxe",
           "red_wool", "blue_wool", "green_wool", "yellow_wool", "shears"]



class Inventory:
    Combine = Combine
    Swap = Swap
    __str__ = __repr__
    __repr__ = __repr__

    PosOfEachSlot = [[(671, 577), (746, 581), (819, 582), (891, 585), (955, 579), (1039, 581), (1084, 582), (1174, 580), (1241, 575)],
                     [(676, 634), (741, 639), (815, 644), (908, 636), (964, 638),
                      (1043, 648), (1115, 648), (1174, 648), (1243, 645)],
                     [(665, 716), (751, 723), (813, 719), (908, 718), (959, 724),
                      (1032, 714), (1108, 724), (1187, 736), (1232, 727)],
                     [(674, 813), (742, 811), (823, 806), (890, 810), (967, 818), (1029, 823), (1103, 819), (1171, 818), (1236, 815)]]
    armor = None

    def __init__(self, myMap: list, armor=None):
        if getShape.getShape(myMap) != (4, 9):
            raise ValueError("Not a Minecraft Inventory setup.")
        self.myMap = myMap
        self.armor = armor
        self.history = []

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
        mode = mode.lower()

        # return the number of slot a item takes up and the minimum number needed
        def CountMin(name, mode=['Name', "Category"][0]):
            def toStack(num: int, fullStack=64):
                if num < 0:
                    raise ValueError("Don't support negative numbers")

                return (num-1)//fullStack+1

            count = 0
            if mode == "name":
                for x in range(9):
                    for y in range(4):
                        if self.myMap[x][y].name == name:
                            count += self.myMap[x][y].number

                count = toStack(count, self.myMap[x][y].fullStack)
            elif mode == "category":
                for x in eval(f"Slot.{name}"):
                    count += CountMin(x, "name")
            return count
        slotTake = 0
        for x in range(9):
            for y in range(4):
                if eval(f"self.myMap[x][y].{mode}") == name:
                    slotTake += 1
        return slotTake, CountMin(name, mode)

    def FindBy(self, name, mode=['Name', "Category"][1]):
        # Find all slots coordinates a item lies 
        mode = mode.lower()
        Z=[]
        for x in range(9):
            for y in range(4):
                if eval(f"self.myMap[x][y].{mode}") == name:
                    Z.append((x, y))
        return Z
    Gather = AI.Gather
    AISetUp = AI.AISetUp
    def perform(self):
        # After all calculation perform that to Minecraft base on calculation history
        def ClickAt(x: int, y: int):
            x, y = self.PosOfEachSlot[x][y]
            win32api.SetCursorPos((x, y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            getShape.Sleepp(0.005)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        lib.resorce.pressAndHold(key)
        lib.resorce.release(key)

        for x in range(self.history):
            if x[0] == "Combined":
                for _ in range(3):
                    ClickAt(x[1], x[2])
            # Optimize movement if swap with a slot have x=0
            elif x[0] == "Swap":
                if x[1] == 0:
                    Press("Ctrl")

                ClickAt(x[1], x[2])
                ClickAt(x[3], x[4])
                ClickAt(x[1], x[2])
            elif x[0] == "Ctrl+Click":
                pass
