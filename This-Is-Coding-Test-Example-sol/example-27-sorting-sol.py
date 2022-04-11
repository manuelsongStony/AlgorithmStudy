import bisect
def binary_search(array,x,start,end):
    if start>end:
        return end

    mid=(start+end)//2

    if array[mid] ==x:
        return mid

    if array[mid]>x:
        return  binary_search(array, x, start, mid-1)
    else:
        return binary_search(array, x, mid+1, end)



n,x=7,4
array=[1,1,2,2,2,2,3]

k=binary_search(array,x+0.5,0,n-1)-binary_search(array,x-0.5,0,n-1)

if k==0:
    k=-1

print(k)
