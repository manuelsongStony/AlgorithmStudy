def binary_search(array,target):
    start=0
    end=len(array)-1
    mid= (start+end)//2

    while start<=end:

        if  array[mid] == target:
            return array[mid]
        elif array[mid]>target:
            end=mid-1
        else:
            start =mid+1


    return end


n=4
array=[5,1,7,9]

array.sort()

mid=(array[0]+array[-1])//2

print(binary_search(array,mid))
