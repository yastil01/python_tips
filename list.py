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
to allocate row*col 2d array in python
res = [[-1 for _ in range(col)] for _ in range(row)]

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
