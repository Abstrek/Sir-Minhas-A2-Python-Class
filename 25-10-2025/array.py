#DECLARE myList : ARRAY [0:4] OF STRING 
myList = ["" for index in range(5)] #intializing the array with empty charachters 
# "" = empty characters

for i in range(5): 
    name : str = input("Enter a name: ").upper() #upper function converts all characters into upper-case. 
    myList[i] = name

print(myList)

