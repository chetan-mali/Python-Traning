from collections import OrderedDict
order_dict = OrderedDict()
check = "hello"
while (check != "QUIT"):
    data = input().upper()
    if data != 'QUIT':
        try:
            data = list(data.split())
            item_price= int(data[len(data)-1])
            item_name=''
            for i in range(len(data)-1):
                item_name = item_name+" "+data[i]
            if item_name != "quit":
                if item_name in order_dict.keys():
                    initial = order_dict[item_name]
                    order_dict[item_name]=initial + item_price
                else:
                    order_dict[item_name] = item_price
            else:
                check = item_name

        except Exception as e:
            print("Invalid Input :" ,e)
    else:
        break

for key,value in order_dict.items():
    print(key,value)
