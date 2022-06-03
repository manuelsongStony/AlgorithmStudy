#틀림 예시 문제 제대로 읽고 틀린예시 몇개 찾아보기
n=4
array=[10,10,15,15,20,40,50]
#20+35+50=105
#20+30+50=100
array.sort
sum=10
result=0
for i in range(1,len(array)):
    sum+=array[i]
    result+=sum

print(result)