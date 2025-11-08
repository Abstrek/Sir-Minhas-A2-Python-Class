myList : int = [1, 15, 30, 35, 37, 45, 50]

def binary_search(item : int) -> bool: 
    found : bool = False
    end : int = len(myList) - 1
    start : int = 0
    while (found == False) and (start <= end): 
        print("---------------------------")
        print(f"start: {start}, end: {end}")
        mid : int = (end + start) // 2
        print(f"mid: {mid}")
        input()
        if myList[mid] == item:
            return True 
        elif myList[mid] < item: 
            start = mid + 1
        else:
            end = mid - 1

print(len(myList))
binary_search(38)
            
        
