from bisect import bisect_left,bisect_right

a=[1,2,3,4,5]
b=[5,4,3,2,1]
right_value=1
left_value=6

right_index=bisect_right(b,right_value)
left_index=bisect_left(b,left_value)


print(right_index)
print(left_index)