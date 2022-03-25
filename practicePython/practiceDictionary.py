rec_dict={}
a="manuel song"
b="theo seo"

print((a.split())[0])
print((a.split())[1])

rec_dict[(a.split())[0]]=[]
rec_dict[(b.split())[0]]=[]

rec_dict[(a.split())[0]].append((a.split())[1])

for i in rec_dict:
    print(rec_dict[i])


