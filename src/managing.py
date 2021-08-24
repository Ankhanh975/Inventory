def add2D(this, other):
    out = this.split('\n')
    Z = other.split('\n')

    for x in range(min(len(out), len(Z))):
        out[x] += Z[x] + "\n"

    return ''.join(out)
    
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

def ToEnderChest(self, x: int, y: int):
    pass

def Buy(self, item):
    # Trade the item with NPC
    pass

def ToEnderChestAll(self, mode= ["in", "out"][0], seclect=["resource", "throwAble"][0]): 
    if mode == "in":
        pass
    if seclect == "resource":
        pass
    for x in range(3):
        for y in range(9):
            pass