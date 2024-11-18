s=input()
r=''
for i in s:
    a=ord(i)
    if 97<=a<=122: # if it is lower 97<=a<=122
        r+=chr(a-32)
    else: # if it upper 65<=a<=90
        r+=chr(a+32)
print(r)
