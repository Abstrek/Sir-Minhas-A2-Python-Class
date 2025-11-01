#DECLARE myList : ARRAY [0:4] OF STRING
myList : str = ["" for i in range(5)]

top_of_stack : int  = -1 

def push(item : str): 
    global myList, top_of_stack 
    print(top_of_stack)
    if top_of_stack == len(myList) - 1: 
        print("Stack full")
    else:
        top_of_stack = top_of_stack + 1 
        myList[top_of_stack] = item
        print(item, " pushed")

def display():
    global myList, tos
    print("---------------------")
    for i in range(len(myList)): 
        print(i,"" , myList[i])

    print("top of stack: ", top_of_stack)
    print("---------------------")

def pop():
    global myList, top_of_stack
    if top_of_stack == -1: 
        print("Stack is already empty")
    else: 
        print(myList[top_of_stack], " has been popped.")
        myList[top_of_stack] = ""
        top_of_stack = top_of_stack - 1 

push("h")
push("h")
push("h")
pop()
push("h")
pop()
push("h")
push("h")
pop()
display()
