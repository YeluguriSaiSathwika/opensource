n=int(input())
s=str(abs(n)) #to convert absolute value of n to string
a=int(s[::-1])
if (-2**31)<=a and a<=(2**31-1):
    if n<0: #if n is negative no.
        print(-a)
    else: #if n is positive no.
        print(a)
else:
    print(0)
