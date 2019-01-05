List = [12,24,35,24,88,120,155,88,120,155]
List2 =[]
for element in List:
    if element not in List2:
        List2.append(element)
print(List2)