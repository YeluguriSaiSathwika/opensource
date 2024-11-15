n=int(input())
a=list(map(int,input().split()))
print(*(a[::-1])) #'*' is used to get only elements from list without commas,brackets.... (to retrieve only values)
