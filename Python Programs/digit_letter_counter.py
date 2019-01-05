Dict_data = {'Letter':0,'Digits':0}
user_input = input()
for character in user_input:
    if character.isdigit() :
        Dict_data['Digits']+=1
    elif character.isalpha():
        Dict_data['Letter']+=1
print("Letters:",Dict_data['Letter'])
print("Digitd :",Dict_data['Digits'])
