======================================
Hash
======================================
# to iterate over hash key
hash = {'a': 1, 'b': 2, 'c': 3}
for key, val in hash.items():
  print(key, val)
  
for key in hash:
  print(key, hash[key])

# to sort hash by key
hash = sorted(hash.items(), key = lambda x: x[0])

# to sort hash by key
hash = sorted(hash.items(), key = lambda x: x[0], reverse = True)

# to sort hash by value
hash = sorted(hash.items(), key = lambda x: x[1])

# to sort hash by value
hash = sorted(hash.items(), key = lambda x: x[1], reverse = True) 

NOTE: THE HASH WILL NOW BECOME A LIST, SO IF YOU USE HASH.ITEMS(),
IT WILL GIVE ERROR. FOLLOWING SHOULD WORK

for key, val in hash:
    print(key, val)
======================================
List
======================================
to allocate row*col 2d array in python
res = [[-1 for _ in range(col)] for _ in range(row)]

You can merge two list just like strings using + operator
a = [1, 2]
b = [3, 4]
c = a + b
c = [1, 2, 3, 4]
NOTE: both a and b should be list here

======================================
Strings
======================================
To sort a string you can use sorted
s = "dcba"
s = sorted(s)
this will give s = ['a', 'b', 'c', 'd']

so we need to merge 
s = ''.join(sorted(s))
s will now become "abcd"
======================================
Heaps
======================================
