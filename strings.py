======================================
Strings(immutable)
======================================
Strings are immutable in python. Means once declared, you can't modify 
perticular index

for example,
a = 'yash'
a[0] = 'p'
print(a)

output:
Traceback (most recent call last):                                                                                                                           
  File "main.py", line 10, in <module>                                                                                                                       
    a[0] = 'p'                                                                                                                                               
TypeError: 'str' object does not support item assignment
  
NOTE: if you want to perform some operation on string in place, you gotta
  convert string to list and then join it again. conversion can be done like
  this. if you are given list of char, you are fine. You can modify in place
  
  s = list(s)
  
-----------------------------------------------
  
lets say you wanna swap two index char in a list of string. don't use custom
swap function. You can just do it in this pythonic way. To swap s[i] with s[j]

s[i], s[j] = s[j], s[i]

-----------------------------------------------
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

-----------------------------------------------
To convert entire string in lower case
string_name = string_name.lower()

NOTE: Make sure you need to recive it back to some string. The function
doesn't do in place lowering of characters
-----------------------------------------------
to remove punctuation from string

for c in string.punctuation:
  string_name = string_name.replace(c,' ')

NOTE: make sure you need to receive it back to some string. The function 
  doesn't fo in place replace
-----------------------------------------------
  
# Python3 code to remove whitespace 
def remove(string): 
    return string.replace(" ", "") 
      
# Driver Program 
string = ' g e e k '
print(remove(string)) 
