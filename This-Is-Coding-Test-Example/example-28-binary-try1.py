"""
n=5
array=[-15,-6,1,3,7]
"""
n=7
array=[-15,-4,2,8,9,13,15]

def binary_search(array):

    low =0
    high=n
    while True:
        mid = (high+low)// 2

        if array[mid]==mid:
            return mid

        if low>high:
            return -1

        if array[mid]<mid:
            low=mid+1
        if array[mid]>mid:
            high=mid-1


print(binary_search(array))