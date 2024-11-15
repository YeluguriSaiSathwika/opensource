n=int(input())
k=int(input())
a=str(bin(n))[2:] #[2:] indexing is done to remove '0b' {when we covert dec to bin using bin() it starts with 0b}
if k<=len(a) and a[-k]=='1': #[-k] negative indexing because bit counting starts from LSB(rightend)
    print('true')
else:
    print('false')
