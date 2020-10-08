======================================
List(Mutable)
======================================
List is mutable object in python, so you don't need to pass list
defined in the parent function to the child function

def parent():
  res = []
  def child():
    res.append(1)
    
 This works fine. remember this will not work for normal variable. 
you can still read the variable but can't write it as it is immutable
-----------------------------------------------
a = []
a[0] = 1
This will give an error. You can not do this
a.append(1)
This will work fine

if you want to do a[0] = 1, you need to allocate that list befor accessing it
a=[0]*5
a[0] = 1
this will work fine
----------------------------------------------- 
to allocate row*col 2d array in python
res = [[-1 for _ in range(col)] for _ in range(row)]

or 

a = [[0]*col]*row

for example, 
col = 2
row = 3

a = [[0]*col]*row
res = [[0 for _ in range(col)] for _ in range(row)]
print(a)
print(res)

Both will be same:
[[0, 0], [0, 0], [0, 0]]                                                                                                                                     
[[0, 0], [0, 0], [0, 0]]                                                                                                                                     
                                   

----------------------------------------------- 
To append an element at given index in list, use a.insert(index, val)
a = [2,3,4]
a.insert(0, 1)
a = [1,2,3,4]

----------------------------------------------- 
to check if the given object is a list or not in python is isinstance(x, list)
a = [1,2,3]
if isinstance(a, list):
    print('yes')
else:
    print('no')
    
-----------------------------------------------  
You can merge two list just like strings using + operator
a = [1, 2]
b = [3, 4]
c = a + b
c = [1, 2, 3, 4]
NOTE: both a and b should be list here

In a lot of recursion problems, you will need to append something and
pass it to the other function, for example..

func(curr + [nums[i]])
-----------------------------------------------  

You can find index for an element in the list using index()
a = [1,2,3,4,5]
print(a.index(5)) -> 4
if there are duplicates in the list, it returns the index with the 1st match
a = [1,2,3,5,5,5]
print(a.index(5)) -> 3
-----------------------------------------------

# Python code to demonstrate the working of  
# sum() 
   
numbers = [1,2,3,4,5,1,4,5] 
  
# start parameter is not provided 
Sum = sum(numbers) 
-----------------------------------------------
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

-----------------------------------------------

a = [[1,2,3], [4,5,6], [7,8,9]]
a.pop(1)
a.insert(1, 100.25)
print(a)

-----------------------------------------------
This is very important
in python, list is passed by object reference by default
for example, 

def set_list(my_list): 
    my_list.append("fuck")
  
def add(my_list): 
    my_list.append("D")
 
def print_list(my_list):
    set_list(my_list) 
    add(my_list)
    print(my_list)

print_list(["E"]) 

what would be printed????
You would be expecting the output to be ["E"] right?
But you would be fucked and the output is actually ["E", "fuck", "D"]

How to fix this? you need to pass list as a value and not by the object reference
def set_list(my_list): 
    my_list.append("fuck")
  
def add(my_list): 
    my_list.append("D")
 
def print_list(my_list):
    set_list(list(my_list)) 
    add(list(my_list))
    print(my_list)

print_list(["E"])

output of the above code will be ["E"]

You need to pass list(my_list) instead of my_list. That way you will send the copy of 
my_list and not the object reference of my_list



