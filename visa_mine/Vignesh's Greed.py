n=int(input())
s=list(map(int,input().split()))
s.sort(reverse=True) #descending order
for i in range(n-2): #for checking all possibilities in given list
    if s[i]<s[i+1]+s[i+2]: #triangle condition
        print(s[i]+s[i+1]+s[i+2]) #triangle perimeter
        break
else:
    print(-1)
