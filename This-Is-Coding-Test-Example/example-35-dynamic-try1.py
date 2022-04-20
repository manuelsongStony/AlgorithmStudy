"""
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36
1, 2, 3, 4, 5, 6, 7, 8, 9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
0, 1, 0, 2, 0, 1, 3, 0, 1,  2, 0, 4, 1, 2, 3, 0, 0, 1, 5
"""

array = []

array.append(1)

ugly = [2, 3, 5]
compare = [[2, 0], [3, 0], [5, 0]]
for i in range(1000):
    a = compare[0][0] * array[compare[0][1]]
    b = compare[1][0] * array[compare[1][1]]
    c = compare[2][0] * array[compare[2][1]]
    temp = min(a, b, c)

    array.append(temp)
    if temp == a:
        if a == b and b == c:
            compare[0][1] += 1
            compare[1][1] += 1
            compare[2][1] += 1
        elif a == b:
            compare[0][1] += 1
            compare[1][1] += 1
        elif a == c:
            compare[0][1] += 1
            compare[2][1] += 1
        else:
            compare[0][1] += 1
    elif temp == b:
        if b == c:
            compare[1][1] += 1
            compare[2][1] += 1
        else:
            compare[1][1] += 1
    else:
        compare[2][0] += 1

print(array)
