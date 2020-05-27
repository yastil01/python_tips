def list_top_1():
    myList = ['janet']
    def update_list_1():
        myList.append('yash')
    update_list_1()
    print(myList)

def list_top_2():
    myList = ['janet']
    def update_list_2(givenList):
        givenList.append('yash')
    update_list_2(myList)
    print(myList)
    
list_top_1()
list_top_2()

=========================
output
=========================
['janet', 'yash']                                                                                                                                                                                                                               
['janet', 'yash']      

=========================
Explaination
=========================
The answer is NO. 

In case 1, we don't pass myList which is defined in the parent function 
to child function. But because list is mutable in python, the modification
is allowed in the child function

In case 2, we pass myList which is defined in the parent function 
to child function. In this case, the same object is sent to the child 
function and modified list is returned
