n=int(input())
a=list(map(int,input().split()))
k=0
gcd=a[0]
j=1
while(j<n):
    if(a[j]%gcd==0):
        j+=1
    else:
        gcd=a[j]%gcd
print(gcd)