def AISetUp(self):
    
    # Check for best weapon
    if self.CountByCategory("Sword") != 0:
        rank = self.myMap[0][0].rank if self.myMap[0][0].category == "Sword" or 0

        for x, y in range(self.FindBy("Sword", mode="Category")):
            if self.myMap[0][0].rank > rank:
                self.Swap(0,0, x,y)
                rank = self.myMap[0][0].rank
        

    elif self.CountByCategory("Sword") == 0 and self.CountByCategory("Axes") != 0:
        x, y = self.FindBy("Axes", mode="Category")[0]
        self.Swap(0,0,x,y)

    # Select best block
    elif self.myMap[0][1].category != "Block":
        for _ in range(4):
            pass
        min(4, self.CountByStack("Block", mode="Category"))
        if self.CountByStack("Block", mode="Category"):
            pass
    
    # apple_golden
    count = self.CountByName("Apple")
    if count != 0:
        if self.CountByName("Bow") == 0:
            # Make sure >= 1 apple is in myMap[0][2]
            if self.myMap[0][2].name != "Apple":
                x, y = self.FindBy("Apple", mode="Name")[0]
                self.Swap(0,2, x,y)
            # All or 64(the rest in not in control) apple is in myMap[0][2]
            if self.myMap[0][2].number <= min(count, 64):
                self.Combine(0, 2)

    # Possion
    count = self.CountByCategory("Possion")
    if count != 0:
