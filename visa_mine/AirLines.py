x,n=map(int,input().split())
p=(n+99)//100 #planes needed for n passengers, (n+99) is done for proper rounding off the number
print(p-x) #p-x --> no. of new planes required
