#s=input()
s='abcabcabcabcdededededede'

array=[x for x in s]

result=10e9
for i in range(1,(len(s)//2) +1):
    pressed_string=''
    j=0
    while j<len(s):
        count=1
        for k in range(j,len(s),i):
            if s[k:k+i]==s[k+i:k+i+i]:
                count+=1
            else:
                break;


        if count==1:

            pressed_string = pressed_string + s[j:j+i]
            j = j + i
        else:
            pressed_string = pressed_string + str(count) + s[j:j+i]
            j=j+count*i

    print(pressed_string)
    result=min(result,len(pressed_string))

print(result)
#print([x for x in s])
#print(''.join(array))