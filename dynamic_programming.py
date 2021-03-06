Subarray/Substring
================================================================================
A subbarray is a contiguous part of array. An array that is inside another array. 
For example, consider the array [1, 2, 3, 4], There are 10 non-empty sub-arrays. 
The subbarays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4). 

In general, for an array/string of size n, 
there can be n subarrays of size 1
there can be n-1 subarrays of size 2
there can be n-2 subarrays of size 3
....
....
there can be 2 subarray of size n-1
there can be 1 subaaray of size n

so total subarrays = n + n-1 + n-2 + ... + 2 + 1 = n*(n+1)/2
there are n*(n+1)/2 non-empty subarrays/subsrings.



Subset/subsequence
================================================================================
A subsequence is a sequence that can be derived from another sequence by zero or more elements, 
without changing the order of the remaining elements.For the same example, there are 15 sub-sequences. 
They are (1), (2), (3), (4), (1,2), (1,3),(1,4), (2,3), (2,4), (3,4), (1,2,3), (1,2,4), (1,3,4), (2,3,4), (1,2,3,4). 
Basically for each element, we have two options. Either pick it in the subsequece or leave it

More generally, we can say that for a sequence of size n, we can have (2^n-1) non-empty sub-sequences in total. 2^n if 
you count an empty string too
