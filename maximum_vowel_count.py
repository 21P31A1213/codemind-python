n=str(input())
a=n.lower()
b=a.split()
d='aieou'
m=[]
for i in b:
    s=0
    c=list(i)
    for j in c:
        if j in d:
            s=s+1
    m.append(s)
print(max(m))
    