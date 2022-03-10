class Restangle():
    def __init__(self,l,w):
        self.lenght = l
        self.width = w

    def restangle_area(self):
        return self.lenght * self.width

newRestangle = Restangle(5,10)
print(newRestangle.restangle_area())
