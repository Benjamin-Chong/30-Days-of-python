#Exercises: All of these code segments are the going to be the ones that I am putting into the python interpreter.

#Syntax Error: an error that associated with minor errors like not putting parenthesis where its needed, etc.
#print 'hello world' returns SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

#Name Error: error that is outputted when a variable has not been defined. it is fixed by declaring a variable
#NameError: name 'age' is not defined when I put print(age)
#To fix this all we need to do is define age. For example, we can put age = 20

#Index Error: this error is outputted when the index is out of range.
#numbers = [1, 2, 3]
#numbers[10]
#returns list index out of range. To fix this, we simply need to be more careful where we are trying to access.

#Module Not Found Error: error is raised when the desired import does not exist or was not found.
#import maths returns a module not found because it is not in the python library, therefore we cannot access it.
#it returns - ModuleNotFoundError: No module named 'maths'
#to fix it we need to type import math

#Attribute Error: function does not exist in the module.
#import math
#math.PI returns - AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
#to fix this, we need to use pi to get the correct output. The attributes within these imports are case sensitive.

#Key Error: when accessing a dictionary, it is possible to get a key error when you type a name that does not exist.
#user = {'name': 'Ben', 'age':25}
#user['nae'] returns KeyError: 'nae'
#to fix this, we just need to change nae to name.

#Type Error: usually a mismatch between two types of data. An example of this would be int and string.
#5 + '2' returns TypeError: unsupported operand type(s) for +: 'int' and 'str'
#to fix this, we just need both to be the same type.

#Import Error: this error is outputted when the desired import is not found in its module.
#from math import power returns ImportError: cannot import name 'power' from 'math'
#this is fixed by from math import pow.

#Value Error: error that is outputted when a given string cannot be changed to a number because there is usually a non-numerical number
#int('12a') returns ValueError: invalid literal for int() with base 10: '12a'
#to fix this, we just need to remove the a

#Zero Division Error: dividing by 0.
# 1/0 returns ZeroDivisionError: division by zero
#the only fix is to not divide by 0.
