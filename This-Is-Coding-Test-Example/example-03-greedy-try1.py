binary_number = input()



zero_low_case=0
one_low_case=0

if int(binary_number[0])==0:
    continue_search = 0
    zero_low_case +=1
else:
    continue_search = 1
    one_low_case += 1


for i in binary_number:
    if continue_search == 1:
        if int(i)==1:
            continue
        else:
            zero_low_case+=1
            continue_search=0
    else:
        if int(i) == 0:
            continue
        else:
            one_low_case += 1
            continue_search=1

if zero_low_case>one_low_case:
    print(one_low_case)
else:
    print(zero_low_case)