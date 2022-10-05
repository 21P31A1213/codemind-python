n=str(input())
c='aieouAEIOU'
b=list(n)
d=[]
e=[]
for i in b:
    if i in c:
        d.append(i)
if len(d)>0:
    print(len(d))
else:
    print('0')