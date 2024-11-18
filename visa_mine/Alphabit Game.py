s=input()
v,c=0,0
for i in s:
    if i in {'a','e','i','o','u','A','E','I','O','U'}:
        v+=1
    elif i.isalpha():
        c+=1
    else:
        pass
print(f'{v},{c}')
