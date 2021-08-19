import Inventory
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

if __name__ == '__main__':
    inputMap = [Inventory.Slot("Block", x+5) for x in range(9)]
    inputMap = [inputMap for y in range(4)]

    inputMap = Inventory.Inventory(inputMap)
    print (inputMap)
    inputMap.Combine(1,1)
    print (inputMap)