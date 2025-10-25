## <p style="text-align: center;">16/10/2025</p>

### ARRAYS
---

There are no arrays in python, that is why we have to make list into arrays since only lists are by default in python 

Array:- Array can store multiple items of same datatypes and the lenght is defined at the start. <br></br>
List:- Can be any length and length can be changed dynamically (in execution of the program). Datatypes can be different. 

Note:- Indexing in python starts from 0.

We need to declare it in comments as following:- 

```	python
#DECLARE myList : ARRAY [0:4] OF STRING 
```
(do note that this is a comment. Declaration is a requirement of cie no direct intialisation of arrays)

Intialise this array with empty strings as follows:- 
```	python
myList = ["" for index in range(5)] # This '5' can be the length of any array
```

All searching, sorting, input, printing will be done through an array. 
<br></br>
### LINEAR SEARCH 
---
For linear search, use while loop as the "Break" keyword isn't allowed and thus for-loop isn't allowed. 
<br></br>
### FUNCTION
----
Use the keyword "global" besides a variable identifier that is present in the main program and is being used in the function like for example I am using a list present in the main program called "myList" so 
I would put the following in my function: 
```python
	def somerandomfunction() -> int: #arrow means this function returns an integer
		global myList
```
This is a good practice to do. 

