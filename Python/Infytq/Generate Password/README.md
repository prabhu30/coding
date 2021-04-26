# Generate Password


# Question :
Given input of array of string in format <employee name> <employee number> separated by commas ,you have to generate password for each employee.
Employee name contains only alphabets and employee number contains only digits.

The conditions to generate the password are

The password will be single the character in the name of the employee at the index k

where k is the digit that is present in the employee number that is less than or equal to the length of the employee name.

**Note : The string index should be considered from 1.**

# EXAMPLE

# Input :
<pre> Robert:36787,Tina:68721,Jo:56389 </pre>

# Output :
<pre> tiX </pre>

# EXPLANATION :
Length of Robert is 6 and 6 is present in employee number of Robert 36787, so return the alphabet at position 6 that is 't'.

Length of Tina is 4 and 4 is not present in the 68721 so select the number which is max and less than the length of Tina so select 2 return the alphabet at 
position 2 that is 'i'.

Length of Jo is 2 it is not present in 56389 and there is not present any number which is less than 2 so return 'X'.

# CONSTRAINT :
1<length(employee Name)<10

# INPUT FORMAT :

A single string that that has sub strings separated by commas.

employee name and employee number were separated by colon

# OUTPUT FORMAT :
A single string formed by concatenating the of passwords of all employees.

# Solution (Executable) :
For solution - [Click Here](https://onecompiler.com/python/3wvqmzm3w)
