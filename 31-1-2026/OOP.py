#Class definition
class Students: 

    #PRIVATE StudentID : STRING
    #PRIVATE Name : STRING
    #PRIVATE Age : INTEGER

    def __init__(self): 
        self.__name  = ""
        self.__studentID = ""
        self.__age = 0

    def SetAge(self, i): 
        self.__age = i

    def SetID(self, i): 
        self.__studentID = i

    def SetName(self, i): 
        self.__name = i

    def GetAge(self): 
        return self.__age

    def GetID(self): 
        return self.__studentID

    def GetName(self): 
        return self.__name

    def Display(self): 
        print("ID:   ", self.__studentID)
        print("Name: ", self.__name)
        print("Age:  ", self.__age)


class Subjects(Students):  

    #PRIVATE Sub1 : STRING
    #PRIVATE Sub2 : STRING 
    #PRIVATE Sub3 : STRING 
    
    def __init__(self): 
        super().__init__()
        self.__sub1 = ""
        self.__sub2 = ""
        self.__sub3 = ""

    def SetSubjects(self, s1, s2, s3): 
        self.__sub1 = s1
        self.__sub2 = s2
        self.__sub3 = s3

    def GetSub1(self): 
        return self.__sub1

    def GetSub2(self):
        return self.__sub2

    def GetSub3(self): 
        return self.__sub3

    def Display():
        super().Display()
        print("Sub1: ", self.Sub1)
        print("Sub2: ", self.Sub2)
        print("Sub3: ", self.Sub3)

#Testing of the first class
     
x = [Subjects() for i in range(3)]

for i in range(3):
    id = input("Enter id:   ")
    na = input("Enter name: ")
    ag = int(input("Enter age:  "))
    s1 = input("Enter Sub1: ")
    s2 = input("Enter Sub2: ")
    s3 = input("Enter Sub3: ")
    x[i].SetID(id)
    x[i].SetName(na)
    x[i].SetAge(ag)
    x[i].SetSubjects(s1, s2, s3)


for i in range(3): 
    print("----------------------------------------------------------------------------------------")
    print(f"StudentID: {x[i].GetID()}, Name: {x[i].GetName()}, Age: {x[i].GetAge()}")
    print(f"1st Subject: {x[i].GetSub1()}, 2nd Subject: {x[i].GetSub2()}, 3rd Subject: {x[i].GetSub3()}")

print("----------------------------------------------------------------------------------------")
