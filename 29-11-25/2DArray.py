#DECLARE myList : [5, 5] OF INTEGER
myList : int = [
                [1001, 62],
                [1002, 66],
                [1003, 44],
                [1004, 52],
                [1005, 32],
                ]


def linear_search(ID : int) -> int:
    global myList 
    found : bool = False 
    i : int = -1
    while found == False and i < 4: 
        i += 1 
        if myList[i][0] == ID: 
            return myList[i][1]


    return -1 

def bubble_sort(): 
    global myList
    last : int = 5
    for i in range(5):
        for i in range(last - 1):
            if myList[i][1] > myList[i+1][1]: 
                temp1 : int = myList[i][0]
                temp2 : int = myList[i][1]
                myList[i][0] = myList[i+1][0]
                myList[i][1] = myList[i+1][1]
                myList[i+1][0] = temp1 
                myList[i+1][1] = temp2 
        last -= 1

    display()
    
def display():
    print("----------------------------------")
    for i in range(len(myList)): 
        print(i+1, ": ", myList[i][0], myList[i][1])
    print("----------------------------------")    


bubble_sort()

#ID : int = int(input("Enter ID to be found: "))
#marks : int = linear_search(ID)
#if(marks == -1): 
#    print(f"Student ID: {ID} not found" )
#else: 
#    print(f"Student with ID: {ID} got {marks}")
