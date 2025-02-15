class Circle:
    def __init__(self,r=None):
        self.r  = r
        self.area = None
        self.parameter =None

    def setarea(self):
        self.area = 3.14*self.r*self.r

    def setperimeter (self):
        self.parameter = 2*3.14*self.r

    def getarea(self):
        return self.area
    
    def getperimeter (self):
        return self.parameter

c1 = Circle()
c1.r = int(input("Enter the radius of the circle: "))
c1.setarea()
c1.setperimeter()
print(c1.getarea())
print(c1.getperimeter())  # Output: 113.04 37.68