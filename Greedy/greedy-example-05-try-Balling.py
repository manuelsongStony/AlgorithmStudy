n, m = map(int, input().split())

array = list(map(int, input().split()))
counter = 0

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if array[i] != array[j]:
            counter += 1

print(counter)
