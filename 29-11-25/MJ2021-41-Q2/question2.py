#DECLARE arrayData : ARRAY[0:9] OF INTEGER
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(value: int): 
    global arrayData 
    i = -1 
    while i < len(arrayData) - 1:
        i += 1
        if arrayData[i] == value: 
            return True

    return False
    

value = int(input("Enter a value to be found: "))
condition = linearSearch(value)

if condition == True: 
    print("Value entered was found.")
else: 
    print("Value entered was not found.")

def bubbleSort(): 
    temp = 0
    for x in range(0, len(arrayData) - 1):
        for y in range(0, len(arrayData) -1): 
            if arrayData[y] < arrayData[y+1]: 
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp 
