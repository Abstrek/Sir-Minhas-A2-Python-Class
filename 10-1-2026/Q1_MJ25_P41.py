#DECLARE Queue : ARRAY[0:19] OF INTEGER
Queue = [-1 for i in range(20)]

#DECLARE HeadPointer, TailPointer, NumberItems : INTEGER
HeadPointer : int = -1
TailPointer : int = -1 
NumberItems : int  = 0

def Enqueue(item : int) -> bool: 
    global HeadPointer, TailPointer, NumberItems, Queue
    if NumberItems == 20: 
        return False

    NumberItems += 1
    
    if TailPointer == -1 and HeadPointer == -1: 
        TailPointer = 0
        HeadPointer = 0
    else: 
        TailPointer += 1

    if TailPointer > 19: 
        TailPointer = 0 

    Queue[TailPointer] = item 

    return True

def Dequeue() -> int: 
    global HeadPointer, TailPointer, NumberItems, Queue

    if NumberItems == 0:
        return -1

    NumberItems -= 1 
    temp : int = Queue[HeadPointer]

    if HeadPointer == TailPointer: 
        HeadPointer = -1
        TailPointer = -1 
    elif HeadPointer == 19:
        HeadPointer = 0 
    else: 
        HeadPointer += 1 

    return temp 

condition : bool = False
for i in range(1, 26): 
    condition = Enqueue(i)
    if condition == True: 
        print(f"{i} Successful")
    else: 
        print(f"{i} Unsuccessful")

for i in range(2):
    x = Dequeue()
    print(x)
