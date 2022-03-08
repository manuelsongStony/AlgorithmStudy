n=int(input())

d=[0]*1000
d[0]=0
d[1]=1
d[2]=3
d[3]=5
d[4]=10
for i in range(3,n+1):
    if i %2==0:
        d[i]=3**(i//2)+1
    else:
        d[i]=d[i-1]*2-1

print(d[n]%796796)
