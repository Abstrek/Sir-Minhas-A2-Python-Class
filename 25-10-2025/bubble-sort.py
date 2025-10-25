#DECLARE myList : ARRAY [0:9] OF INTEGER
myList : int = [45, 15, 5, 35, 25, 95, 55, 85, 65, 75]

def BubbleSort():
    global myList
    last : int = len(myList)
    for i in range(0, len(myList) - 1): 
        for j in range(last - 1): 
            if(myList[j] > myList[j+1]): 
                temp : int = myList[j]
                myList[j] = myList[j+1]
                myList[j + 1] = temp 

        last -= 1

print(myList)
BubbleSort()
print(myList)
