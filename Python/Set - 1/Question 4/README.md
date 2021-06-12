# Question
Given a number N and an array that has N integers. You have to return result array such that, if minimum element of the given array is even, the first element of the result array
should be even and same in the case of odd. Then you have to add the remaining elements into the result array such that there are even and odd nums are in an alternative manner.

# Input 1
<pre>
5
9 12 23 8 5
</pre>

# Output 1
<pre>
5 8 9 12 23
</pre>

# Explanation
As the numbers are to be arranged in increasing order hence we start with 5 in the given array, also the starting number is odd therefore the next number has to be even and has to
be smallest in even number, i.e., 8..... and so on.

# Input 2
<pre>
5
47 49 36 98 90
</pre>

# Output 2
36 47 90 49 98

# Explanation
In the given array, 36 is the smallest number hence we start with it and arramge the series as even-odd alternatively
