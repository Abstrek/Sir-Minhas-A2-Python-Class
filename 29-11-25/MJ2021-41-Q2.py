#DECLARE arrayData : ARRAY[0:9] OF INTEGER
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(value: int): 
    global arrayData 
    i = -1 
    while i < len(arrayData):
        i += 1
        if arrayData[i] == value: 
            return True

    return False

    

print(linearSearch(10))
