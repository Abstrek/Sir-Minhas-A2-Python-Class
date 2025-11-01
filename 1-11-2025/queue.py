#DECLARE myList : Array[0:4] OF STRING
myList : str = ["" for i in range(5)]
head = -1 
tail = -1

def Display():
    global head, tail, myList
    print("----------------------")
    for i in range(len(myList)):
        print(i, "", myList[i])
    print("head ", head)
    print("tail ", tail)
    print("----------------------")

def enqueue(item : str): 
    global head, tail, myList 
    if(head == 0 and tail == 4) or (head == tail + 1):
        print("Full")
    else: 
        if(head == -1 and tail == -1): 
            head = 0 
            tail = 0 
        elif tail == 4: 
            tail = 0 
        else: 
            tail = tail + 1 

        myList[tail] = item
        print("Enqueued")
    Display()

def dequeue(): 
    global head, tail, mylist
    if(tail == -1 and head == -1):
        print("Queue empty")
    else: 
        temp : int = head
        if(head == 4): 
            head = 0
        else: 
            head += 1

        print(myList[temp], " dequeued")
        myList[temp] = ""
        if(head == tail + 1): 
            head = -1 
            tail = -1
    Display()

enqueue("X")
enqueue("Y")
enqueue("Z")
Display()
dequeue()
enqueue("M")
enqueue("A")
enqueue("B")
dequeue()
Display
    
Display()
