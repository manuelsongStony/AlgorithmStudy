recruits=[[1, 50], [1, 60], [3, 70], [0, 65], [2, 50], [1, 90]]
s1,s2=2,70
result=[1, 90]


recruits,s1,s2=[[0, 0], [0, 0], [0, 0], [0, 3], [1, 2], [2, 0], [2, 0], [2, 1]],2,4
recruits,s1,s2=[[0, 0], [0, 0], [0, 0], [2, 0], [0, 2], [1, 1]],2,2
recruits,s1,s2=[[0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 3], [3, 2]],2,3

size_of_rec=len(recruits)
j_counter=0
ex_senior_array=[]
for ele in recruits:
    if ele[0]<s1 and ele[1]<s2:
        j_counter+=1
    else:
        ex_senior_array.append(ele)


#ex_senior_array.sort(key =lambda x:(x[1]),reverse=True)
ex_senior_array.sort(key =lambda x:(x[1]))
if j_counter>len(ex_senior_array):
    j_counter=len(ex_senior_array)

answer=[]
answer.append(ex_senior_array[j_counter-1][0])
answer.append(ex_senior_array[j_counter-1][1])


ex_senior_array.sort(key =lambda x:(x[0]))
answer2=[]
answer2.append(ex_senior_array[j_counter-1][0])
answer2.append(ex_senior_array[j_counter-1][1])


print(answer[0])
print(answer[1])
print(answer2[0])
print(answer2[1])

if (answer==answer2):
    print (answer2)