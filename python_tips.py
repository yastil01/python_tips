======================================
Hash(Mutable)
======================================
# to iterate over hash key
hash = {'a': 1, 'b': 2, 'c': 3}
for key, val in hash.items():
  print(key, val)
  
for key in hash:
  print(key, hash[key])
-----------------------------------------------  
# to sort hash by key
hash = sorted(hash.items(), key = lambda x: x[0])

# to sort hash by key in reverse
hash = sorted(hash.items(), key = lambda x: x[0], reverse = True)

# to sort hash by value
hash = sorted(hash.items(), key = lambda x: x[1])

# to sort hash by value
hash = sorted(hash.items(), key = lambda x: x[1], reverse = True) 

NOTE: THE HASH WILL NOW BECOME A LIST, SO IF YOU USE HASH.ITEMS(),
IT WILL GIVE ERROR. FOLLOWING SHOULD WORK

for key, val in hash:
    print(key, val)
-----------------------------------------------  
To know if the python object is dictionary or not, we can use the following
isinstance(x, dict) -> returns True if x is a dictionary.
NOTE:
This should be aplicable to other data types too

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

======================================
Strings(immutable)
======================================
To sort a string you can use sorted
s = "dcba"
s = sorted(s)
this will give s = ['a', 'b', 'c', 'd']

so we need to merge 
s = ''.join(sorted(s))
s will now become "abcd"

======================================
Heaps(Mutable)
======================================

======================================
Tuple(Immutable)
======================================
Tuple is immutable.
1) 
a = (1, 2, 3)
a[0] = 100 -> ERROR...! -> TypeError: 'tuple' object does not support item assignment
NOTE:  
so, you can not change the content of immutable objects after they are created.
  
2)
a = (1, 2, 3)
a = (100, 200, 300) -> works..!
NOTE:
You can always assign it to new value though as shown in the ex 2

3)
a = ([1,2,3], 'yash')
a[0][0] = 100 -> works...! -> ([100, 2, 3], 'yash')
NOTE:
This works fine becuse mutable property is not based on the tuples, it is based on the
objects tuples are pointing to. List is mutable so you can still modify that part of tuple

4)
a = ([1,2,3], 'yash')
a[1] = 'janet' -> ERROR..! -> TypeError: 'tuple' object does not support item assignment 
Note:
This doesn't work becuse a[1] is pointing to a string which is immutable

Immutable Objects : These are of in-built types like int, float, bool, string, unicode, tuple. 
Mutable Objects : These are of type list, dict, set . Custom classes are generally mutable. 
