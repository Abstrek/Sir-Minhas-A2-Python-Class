#DECLARE myList : ARRAY [0:4] OF STRING 
myList : str = ["Minhas", "Ali", "Kiran", "Ayaan", "Esha"]

def linearSearch(name : str) -> int:
    global myList
    i : int = 0
    while i < 5: 
        if name == myList[i]: 
            return i
        else:
            i += 1

    return -1
        
name : str = input("Enter name: ")
x : int = linearSearch(name)

if x == -1: 
    print(f"{name} not found")
else: 
    print(f"{name} found at position {x}")


    
