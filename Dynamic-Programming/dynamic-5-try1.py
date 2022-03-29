#그리디 -01 -모험가 길드
n=int(input())
array=list(map(int, input().split()))

sorted_array=sorted(array)

answer=0

max=0
counter=0

for i in range(n):
    max=sorted_array[i]
    counter+=1

    if max==counter:
        answer+=1
        counter=0


print(answer)
#print(sorted_array)