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

#output
Task 1:-                                                                                                                                                                                                                    
                                                                                                                                                                                                                            
Keys are                                                                                                                                                                                                                    
1 2 3 4 5 6 Task 2:-                                                                                                                                                                                                        
                                                                                                                                                                                                                            
Reverse: Keys are                                                                                                                                                                                                           
6 5 4 3 2 1 Task 3:-                                                                                                                                                                                                        
                                                                                                                                                                                                                            
Values are                                                                                                                                                                                                                  
2 12 18 24 56 323 Task 4:-                                                                                                                                                                                                  
                                                                                                                                                                                                                            
Reverse Values are                                                                                                                                                                                                          
323 56 24 18 12 2        
