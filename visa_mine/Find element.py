n=int(input())
a=list(map(int,input().split()))
x=int(input())
if x in a:
    print(a.index(x)) #for checking the index of the present value
else:
    print(-1)
