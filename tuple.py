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
