mylist : int = [[-1, 0, i+1] for i in range(10)]
mylist[9][2] = -1 

free_pointer = 0
root_pointer = -1

def insert(item : int) -> bool:
    global mylist, free_pointer, root_pointer
    if free_pointer == -1: 
        print("Tree full")
        return False 
    else: 
        temp : int = free_pointer 
        free_pointer = mylist[free_pointer][2] 
        mylist[temp][1] = item
        mylist[temp][2] = -1 
        if root_pointer == -1: 
            root_pointer = temp
            return True 
        else:  
            current_pointer = root_pointer
            turn_right : bool = False 
            while current_pointer != -1: 
                previous_pointer : int = current_pointer
                if mylist[current_pointer][1] < item: 
                     turn_right = True
                     current_pointer = mylist[current_pointer][2]
                else: 
                    turn_right = False
                    current_pointer = mylist[current_pointer][0]

            if turn_right == True: 
                mylist[previous_pointer][2] = temp
                return True 
            else: 
                mylist[previous_pointer][0] = temp 
                return True

def search(item : int) -> bool: 
    global mylist, free_pointer, root_pointer 
    if root_pointer == -1: 
        return False 
    else: 
        current_pointer = root_pointer 
        while current_pointer != -1:
            if mylist[current_pointer][1] == item: 
                print(current_pointer)
                return True
            else: 
                if mylist[current_pointer][1] < item: 
                    current_pointer = mylist[current_pointer][2]
                else:
                    current_pointer = mylist[current_pointer][0]

        return False
                     
    
                 
for i in range(20):
    item = int(input("Enter data: "))
    AddNode(item)

def InOrder(Root):
    if ArrayNodes[Root][0] != -1: 
        PostOrder(ArrayNodes[Root][0])
   
   print(ArrayNodes[Root][1])

    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])
    
   