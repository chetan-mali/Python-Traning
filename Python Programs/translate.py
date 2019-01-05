user_input = input("Enter a string :")
vowels = ['a','e','i','o','u','A','E','I','O','U',' ']
updated_string = ''
for character  in user_input:
    if character not in vowels:
        updated_string = updated_string + character + "o" + character
    else:
        updated_string = updated_string + character
print(updated_string)
