

n,m =map(int, input().split())
data=[]
for i in range(n):
    k=list((map(int,input().split())))
    if(len(k)!=m):
        print("there is bug")
        break
    k.sort()
    data.append(k[0])
data.sort()
print(data[n-1])

