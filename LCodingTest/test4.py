def recursive(arr,num,i):
    if arr[i]>num:
        return i
    else:
        need=arr[i]+arr[i+1]-brr[i]
        recursive(arr,num-arr[i],i+1)


if sum(brr[0:i])>sum(arr[0:i])

"""
def solution(arr, brr):
    answer=0

    for i in range(len(arr)-1):
        if arr[i] ==brr[i]:
            continue
        else:
            if arr[i]>brr[i]:
                gap = arr[i] - brr[i]
                arr[i]-=gap
                arr[i+1]+=gap

                answer+=1

            else:
                gap =  brr[i]-arr[i]

                if arr[i+1]-gap >=1:
                    arr[i] +=  gap
                    arr[i + 1] -= gap

                    answer += 1

                else:
                    arr[i + 2]-brr[i + 1]-brr[i]

                    else:arr[i + 3]-brr[i + 2]-brr[i+1]-brr[i]
                    
















    return answer


"""


arr=[3, 7, 2, 4]
brr=[4, 5, 5, 2]

#print(solution(arr, brr))
print(recursive(arr, 2, 0))