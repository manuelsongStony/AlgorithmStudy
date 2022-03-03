n=int(input())
listN=list(map(int,input().split()))

m=int(input())
listM=list(map(int,input().split()))

k=max(listN)
coso_list=[0]*(k+1)

#for i in range(k+1):
 #   coso_list[i]=0

for element in listN:
    coso_list[element] +=1

for wants in listM:
    if coso_list[wants] >0:
        print('yes', end = ' ')
    else:
        print('no', end=' ')



