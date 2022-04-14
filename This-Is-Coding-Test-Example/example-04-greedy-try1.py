n = int(input())
array = list(map(int, input().split()))

array.sort()
sum_number = 1
for i in range(n):
    if sum_number >= array[i]:
        sum_number += array[i]

    else:

        break;
print(sum_number)