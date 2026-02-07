class Balloon:
    #PRIVATE Health : INTEGER
    #PRIVATE Colour : STRING 
    #PRIVATE DefenseItem : STRING

    def __init__(self, col, defense_item):
        self.__Health = 100
        self.__Colour = col
        self.__DefenseItem = defense_item

    def GetDefenseItem(self):
        return self.__DefenseItem
    
    def ChangeHealth(self, val):
        self.__Health = self.__Health + val

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else: 
            return False

defense_item = input("Enter a defense item: ")
col = input("Enter colour of the balloon: ") 
Balloon1 = Balloon(col, defense_item)

def Defend(balloon : Balloon):
    opponent_strength = int(input("Enter opponent's strength: "))
    balloon.ChangeHealth(opponent_strength * -1)
    
    print("Defense item of the balloon is: ", balloon.GetDefenseItem())

    check = balloon.CheckHealth()

    if check == True: 
        print("Balloon has no health remaining.")
    else:
        print("Balloon is alive and has health remaining")
    
    return balloon

Balloon1 = Defend(Balloon1)