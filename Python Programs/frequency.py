user_input =input()
data ={}
for character in user_input:
    if character in data.keys():
        initial = data[character]
        data[character]=initial + 1
    else:
        data[character] = 1
print(data)