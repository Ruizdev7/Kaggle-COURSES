"""
Printing
One of the simplest (and most important!) tasks you can ask a computer to do is to print a message.

In Python, we ask a computer to print a message for us by writing print() and 
putting the message inside the parentheses and enclosed in quotation marks. 
Below, we ask the computer to print the message Hello, world!.
"""

# print("this is my first print in kaggle course")


"""
Arithmetic
We can also print the value of some arithmetic operation 
(such as addition, subtraction, multiplication, or division).

For instance, in the next code cell, the computer adds 2 to 1 and then prints
the result, which is 3. Note that unlike when we were simply printing text, 
we don't use any quotation marks.
"""

# print(2 + 3)


# We can also do subtraction in python. The next code cell subtracts 5 from 9 and prints the result, which is 4.

# print(9 - 5)

"""
You can actually do a lot of calculations with python! See the table below for some examples.

Operation	Symbol	Example
Addition	+	1 + 2 = 3
Subtraction	-	5 - 4 = 1
Multiplication	*	2 * 4 = 8
Division	/	6 / 3 = 2
Exponent	**	3 ** 2 = 9

"""

# You can control the order of operations in long calculations with parentheses.


# print(((1 + 3) * (9 - 2) / 2) ** 2)


# In general, Python follows the PEMDAS rule when deciding the order of operations

"""
How Do I Remember It All ... ? PEMDAS !
P -> Parentheses first
E -> Exponents (ie Powers and Square Roots, etc.)
MD -> Multiplication and Division (left-to-right)
AS -> Addition and Subtraction (left-to-right)

Divide and Multiply rank equally (and go left to right).
Add and Subtract rank equally (and go left to right)
"""


"""
Comments
We use comments to annotate what code is doing. They help other people to understand
your code, and they can also be helpful if you haven't looked at your own code in a while. 
So far, the code that we have written is very short, but annotations become more important 
when you have written a lot of code.

For instance, in the next code cell, we multiply 3 by 2. We also add a comment (# Multiply 3 by 2) 
above the code to describe what the code is doing.
"""


# Multiply 3 by 2
# print(3 * 2)


"""
To indicate to Python that a line is comment (and not Python code), you need to write a pound sign (#) as the very first character.

Once Python sees the pound sign and recognizes that the line is a comment, it is completely ignored by the computer. 
This is important, because just like English or Hindi (or any other language!), Python is a language with very strict rules that need to be followed. 
Python is stricter than a human listener, though, and will just error if it can't understand the code.

We can see an example of this, in the code cell below. Python errors if we remove the pound sign, because the text in the comment 
is not valid Python code, so it can't be interpreted properly.
"""


"""
Multiply 3 by 2
  File "/tmp/ipykernel_18/3750420471.py", line 1
    Multiply 3 by 2
             ^
SyntaxError: invalid syntax
"""


"""
Variables
So far, you have used code to make a calculation and print the result, and the result isn't saved anywhere. 
However, you can imagine that you might want to save the result to work with it later. For this, you'll need to use variables.

Creating variables
The next code cell creates a variable named test_var and assigns it the value that we get when we add 5 to 4.

We then print the value that is assigned to the variable, which is 9.
"""


# Create a variable called test_var and give it a value of 4+5
# test_var = 4 + 5

# Print the value of test_var
# print(test_var)

"""
In general, to work with a variable, you need to begin by selecting the name you want to use. 
Variable names are ideally short and descriptive. They also need to satisfy several requirements:

They can't have spaces (e.g., test var is not allowed)
They can only include letters, numbers, and underscores (e.g., test_var! is not allowed)
They have to start with a letter or underscore (e.g., 1_var is not allowed)
Then, to create the variable, you need to use = to assign the value that you want it to have.

You can always take a look at the value assigned to the variable by using print() and 
putting the name of the variable in parentheses.

Over time, you'll learn how to select good names for Python variables. It's completely fine for it to feel uncomfortable now, 
and the best way to learn is just by viewing a lot of Python code!
"""

"""
Manipulating variables
You can always change the value assigned to a variable by overriding the previous value.

In the code cell below, we change the value of my_var from 3 to 100.
"""

# Set the value of a new variable to 3
# my_var = 3

# Print the value assigned to my_var
# print(my_var)

# Change the value of the variable to 100
# my_var = 100

# Print the new value assigned to my_var
# print(my_var)

"""
Note that in general, whenever you define a variable in a code cell, all of the 
code cells that follow also have access to the variable. For instance, we use 
the next code cell to access the values of my_var (from the code cell above) and 
test_var (from earlier in this tutorial).
"""

# print(my_var)
# print(test_var)

"""
The next code cell tells Python to increase the current value of my_var by 3.

To do this, we still need to use my_var = like before. And also just like before, 
the new value we want to assign to the variable is to the right of the = sign.
"""

# Increase the value by 3
# my_var = my_var + 3

# Print the value assigned to my_var
# print(my_var)


"""
Using multiple variables
It's common for code to use multiple variables. This is especially useful when we have 
to do a long calculation with multiple inputs.

In the next code cell, we calculate the number of seconds in four years. 
This calculation uses five inputs.
"""

# Create variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)


"""
As calculated above, there are 126144000 seconds in four years.

Note it is possible to do this calculation without variables as 
just 60 * 60 * 24 * 365 * 4, 
but it is much harder to check that the calculation without variables does not have some error, 
because it is not as readable. When we use variables (such as num_years, days_per_year, etc), 
we can better keep track of each part of the calculation and more easily check for and correct any mistakes.

Note that it is particularly useful to use variables when the values of the inputs 
can change. For instance, say we want to slightly improve our estimate by updating the value of the number of days in a year from 365 to 365.25, 
to account for leap years. Then we can change the value assigned to days_per_year without changing any of the other variables and redo the calculation.
"""

# Update to include leap years
days_per_year = 365.25

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)


"""
Note: You might have noticed the .0 added at the end of the number, which might look unnecessary. 
This is caused by the fact that in the second calculation, we used a number with a fractional part (365.25), 
whereas the first calculation multipled just numbers with no fractional part. 
You'll learn more about this in Lesson 3, when we cover data types.
"""


"""
Debugging
One common error when working with variables is to accidentally introduce typos. 
For instance, if we spell hours_per_day as hours_per_dy, Python will error with message 
NameError: name 'hours_per_dy' is not defined.
"""

"""
print(hours_per_dy)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/tmp/ipykernel_18/142450907.py in <module>
----> 1 print(hours_per_dy)

NameError: name 'hours_per_dy' is not defined
"""

"""
linkcode
When you see NameError like this, it's an indication that you should check how you have spelled 
the variable that it references as "not defined". Then, to fix the error, you need only correct the spelling.
"""
