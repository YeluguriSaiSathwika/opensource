def fun(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b
n=int(input())
a=list(map(int,input().split()))
print(*(fun(a)))
