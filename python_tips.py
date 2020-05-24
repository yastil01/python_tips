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

======================================
List
======================================

======================================
Strings
======================================

======================================
Heaps
======================================
