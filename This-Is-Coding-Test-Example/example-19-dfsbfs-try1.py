import copy


def do_equation(n,count,result,result_array,operators):
    if count==n-1:
        result_array.append(result)
        return

    if operators[0]>0:
        temp_result=copy.deepcopy(result)
        temp_result=temp_result+"+"
        temp=copy.deepcopy(operators)
        temp[0]-=1
        do_equation(n, count+1, temp_result, result_array, temp)
    if operators[1]>0:
        temp_result = copy.deepcopy(result)
        temp_result = temp_result + "-"
        temp = copy.deepcopy(operators)
        temp[1] -= 1
        do_equation(n, count + 1, temp_result, result_array, temp)
    if operators[2]>0:
        temp_result = copy.deepcopy(result)
        temp_result = temp_result + "*"
        temp = copy.deepcopy(operators)
        temp[2] -= 1
        do_equation(n, count + 1, temp_result, result_array, temp)
    if operators[3]>0:
        temp_result = copy.deepcopy(result)
        temp_result = temp_result + "/"
        temp = copy.deepcopy(operators)
        temp[3] -= 1
        do_equation(n, count + 1, temp_result, result_array, temp)


"""
n=2
number_array=[5,6]
operators=[0,0,1,0]



n=3
number_array=[3,4,5]
operators=[1,0,1,0]
"""

n=6
number_array=[1,2,3,4,5,6]
operators=[2,1,1,1]

max_answer=0
min_answer=int(10e9)


result=""
result_array=[]
counter=0

do_equation(n,counter,result,result_array,operators)

answer_array=[]


for eq in result_array:
    result_of_equaltion=number_array[0]
    for i in range(n-1):
        if eq[i]=="+":
            result_of_equaltion += number_array[i+1]
        elif eq[i]=="-":
            result_of_equaltion -= number_array[i+1]
        elif eq[i]=="*":
            result_of_equaltion *= number_array[i+1]
        else :
            result_of_equaltion =int(result_of_equaltion/ number_array[i+1])

    answer_array.append(result_of_equaltion)

print(result_array)
print(max(answer_array),min(answer_array))
