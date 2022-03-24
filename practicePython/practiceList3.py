print(x for x in range(4))
print([x for x in range(4)])

t=[x for x in range(4)]

for x in t[1:-1]:
    print(x,end=' ')

print()

for x in t[0:-1]:
    print(x,end=' ')