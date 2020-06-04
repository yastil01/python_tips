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

hash = {'a': 1, 'b': 2, 'c': 3}
hash = sorted(hash.items(), key = lambda x: x[0])
print(hash)
output -> [('a', 1), ('b', 2), ('c', 3)]      

for key, val in hash:
    print(key, val)

output:
a 1                                                                                                                                                          
b 2                                                                                                                                                          
c 3      

# to sort hash based on 1st index of value
hash = {'a': [7,1], 'b': [2,5], 'c': [3,7]}
hash = sorted(hash.items(), key = lambda x: x[1][1])
for key, val in hash:
    print(key, val)

output:
a [7, 1]                                                                                                                                                     
b [2, 5]                                                                                                                                                     
c [3, 7]

# to sort hash based on 0th index of value
hash = {'a': [7,1], 'b': [2,5], 'c': [3,7]}
hash = sorted(hash.items(), key = lambda x: x[1][0])
for key, val in hash:
    print(key, val)
    
output:
b [2, 5]                                                                                                                                                     
c [3, 7]                                                                                                                                                     
a [7, 1] 

Note: Watch closely, we are not using hash.values() even if we want to sort 
hash based on the value. if we do that, output will be totally different. You 
will lose keys. If you want to still use keys, always use hash.items(), that will
convert hash into list but it will maintain output as tuples of (key, value) pair

# sorting hash based on the values gives output list in which keys are not present
hash = {'a': [7,1], 'b': [2,5], 'c': [3,7]}
hash = sorted(hash.values(), key = lambda x: x[1])
for key, val in hash:
    print(key, val)
    
output:
7 1                                                                                                                                                          
2 5                                                                                                                                                          
3 7   
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

-----------------------------------------------
Syntax : str.split(separator, maxsplit)

Parameters :
separator : This is a delimiter. The string splits at this specified separator. 
  If is not provided then any white space is a separator.
  
maxsplit : It is a number, which tells us to split the string into maximum of 
  provided number of times. If it is not provided then there is no limit.

Returns : Returns a list of strings after breaking the given string by the specified separator. 

text = 'geeks for geeks'
# Splits at space 
print(text.split()) 
['geeks', 'for', 'geeks']

  
word = 'geeks, for, geeks'
# Splits at ',' 
print(word.split(','))
['geeks', 'for', 'geeks']

  
word = 'geeks:for:geeks'
# Splitting at ':' 
print(word.split(':'))
['geeks', 'for', 'geeks']


word = 'CatBatSatFatOr'
# Splitting at 3 
print([word[i:i+3] for i in range(0, len(word), 3)]) 
['Cat', 'Bat', 'Sat', 'Fat', 'Or']

['geeks', 'for', 'geeks']
['Cat', 'Bat', 'Sat', 'Fat', 'Or']

-----------------------------------------------
The join() method provides a flexible way to create strings from iterable objects. 
It joins each element of an iterable (such as list, string and tuple) by a string 
separator (the string on which the join() method is called) and returns the concatenated string.

string.join(iterable)

# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))
1, 2, 3, 4

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))
1, 2, 3, 4

s1 = 'abc'
s2 = '123'
# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))
s1.join(s2): 1abc2abc3

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))
s2.join(s1): a123b123c

-----------------------------------------------
an_upper = "A"
an_uppercase_check = an_upper.isupper()
print(an_uppercase_check)
True

if given a string, it checks all char
an_upper = "Ab"
an_uppercase_check = an_upper.isupper()
print(an_uppercase_check)
False
-----------------------------------------------
an_lower = "a"
an_lowercase_check = an_lower.islower()
print(an_lowercase_check)
True

if given a string, it checks all char
an_lower = "aB"
an_lowercase_check = an_lower.islower()
print(an_lowercase_check)
-----------------------------------------------
string = '15460'
print(string.isdigit()) 
True

string = '154ayush60'
print(string.isdigit())
False
-----------------------------------------------
The isalpha() methods returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.

string = 'Ayush'
print(string.isalpha())
True
   
string = 'Ayush0212'
print(string.isalpha())
False
   
# checking if space is an alphabet 
string = 'Ayush Saxena'
print( string.isalpha())
False
-----------------------------------------------
isalnum() to check if string only contains numbers and alphabets












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
