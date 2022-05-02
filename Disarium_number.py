Number=int(input())
length=len(str(Number))

Temp=Number
sum=0
rem=0

while Temp>0:
    rem=Temp%10
    sum=sum+int(rem**length)
    Temp=Temp//10
    length=length-1
if sum==Number:
    print('True')
else:
    print('False')