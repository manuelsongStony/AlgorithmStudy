array=[15,11,4,8,5,2,4]
array_modify=[[15,1],[11,1],[4,1],[8,1],[5,1],[2,1],[4,1]]
count=0

n=len(array)

for i in range(n-2,-1,-1):
    temp = 0
    for j in range(i+1,n):
        if array_modify[i][0]>array_modify[j][0]:
            temp=max(temp,array_modify[j][1]+1)
        else:
            continue
    array_modify[i][1]=temp

array_modify.sort(key=lambda x:-int(x[1] ))

print(n-array_modify[0][1])


        #array_modify[i][0]=max value of array_modify[?][1] that array_modify[?][0] is less than array_modify[i][0] +1
