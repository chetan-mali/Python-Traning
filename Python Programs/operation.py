def Add(List):
    return sum(List)
def Multiply(List):
    result = 1
    for element in List:
        result = result * element
    return result
def Largest(List):
    return max(List)
def Smallest(List):
    return min(List)
def Sorting(List):
    List.sort()
    return List
def Duplication(List):
    List = list(set(List))
    return List
def Print():
    print("Sum :", Add(user_input))
    print("Multiply :", Multiply(user_input))
    print("Largest:", Largest(user_input))
    print("Smallest :", Smallest(user_input))
    print("Sorted :", Sorting(user_input))
    print("Without Duplication:", Duplication(user_input))
while(True):
    try:
        user_input = list(map(int,input("Enter Number (seperated by space):").split()))
    except Exception :
        print("Invalid Input !!")
    else:
        break
Print()