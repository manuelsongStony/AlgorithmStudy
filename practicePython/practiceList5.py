
i=[1,2]
k=[2,1]
j=[[1,2],[2,3]]
print(i in j)
print(k in j)

t=list("Manuel Song")

t[::-1] #  from index 0 to index len(t)
print(t[::1])
print(t[::2])
print(t[3:0:-1])
print(t[0:3:-1])
print(t[0:-5:-1])

print(t[13:-10:-1])
#['g', 'n', 'o', 'S', ' ', 'l', 'e', 'u', 'n']


print(t[3:-5:-1])
#[]

print(t[3:-10:-1])
#['u', 'n'] u~a

print(t[3:-12:-1])
#['u', 'n', 'a', 'M']


print(t[10::-1])
print(t[len(t):-len(t)-1:-1])
print(t[::-1])


list1 = ['1', '2', '3']
str1 = ' '.join(list1)
str2 = ''.join(list1)
print(str1)
print(str2)