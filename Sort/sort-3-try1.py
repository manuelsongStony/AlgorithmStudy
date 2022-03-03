n,k=map(int,input().split())

li1=list(map(int,input().split()))

li2=list(map(int,input().split()))

li1.sort()
li2.sort()

for i in range(k):
    if li1[i]>=li2[n-1-i]:
        break
    else:
        li1[i]=li2[n-1-i]

sum=0
for num in li1:
    sum+=num
print(sum)