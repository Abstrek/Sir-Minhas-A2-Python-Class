class node: 
    def __init__(self): 
        self.data = -1
        self.nextNode = -1

#DECLARE linkedList : ARRAY[0:9] OF node
linkedList = [node() for i in range(10)]

linkedList[0].data = 1
linkedList[0].nextNode = 1
linkedList[1].data = 5
linkedList[1].nextNode = 4
linkedList[2].data = 6
linkedList[2].nextNode = 7
linkedList[3].data = 7
linkedList[3].nextNode = -1
linkedList[4].data = 2
linkedList[4].nextNode = 2
linkedList[5].data = 0
linkedList[5].nextNode = 6
linkedList[6].data = 0
linkedList[6].nextNode = 8
linkedList[7].data = 56
linkedList[7].nextNode = 3
linkedList[8].data = 0
linkedList[8].nextNode = 9
linkedList[9].data = 0
linkedList[9].nextNode = -1


#DECLARE startPointer, emptyList : INTEGER
startPointer = 0
emptyList = 5 

def outputNodes(myList, myPointer): 
    Pointer = myPointer
    while Pointer != -1: 
        print("Data at index", Pointer, "is:", myList[Pointer].data)
        Pointer = myList[Pointer].nextNode

outputNodes(linkedList, startPointer)

def addNode(linkedList, startPointer, emptyList):
    if emptyList == -1: 
        return False 
    
    value = int(input("Enter data: "))
    linkedList[emptyList].data = value
    temp = emptyList

    if emptyList == 0: 
        startPointer = 0
        emptyList = 1
        return True
    
    emptyList = linkedList[emptyList].nextNode
    pointer = startPointer
    previousPointer = -1
    while pointer != -1: 
        previousPointer = pointer
        pointer = linkedList[pointer].nextNode
    
    linkedList[previousPointer].nextNode = temp 
    linkedList[temp].nextNode = -1
    
    return True

condition = addNode(linkedList, startPointer, emptyList)
if condition: 
    print("Value added successfully!")
else:
    print("Error: Linked list empty")

outputNodes(linkedList, startPointer)
