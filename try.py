x=5

class Test:
    print(x)
    x=x+1
    def __init__(self):
        print(x, self.x)

Test()