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
-----------------------------------------------  

You can find index for an element in the list using index()
a = [1,2,3,4,5]
print(a.index(5)) -> 4
if there are duplicates in the list, it returns the index with the 1st match
a = [1,2,3,5,5,5]
print(a.index(5)) -> 3
