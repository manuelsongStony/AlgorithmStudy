def solution(s):
    array = []
    array2=[]
    if len(s)==1:
        return 1
    for i in range(1, len(s)// 2+1):
        compare = s[0:i]
        count = 1
        temp = ""
        j=i
        while j<len(s):
            if s[j:j + i] == compare:
                count += 1
            else:
                temp = temp + compare if count == 1 else temp + str(count) + compare
                compare = s[j:j + i]
                count = 1
            j+=i

        if count !=1:
            temp=temp + str(count) + compare
            if j!=len(s):
                temp = temp + s[j - i:]
        else:
            temp=temp+s[j-i:]

        #array2.append(temp)
        array.append(len(temp))

    answer = sorted(array)[0]
    return answer

s="aabbaccc"
s="a"
print(solution(s))