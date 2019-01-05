#Regular Expression for floating number
"""
In this task, a valid float number
must satisfy all of the following requirements:

Number can start with +, - or . symbol.
"""

import re
N = input("Enter a Number :")
expr=re.compile("^[+-]?[0-9]*\.([0-9]+)$")
result = expr.findall(N)
if len(result)>0:
    print("True")
else:
    print("False")