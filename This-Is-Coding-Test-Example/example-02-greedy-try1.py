#[그리디 -실전 2]곱하기 혹은 더하기

array=list(map(int,input()))

#print(array[1])

result=0
for num in array:
    if result==0:
        result+=num
        continue
    if num==1 or num==0:
        result+=num
    else:
        result*=num

print(result)

