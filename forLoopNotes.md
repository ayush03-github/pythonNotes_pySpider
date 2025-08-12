Looping : is used to repeat a block of code n number of times based on condition. The block will be repeated until the condition becomes false.


                    TYPES
                      |
               |'''''''''''''|
               |             |
           For Loop        While
              |
    |''''''''''''''''''|
    |                  |
using range()    using Iterable

For : A for loop is used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects. It is typically employed when the number of iterations is known in advance, as it processes each item in the sequence until the sequence is exhausted.

Syntax : For variableName in range (start,stop, step):
            #statement

Example : 
Input : for i in range (1,6,1):
                print(i)

Output : 
1
2
3
4
5

Input : for i in range (1,6,1):
                print(i,end=" ")

Output : 
1 2 3 4 5


Start : from where the loop starts
End : at where the loop ends
Step : change in value (either increment or decrement)



While : A while loop repeatedly executes a block of code as long as a specified condition remains true. It is useful when the number of iterations is not known beforehand, and the loop's termination depends on a condition becoming false. 

