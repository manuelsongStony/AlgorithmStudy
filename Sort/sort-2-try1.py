n = int(input())
li=[]
for i in range(n):
    name, score= input().split()
    score=int(score)
    li.append((name,score))

def compare_score(e):
    return e[1]

result = sorted(li, key=compare_score)

for i in result:
    print(i[0],end=' ')
