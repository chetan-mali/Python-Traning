string  = "RESTART"
index = string.index("R")+1
string_f=string[0:index]+string[index:].replace("R","$")
print(string_f)
