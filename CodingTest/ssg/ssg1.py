
def solution(v,a,b):


    answer=0
    v.sort(reverse=True)

    if len(v)==1:
        return v[0]//a
    if a==b:
        return v[len(v)-1]//a

    while v[0]>=a and v[len(v)-1]>=b:

        """
        v=[x-b for x in v]
        v[0] = v[0] +b - a
        answer+=1
        v.sort(reverse=True)
        
        """
        k=(v[0]-v[1])//(a-b)

        if k==0:
            answer+=v[0]//a
            return answer

        v = [x - k*b for x in v]
        v[0] = v[0] + k*b - k*a
        answer += k
        v.sort(reverse=True)

    return answer






#v, a, b = [4, 5, 5], 2, 1
v,a,b=[4,4,3],2,1

v,a,b=[10,7,4],3,1

#7 6 3

#4 5 2 ->5 4 2

#2 3 2 ->3 2 2

#0 1 1

print(solution(v,a,b))
