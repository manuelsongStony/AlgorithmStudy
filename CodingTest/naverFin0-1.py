"""
recruits=[[1, 50], [1, 60], [3, 70], [0, 65], [2, 50], [1, 90]]
s1,s2=2,70
result=[1, 90]
"""

#recruits,s1,s2=[[0, 0], [0, 0], [0, 0], [0, 3], [1, 2], [2, 0], [2, 0], [2, 1]],2,4
#recruits,s1,s2=[[0, 0], [0, 0], [0, 0], [2, 0], [0, 2], [1, 1]],2,2

recruits,s1,s2=[[0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 3], [3, 2]],2,3

size_of_rec=len(recruits)
j_counter=0
ex_senior_array=[]
for ele in recruits:
    if ele[0]<s1 and ele[1]<s2:
        j_counter+=1
    else:
        ex_senior_array.append(ele)

senior_size=len(ex_senior_array)


answer=[]
for i in range(101):
    for j in range(101):
        temp_jocounter=j_counter
        expert_counter = 0
        temp_senior_size=senior_size
        for ele in recruits:
            if ele[0]>=i and ele[1]>=j:
                if ele[0]>=s1 or ele[1]>=s2:
                    temp_senior_size-=1
                    expert_counter+=1
                else:
                    temp_jocounter-=1
                    expert_counter += 1


        if temp_senior_size>expert_counter and temp_jocounter>temp_senior_size and expert_counter>0:
            answer.append((i,j))

max_val=0
max_val_array=[]

print(answer)

for ele in answer:
    if ele[0]+ele[1]>max_val:
        max_val_array=[]
        max_val_array.append(ele)
    if ele[0]+ele[1]==max_val:
        max_val_array.append(ele)

max_val_array.sort(key=lambda x:(x[0]))

print(max_val_array)