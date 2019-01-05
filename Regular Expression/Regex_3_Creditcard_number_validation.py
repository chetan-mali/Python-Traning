#Regular Expression Credit card number verification
"""
A valid credit card from ABCD Bank has the following characteristics:

It must start with a '4', '5' or ' 6'.
It must contain exactly 16 digits
It must only consist of digits (0-9)
It may have digits in groups of 4, separated by one hyphen "-"
It must NOT use any other separator like ', ' , '_', etc
It must NOT have 4 or more consecutive repeated digits 
"""

import re

#List of credit card numbers 
C_numbers =["4123456789123456","5123-4567-8912-3456","61234-567-8912-3456","4123356789123456","5133-3367-8912-3456","5123 - 3567 - 8912 - 3456"]

#regular Expression for Email Validation
expr=re.compile("^[456][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?([0-9]{4})$") 

#
for number in C_numbers:
    result = expr.findall(number)
    if len(result)>0 and not re.search(r'(\d)\1{3}', re.sub('-', '', number)) :
       print(number,"Valid Number")
    else:
        print(number,"Invalid Number")

        
