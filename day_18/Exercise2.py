#Exercise 2
import re
import keyword
def valid_variable(str):
    must = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(must, str)) and not keyword.iskeyword(str)

print(valid_variable('set'))