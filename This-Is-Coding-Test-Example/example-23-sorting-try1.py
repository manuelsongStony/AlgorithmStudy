import functools

n = 12
array = [["Junkyu", 50, 60, 100],
         ["SangKeun", 80, 60, 50],
         ["Sunyoung", 80, 70, 100],
         ["Soong", 50, 60, 90],
         ["Haebin", 50, 60, 100],
         ["Kangsoo", 60, 80, 100],
         ["Donghyuk", 80, 60, 100],
         ["Sei", 70, 70, 70],
         ["Wonseob", 70, 70, 90],
         ["Sanghyun", 70, 70, 80],
         ["nsj", 80, 80, 80],
         ["Taewhan", 50, 60, 90],
         ]


def comparer(x, y):
    if x[1]==y[1]:
        if x[2]==y[2]:
            if x[3] == y[3]:
                if x[0]<y[0]:
                    return -1
                else:
                    return 1
            else:
                return  y[3]-x[3]
        else:
            return x[2] - y[2]
    else:
        return y[1]-x[1]

print(sorted(array, key=functools.cmp_to_key(comparer)))
