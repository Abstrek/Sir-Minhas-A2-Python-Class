class Character: 
    #PRIVATE Name : STRING
    #PRIVATE XPosition : INTEGER
    #PRIVATE YPosition : INTEGER 

    def __init__(self, N, XP, YP):
        self.__Name = N
        self.__XPosition = XP
        self.__YPosition = YP

    def GetXPosition(self):
        return self.__XPosition 

    def GetYPosition(self):
        return self.__YPosition
    
    def SetXPosition(self, val):
        NewPos = self.__XPosition + val
        if NewPos >= 10000:
            self.__XPosition = 10000
        elif NewPos <= 0: 
            self.__XPosition = 0
        else:
            self.__XPosition = NewPos
    
    def SetYPosition(self, val):
        NewPos = self.__YPosition + val
        if NewPos >= 10000:
            self.__YPosition = 10000
        elif NewPos <= 0: 
            self.__YPosition = 0
        else:
            self.__YPosition = NewPos
    
    def Move(self, val):
        if val == "up":
            self.SetYPosition(10)
        elif val == "down":
            self.SetYPosition(-10)
        elif val == "right":
            self.SetXPosition(10)
        elif val == "left":
            self.SetXPosition(-10)
        else:
            print("Invalid direction input")

Jack = Character("Jack", 50, 50)

class BikeCharacters(Character):
    def __init__(self, N, XP, YP):
        super().__init__(N, XP, YP)
    
    def Move(self, val):
        if val == "up":
            super().SetYPosition(20)
        elif val == "down":
            self.SetYPosition(-20)
        elif val == "right":
            self.SetXPosition(20)
        elif val == "left":
            self.SetXPosition(-20)
        else:
            print("Invalid direction input")

Karla = BikeCharacters("Karla", 100, 50)

Cchoice = input("Please enter which character would you like to move: ").strip().lower()
Dchoice = input("In which direction would you like to move said character: ").lower()

if Cchoice == "jack":
    Jack.Move(Dchoice)              
    print("Jack's new position is X = ", Jack.GetXPosition(), " Y = ", Jack.GetYPosition())
elif Cchoice == "karla":
    Karla.Move(Dchoice)
    print("Karla's new position is X = ", Karla.GetXPosition(), " Y = ", Karla.GetYPosition())
else:
    print("Invalid character option.")