myList : int = [10, 5, 16, 13, 1]

def insertion_sort():
    for i in range(1, len(myList)): 
        insert_item : int = myList[i]
        currentptr : int = i - 1
        while currentptr > -1 and insert_item < myList[currentptr]: 
            myList[currentptr + 1] = myList[currentptr]
            currentptr -= 1

        myList[currentptr + 1] = insert_item
        print(myList)

def insert(): 
    for i in range(1, len(myList)): 
        item_to_insert = myList[i]
        pointer = i - 1 
        while pointer > -1 and item_to_insert < myList[pointer]: 
            myList[pointer + 1] = myList[pointer]
            pointer -= 1 
            print("-----------------------------------------")
            print(myList)
            print("-----------------------------------------")

        myList[pointer + 1 ]= item_to_insert
        
insert()
