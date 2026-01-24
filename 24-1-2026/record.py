class Students: 
    def __init__(self):
        self.Marks = 0
        self.StudentID = ""

myList = [Students() for i in range(5)]

'''
for i in range(5): 
    StudentID = input("Enter Student ID: ")
    Marks = int(input("Enter Student Marks: "))
    myList[i].StudentID = StudentID
    myList[i].Marks = Marks
'''

myList[0].StudentID = "MR1001"
myList[0].Marks = 65
myList[1].StudentID = "MR1002"
myList[1].Marks = 75
myList[2].StudentID = "MR1003"
myList[2].Marks = 35
myList[3].StudentID = "MR1004"
myList[3].Marks = 85
myList[4].StudentID = "MR1005"
myList[4].Marks = 65


def Display(): 
    for i in range(5):
        print("------------------------------------------")
        print(f"StudentID: {myList[i].StudentID}, Marks: {myList[i].Marks}")
    print("------------------------------------------")

def LinearSearch(ID): 
    global myList
    Found = False 
    i = 0 
    while Found == False and i < 5: 
        Student = myList[i].StudentID
        if Student == ID: 
            print(myList[i].Marks)
            Found = True
        else: 
            i += 1

    if Found == False: 
        print(-1)

def Bubble_Sort():
    global myList
    swap = True
    i = 0 
    while swap == True and i < len(myList): 
        swap = False 
        for i in range(len(myList) - 1):   
            if myList[i].Marks <  myList[i+1].Marks:
                swap = True
                temp1 = myList[i+1].StudentID
                temp2 = myList[i+1].Marks
                myList[i+1].StudentID = myList[i].StudentID
                myList[i+1].Marks = myList[i].Marks
                myList[i].StudentID = temp1
                myList[i].Marks  = temp2

            i += 1

def Insertion(): 
    global myList
    for i in range(2, len(myList)): 
        temp1 = myList[i].StudentID
        temp2 = myList[i].Marks
        pointer = i - 1
        while pointer > -1 and myList[pointer].Marks > temp2: 
            Display()
            myList[pointer+1].Marks = myList[pointer].Marks
            myList[pointer+1].StudentID  = myList[pointer].StudentID
            pointer -= 1
        myList[pointer+1].StudentID = temp1
        myList[pointer+1].Marks = temp2




Insertion()
Display()
