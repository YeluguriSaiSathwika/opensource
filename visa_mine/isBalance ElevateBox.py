n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    l,r=0,0,0
    for j in range(i):
        l+=a[j]
    for j in range(i+1,n):
        r+=a[j]
    b.append(abs(l-r))
print(*(b))
