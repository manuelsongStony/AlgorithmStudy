#food_times=[3, 1, 2]
#k=5

food_times=[4,3, 1, 2]
k=5


"""
n=len(food_times)
zero_counter= food_times.count(0)
after_zero_n=n-zero_counter

if sum(food_times)<k:
    answer=-1
    #return answer
    print(answer)
    
"""
answer=-1
food_times_tuple=[]

for i in range(len(food_times)):
    food_times_tuple.append((food_times[i],i))

food_times_tuple.sort()

sum=0

for i in range(len(food_times)):

    if 0>k-(food_times_tuple[i][0]-sum)*(len(food_times)-i):#0이 아닌것중 제일작은수
        if i==len(food_times)-1:
            answer=food_times_tuple[len(food_times)-1][1]+1
            break

        tuples=[]
        for j in range(i,len(food_times)):
            tuples.append(food_times_tuple[j])
        tuples.sort(key=lambda x: x[1]) # 솔팅
        t=k%(len(tuples))
        answer=tuples[t][1] +1 #원래번호 #나머지솔티드리스트, 자릿수 1
        break
    else:
        k-=(food_times_tuple[i][0]-sum)*(len(food_times)-i)
        sum=food_times_tuple[i][0]

print(answer)