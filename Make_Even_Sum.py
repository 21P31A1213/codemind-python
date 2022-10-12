n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if sum(a)%2==0:
        print('1')
        break
    else:
        print('0')
        break