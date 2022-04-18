import copy
a="sundays"
b="saturday"
#answer should be 4
a2="cat"
b2="cut"

a_array=list(a)
b_array=list(b)


#a가 더 작다면 삽입이 낫고 더크다면 교환이 남 -> 삭제는 제일나중에 생각(제일낭비)

temp_array=copy.deepcopy(a_array)

change_count=0

index=0
while temp_array!=b_array:
    if len(temp_array)<len(b_array):
        if temp_array[index]==b_array[index]:
            index+=1
        else:
            temp_array.insert(index, b_array[index])
            change_count+=1
            index += 1
    else:
        if temp_array[index]==b_array[index]:
            index+=1
        else:
            temp_array.pop(index)
            temp_array.insert(index, b_array[index])
            change_count+=1
            index += 1

    if index >=len(b_array):
        n=len(temp_array) - len(b_array)
        for _ in range(n):
            temp_array.pop(len(temp_array)-1)
            change_count += 1

print(change_count)

