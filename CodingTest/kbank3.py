money = 8
re_roll = 5
price=[("a", 1), ("b", 2), ("c", 3), ("d", 4)]

array = [["a", "d", "d", "b"], ["c", "b", "b", "b"], ["c", "d", "a", "b"], ["b", "c", "a", "a"]]
"""
리롤 1번했을때 살수있는개수 2번했을때 3번했을때,4번~ n 번 개수 의max값
"""

count_array=[0]*len(price)
compare=[0]*len(array)

for i in range(len(array)):
    cash=money-5*i
    counter=0

    for shape in array[i]:
        index=-1
        for j in range(len(price)):
            if price[j][0]==shape:
                index=j
                break

        count_array[j]+=1


    for k in range(len(price)):
        for _ in range(count_array[k]):
            cash -= price[k][1]
            if cash>=0:
                counter+=1
            else:
                break

        if cash<0:

            break

    compare[i] = counter
print(compare)





"""
1=a -> 1
2=a or b -> 1
3= a,b -> 2
4=a,b ->2
5=a,b ->2
6=a,b or a,d, or b,d->2
7=a,b,d or ->3
8=a,b,d->3
9=a,b,d->3
10=a,b,d or a,b,|,b->3 
11=a,b,d,d or a,b,|,b->4
12=a,b,d,d(11) or a,b,|,b,b(12) ->4
13=a,b,d,d(11) or a,b,|,b,b(12) ->4
14=a,b,d,d(11) or a,b,|,b,b,b(14) ->5
15=a,b,d,d(11) or a,b,|,b,b,b(14) ->5
16=a,b,|,b,b,b(14) ->5
17=a,b,|c,b,b,b(17) ->6
18=a,b,d|b,b,b(18) or a,b,|c,b,b,b(17) ->6
19=a,b,d|b,b,b(18) or a,b,|c,b,b,b(17) ->6
20=
"""

