def hash_top_1():
    hash = {'janet': 200}
    def update_hash_1():
        hash['yash'] = 100
    update_hash_1()
    print(hash)

def hash_top_2():
    hash = {'janet': 200}
    def update_hash_2(map):
        map['yash'] = 100
    update_hash_2(hash)
    print(hash)

hash_top_1()
hash_top_2()

=========================
output
=========================
{'janet': 200, 'yash': 100}                                                                                                                                  
{'janet': 200, 'yash': 100}

=========================
Explaination
=========================
The answer is NO. 

In case 1, we don't pass hash which is defined in the parent function 
to child function. But because hash is mutable in python, the modification
is allowed in the child function

In case 2, we pass hash which is defined in the parent function 
to child function. In this case, the same object is sent to the child 
function and modified hash is returned

