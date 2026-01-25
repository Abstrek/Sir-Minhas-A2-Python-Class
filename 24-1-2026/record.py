
#Record datatype Students
class Students: 
    #DECLARE self.Marks : INTEGER
    #DECLARE self.Marks : INTEGER

    #self means passing the student class to itself so the class can use its functions.
    def __init__(self):
        self.Marks = 0
        self.StudentID = ""

#Intializing the array myList with the Students record datatype. 
myList = [Students() for i in range(5)]


#Taking values of the array as input.
'''
for i in range(5): 
    StudentID = input("Enter Student ID: ")
    Marks = int(input("Enter Student Marks: "))
    myList[i].StudentID = StudentID
    myList[i].Marks = Marks
'''


#Hardcoding the values for quicker testing. 
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


'''
Since we cannot just print(myList) (It will just return the data type and address) we will need to create
a different function for displaying the data.
'''
def Display(): 
    for i in range(5):
        print("------------------------------------------")
        print(f"StudentID: {myList[i].StudentID}, Marks: {myList[i].Marks}")
    print("------------------------------------------")


#Linear search with the ID given
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

#Bubble sort
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


Bubble_Sort()
Display()
