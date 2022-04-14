#s=input()
s="K1KA5CB7"
sum=0
array=[]
for i in s:
    if i.isalpha():
        array.append(i)
    else:
        sum+=int(i)

array.sort()
string_sum=''.join(array)
print(string_sum+str(sum))