# from ...Inventory.lib.LoadData import LoadYaml

# data = LoadYaml("C:/Users/Dell/Desktop/C++/Inventory/data.yaml")["data"]
# print(data)

from dataclasses import dataclass, field

@dataclass()
class Person:
    x: int
    y: int=5
    
a = Person(1,2)
print(a, a.x, a.y)
d