from src import Inventory
import random
from src import Slot
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
def readMap(jpg):
    pass
if __name__ == '__main__':
    x=Slot.Slot()
    print("From main", Slot.Slot.__dict__)
    print("From main", x)
    print("From main", x.__dict__)
    print(x.name)
    print(x.Try())
# if __name__ == '__main__':
#     inputMap=[[0, 0, 0, 0, 0, 0, 0, 0, 0], 
#             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#     for i in range(4):
#         for j in range(9):
#             inputMap[i][j] = Inventory.Slot("Air", 1)
#     inputMap[0][0] = Inventory.Slot("Block", 32)
#     inputMap[0][1] = Inventory.Slot("Block", 16)
#     inputMap[0][2] = Inventory.Slot("Block", 16)
#     inputMap[0][3] = Inventory.Slot("Block", 16)
#     inputMap[0][4] = Inventory.Slot("Block", 32)
#     inventory = Inventory.Inventory(inputMap)
#     print ("Before\n", inventory)
#     inventory.Combine(0,1)
#     print ("After\n", inventory)
#     print(eval(f"Inventory.Slot.sword"))