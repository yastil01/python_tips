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
