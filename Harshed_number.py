n=int(input())
s=0
a=n
while n>0:
    r=n%10
    s=s+r
    n=n//10
if a%s==0:
    print('True')
else:
    print('False')