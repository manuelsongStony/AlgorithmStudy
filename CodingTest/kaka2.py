
def solution(queue1, queue2):
    answer = 0


    total_queue = queue1 + queue2
    total = sum(total_queue)

    if total % 2 != 0 or max(total_queue) > total // 2 :
        return -1



    target=total//2


    right=0
    left=0

    sum_number=0

    go_right_flag=True

    array=[]
    while True:

        if go_right_flag:
            temp=total_queue[right]

            if sum_number + temp == target:

                array.append((left,right))

                sum_number += temp
                right += 1

            elif sum_number + temp < target:

                sum_number += temp
                right += 1

            else:
                right -= 1
                left -= 1
                go_right_flag=False

        else:

            temp = total_queue[left]

            if sum_number + temp == target:
                array.append((left,right))

                sum_number += temp
                left -= 1

            elif sum_number + temp < target:
                sum_number += temp
                left -= 1

            else:

                if right > 0:
                    sum_number -= total_queue[right]
                    right -= 1
                else:

                    break



    print(array)



    if len(array)==0:
        answer=-1
    else:
        min_v=9e10
        for ele in array:
            if ele[0]==0:
                min_v=0
                break

            min_v=min(min_v,len(queue1)+ele[0]+ele[1]+1)



        answer=min_v
    return answer

"""
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

#queue1 = [4, 2, 7, 2]
#queue2 = [3, 6, 5, 1]
"""
queue1 =[1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
"""
queue1 =[1, 1]
queue2 =[1, 5]
"""

print(solution(queue1, queue2))
