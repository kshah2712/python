# You are given a string and your task is to swap cases. In other words, convert
# all lowercase letters to uppercase letters and vice versa
# 20CS018-Dev Halvawala

def swap_case(s):

    temp = []
    lst = list(s)

    for i in lst:
        j = ""
        if i.islower():
            j = i.upper()
        elif i.isupper():
            j = i.lower()
        else:
            temp.append(i)
        temp.append(j)
    
    r = ''.join(temp)
    
    return r

s = input()
result = swap_case(s)
print(result)