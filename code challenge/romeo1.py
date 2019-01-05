# Read all lines and break all word in list ,then count each word using Dictinory [romeo.txt]
while(True):
    try:
        file = open("romeo.txt","r")
        List = file.readlines()
        word_dict ={}
        for data in List:
            new_list = data.split()
            for word in new_list:
                if word in word_dict.keys():
                    word_dict[word] += 1
                else:
                    word_dict[word] =1
    except Exception as e:
        print(e)
    else:
        break
    finally:
        file.close()
for key,value in word_dict.items():
    print(key,":",value,sep='')