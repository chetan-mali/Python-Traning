#Regular Expression Email Validation 
"""
Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The minimum length is 2 and maximum length of the extension is 4. 
"""


import re
#List of email id both valid and Invaild
Email_list = ["abc@acc@abc.com","lara@hackerrank.com","brian-23@hackerrank.com","britts_54@hackerrank.com"]

#To store valid email 
Valid_emails=[] 

#regular Expression for Email Validation
expr=re.compile("^([a-z0-9_-]+)@[a-z0-9]+\.([a-z]{2,4})$")  

#Loop to check vaild email and store in Valid_emails list 
for email in Email_list:
    result = expr.findall(email)
    if len(result)>0 :
        Valid_emails.append(email)
        
Valid_emails.sort()
print(Valid_emails)
