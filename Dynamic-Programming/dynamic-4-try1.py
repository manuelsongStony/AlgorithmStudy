n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [-1] * 10001

for i in range(n):
    d[array[i]] = 1
# 5 7 11
# d[8]=-1, d[9]=-1 d[10]=2 d[11]=1 d[12]=-1
#5 +5, 5+7, 5+11
#7+7, 7+11
# 11+11
# 11+5+7
for i in range(1, m + 1-array[n-1]):
    if d[i]!=-1:
        for j in range(n):
            if d[i+array[j]]!=-1:
                min(d[i+array[j]], d[i] + 1)
            else:
                d[i + array[j]]=d[i] + 1

print(d[m])