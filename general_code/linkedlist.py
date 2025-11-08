#myList : int = [[0, i+1] for i in range (10)]
#myList[9][1] = -1 
myList = [
    [42,  4],   # index 0
    [5,   5],   # index 1
    [18,  9],   # index 2
    [90, -1],   # index 3 (last node)
    [30,  7],   # index 4
    [7,   6],   # index 5
    [10,  2],   # index 6
    [50,  8],   # index 7
    [75,  3],   # index 8
    [20,  4],   # index 9
]
print(myList)

free_pointer : int = -1
start_pointer : int = 1

def insert(item : int): 
    global free_pointer, start_pointer, myList
    if free_pointer == -1: 
        print("Cannot insert. The List is full.")    
        return False
    else:
        temp : int = free_pointer 
        free_pointer = myList[free_pointer][1]
        myList[temp][0] = item
        positioned : bool = False 
        pointer : int = start_pointer 
        previous_pointer : int = -1
        while positioned == False and pointer != -1: 
            if item < myList[pointer][0]: 
                positioned = True
            else:
                previous_pointer = pointer 
                pointer = myList[pointer][1] 

        if previous_pointer == -1 : 
            start_pointer = temp 
        else: 
            myList[previous_pointer][1] = temp 
        myList[temp][1] = pointer
        myList[temp][0] = item
        
    print(f"start_pointer: {start_pointer}\nfree_pointer: {free_pointer}")
    print(myList)
    print("-------------------------------------------------------------------------------------------------------------------------")
    return True

def delete(item : int): 
    global start_pointer, myList, free_pointer
    found = False
    previous_pointer = -1 
    pointer = start_pointer 
    if start_pointer == -1: 
        print("The list is empty :(")
        return False
    else: 
        while found == False and pointer != -1: 
            if item == myList[pointer][0]: 
                found = True
            else: 
                previous_pointer = pointer 
                pointer = myList[pointer][1]

        if pointer == start_pointer:
            start_pointer = myList[pointer][1]
        elif pointer == -1:
            print("Item not found") 
            return False 
        else: 
            myList[previous_pointer][1] = myList[pointer][1]

        myList[pointer][0] = 0 
        myList[pointer][1] = free_pointer
        free_pointer = pointer
 
            
     
item : int = int(input("enter some shit: "))
hello : bool = delete(item)
print(myList)
print(f"free_pointer: {free_pointer}, start_pointer: {start_pointer}")
 
            
        
