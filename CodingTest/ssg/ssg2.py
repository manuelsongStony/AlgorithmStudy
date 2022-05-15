"""
logs=["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80",
      "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

"""
logs=["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100",
      "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100",
      "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100",
      "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]

dic_id={}
id_set=set()

for ele in logs:
    #array=list(map(int,ele.split()))
    array = list( ele.split())
    if array[0] in id_set:
        dic_id[array[0]][array[1]]=array[2]
    else:
        id_set.add(array[0])
        dic_id[array[0]]={}
        dic_id[array[0]][array[1]] = array[2]


print(dic_id)

answer_set=set()
id_list=list(id_set)


for i in range(len(id_list)):
    for j in range(i+1,len(id_list)):
        j_keys=dic_id[id_list[j]].keys()

        counter=0
        for key in dic_id[id_list[i]].keys():
            if key in j_keys:
                if dic_id[id_list[i]][key]==dic_id[id_list[j]][key]:
                    counter +=1

        if counter >=5:
            answer_set.add(id_list[i])
            answer_set.add(id_list[j])


answer=list(answer_set)
answer.sort()
if answer==[]:
    answer= ["None"]

print(answer)
"""
dic_num[1]=10
print(dic_num)
print(dic_num[2]==None)"""
