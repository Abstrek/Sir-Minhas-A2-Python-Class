def AddRecords(): 
    myfile = open("filing.txt", 'a')

    for i in range(15):
        print(i, " record")
        studentID = input("Enter studentID: ").upper()
        while len(studentID) != 6:
            studentID = input("Please enter the ID again: ")
        
        name = input("Enter student name: ").upper()
        while name == "":
            name = input("Name can't be empty \nEnter a valid name: ")
         
        age = int(input("Enter student's age: "))
        while age < 15 or age > 20 : 
            age = int(input("Enter a valid age: "))
            
        gender = input ("Enter student's gender: ").upper()
        while gender != "MALE" and gender != "FEMALE":
            gender = input("Enter either male or female: ").upper()

        info : str = studentID + " " + name + " " + str(age) + " " + gender + "\n"

        myfile.write(info)

    myfile.close()

def DisplayFile(): 
    myFile = open("filing.txt", 'r')
    info : str = myFile.readline().strip()
    while info != "": 
        studentID, name, age, gender = info.split()
        print(studentID, " ", name)
        #print(info)
        info = myFile.readline().strip()
    myFile.close()

DisplayFile()
