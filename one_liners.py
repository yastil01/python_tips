- when you append something in the list, just think if there is a chance that None will get appended. 
  This can fail the code in many corner cases. if there are chances that None will be in the list, while popping
  check if the popped element is not None and then only do other things
  
- when you use 'and' condition in if, try breaking both condition and see if the code works fine. Sometimes,
  if you don't be careful to check both conditions, code will go and execute else part which is not desired
  
  for example, in backspace string example. # represents backspace and you need to make a string with backspece effect
  intuituvely you might write this
  
  for char in s:
    if char == '#' and stack:
        stack.pop()
    else:
        stack.append(char)
        
  Now lets take this string s = '#abc'. In this case, # will also be appended in the stack which is not expected
  fix should be like this
  
  for char in s:
    if char != '#':
      stack.append(char)
    else:
      if stack:
        stack.pop()
  
