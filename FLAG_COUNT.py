a=int(input())
ar=[]
fa=fb=2
fn=0
for i in range(a):
    ar.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
print(ar[a-1])