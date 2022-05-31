n,c=5,3
distance=[1,2,8,4,9]
distance.sort()

# 두점사이의 거리 어레이로 그다음 c-1 개 골라서 솔팅 솔팅
# 나누기 c-1 한다음 가장작은거 찾기?


difference=[]

full_length= distance[len(distance)-1]-distance[0]
divided_length= full_length//(c-1)

for i in range(0,len(distance)-1):
    difference.append(distance[i+1]-distance[i])

final_array=[]
index=0
account=0
while index<len(difference):
    if account>=c-1:
        break

    number=difference[index]

    while number<divided_length:
        if index == len(difference)-1:
            break
        index += 1
        number+=difference[index]

    number-=difference[index]

    if abs((number+difference[index])-divided_length)>abs(number-divided_length):
        final_array.append(number)
        account+=1
    else:
        final_array.append(number+difference[index])
        index+=1
        account+=1




print(final_array)
final_array.sort()
print(final_array[0])