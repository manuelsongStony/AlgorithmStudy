def binary_search(array,target,start,end):
    while start<=end:
        mid= (start+end)//2

        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1

    return end

n,m = map(int,input().split())

array=list(map(int, input().split()))

array.sort()
sum_rice=0

totalArray=[]

for i in range(n):
    sum_rice=0
    for x in range(i,n):
        sum_rice+=(array[x]-array[i])
    totalArray.append(sum_rice)




totalArray.reverse()

if totalArray[n-1]<m:
    print((sum(array)-m)//n)

else:

    k=binary_search(totalArray,m,0,n-1)

    if totalArray[k]==m:
        print(array[n-1-k])
    else:
        p=0
        while totalArray[k]-p*(n-1-k)>=m:
           p+=1

        p=p-1
        print(array[n - 1 - k]+p)