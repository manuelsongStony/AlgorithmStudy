
#array1=[[1,2],[1,4],[4,2],[2,7],[7,1]]

array=[]
while True:
    x,y=map(int, input().split())
    if x==0 and y==0:
        break
    else:
        temp=[]
        temp.append(x)
        temp.append(y)
        array.append(temp)

web_set=set()
for ele in array:
    web_set.add(ele[0])
    web_set.add(ele[1])

n=len(web_set)

temp_set=set()
for i in range(1,n+1):
    temp_set.add(i)

dset_change=temp_set.difference(web_set)
dset=web_set.difference(temp_set)
conjunction_set=web_set&temp_set


value_list=list(dset_change)
key_list=list(dset)
conjunction_list=list(conjunction_set)


web_dictionary={}

for i in range(len(key_list)):
    web_dictionary[key_list[i]]=value_list[i]

for i in conjunction_set:
    web_dictionary[i] = i

graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

for ele in array:
    graph[web_dictionary[ele[0]]][web_dictionary[ele[1]]]=1

for i in range(1,len(graph)):
    graph[i][i]=0


for inter in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            graph[x][y] = min(graph[x][y], graph[x][inter] + graph[inter][y])

count=0
for col in range(1, n + 1):
    for row in range(1, n + 1):
       count+=graph[col][row]



numerator=n*n-n



print(round(count/numerator,2))





