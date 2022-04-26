p1="(())()"
p2=")("
p3="()))((()"

def is_balanced(s):
    counter=0
    for i in range(len(s)):
        if s[i]=="(":
            counter+=1
        else:
            counter -= 1

        if counter<0:
            return False
    return True


def covert_balacned(s):
    result="("
    array=list(s)
    for i in range(1,len(s)-1):
        if array[i] == "(":
            array[i]=")"
        else:
            array[i] = "("

    for i in range(1,len(s)-1):
        result = result + array[i]

    result=result+")"
    return result




def make_balanced(s):
    if s=="":
        return ""


    answer=''
    open_counter=0
    close_counter=0
    index=0
    for i in range(len(s)):
        if s[i]=="(":
            open_counter+=1
        else:
            close_counter+=1

        if open_counter==close_counter:
            index=i
            break

    u=s[0:index+1]
    v=s[index+1:]

    if is_balanced(u):
        answer=answer+u
    else:
        u=covert_balacned(u)
        answer = answer + u

    answer=answer+make_balanced(v)
    return answer


print(make_balanced(p3))
