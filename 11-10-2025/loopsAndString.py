myData = "ALPHA COLLLEGE"
count = 0 
i = -1

letter = input("Enter a letter: " ).upper()

for index in myData: 
    i += 1 
    if index == letter: 
        print(f"letter {letter} found at position {i}")
        count += 1

if(count  == 0):
    print("not found")



