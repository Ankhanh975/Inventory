def Gather(self, name, x, y):
    # Gather all or 64 of {name} to slot at[x][y]
    count = self.CountByName(name)
    if count != 0:
        # Make sure >= 1 apple is in self.myMap[x][y]
        if self.myMap[x][y].name != name:
            i, j = self.FindBy(name, mode="Name")[0]
            self.Swap(x,y, i, j)
        if self.myMap[x][y].number <= min(count, self.myMap[x][y].fullstack):
            self.Combine(x, y)

def AISetUp(self):
    HaveBow = self.CountByName("Bow") == 0
    # Check for best weapon
    if self.CountByCategory("Sword") != 0:
        rank = self.myMap[0][0].rank if self.myMap[0][0].category == "Sword" else 0

        for x, y in range(self.FindBy("Sword", mode="Category")):
            if self.myMap[0][0].rank > rank:
                self.Swap(0,0, x,y)
                rank = self.myMap[0][0].rank
        
    elif self.CountByCategory("Sword") == 0 and self.CountByCategory("Axes") != 0:
        x, y = self.FindBy("Axes", mode="Category")[0]
        self.Swap(0,0,x,y)

    
    
    # apple_golden
    count = self.CountByName("Apple")
    if not HaveBow:
        self.Gather("Apple", 0, 2)
    else:
        self.Gather("Apple", 0, 3)

    # Check for bow possion 
    if HaveBow and self.myMap[0][2].name != "Bow":
        self.Swap(0, 2, self.FindBy("Bow", mode="Name")[0])

    # Select best block
    if self.myMap[0][1].category != "Block" and self.myMap[0][1].number != 64:
        self.CountByName("red_wool")
        self.CountByName("blue_wool")
        self.CountByName("green_wool")
        self.CountByName("yellow_wool")
        self.Gather("Block", 0, 1)
        All = self.FindBy("Block", mode="Category")
        for x, y in All:
            pass
        self.CountByStack("Block", mode="Category")
        for _ in range(4):
            pass
        min(4, self.CountByStack("Block", mode="Category"))
        if self.CountByStack("Block", mode="Category"):
            pass

    # Possion
    if self.myMap[0][7].category != "Possion":
        for _ in range(4):
            pass
        min(4, self.CountByStack("Possion", mode="Category"))
        if self.CountByStack("Possion", mode="Category"):
            pass
