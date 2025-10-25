#DECLARE myList : ARRAY [0:4] OF STRING 
myList = ["" for index in range(5)]
#myList = ["Minhas", "Ali", "Kiran", "Ayaan", "Esha"]

for i in range(len(myList)): 
    name : str = input("Enter a name: ").upper()
    myList[i] = name

print(myList)

