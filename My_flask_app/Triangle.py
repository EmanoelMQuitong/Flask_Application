class Triangle():
    def __init__(self, base = 1, height = 1):
        self.__base = base      
        self.__height = height  
    

    def getArea(self):
        Area = (1/2)*(self.__base*self.__height)
        return str(Area)

    def setBase(self, base):
        self.__base = base
    
    def setHeight(self, height):
        self.__height = height
