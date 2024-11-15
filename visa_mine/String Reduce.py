s=input()
res=''
c=1
for i in range(1,len(s)+1):
    if i<len(s) and s[i]==s[i-1]:
        c+=1
    else:
        res+=s[i-1]+str(c)
        c=1
print(res)
