======================================
Hash
======================================

# Declare hash function       
key_value = {}     
  
# Initializing value  
key_value[2] = 56       
key_value[1] = 2 
key_value[5] = 12 
key_value[4] = 24
key_value[6] = 18      
key_value[3] = 323 
  
print ("Task 1:-\n") 
print ("Keys are") 
   
# iterkeys() returns an iterator over the  
# dictionary’s keys.
for i in sorted (key_value.keys()) :  
    print(i) 
    
print ("Task 2:-\n") 
print ("Reverse: Keys are") 
for i in sorted (key_value.keys(), reverse = True) :  
    print(i) 

print ("Task 3:-\n") 
print ("Values are") 
# iterkeys() returns an iterator over the  
# dictionary’s keys. 
for i in sorted (key_value.values()) :  
    print(i) 
    
print ("Task 4:-\n") 
print ("Reverse Values are") 
for i in sorted (key_value.values(), reverse = True) :  
    print(i) 
