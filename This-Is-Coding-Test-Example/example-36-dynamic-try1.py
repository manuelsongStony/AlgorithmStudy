import copy
a="sunday"

b="saturday"
#6,5 | 6,6
#answer should be 4
a2="cat"
b2="cut"

a_array=list(a)
b_array=list(b)




def get_the_edit_count(a,b,count):
    if a==b:
        return count
    else:
        index=0
        smaller_value=min(len(a),len(b))
        for _ in range(smaller_value):
            if a[index]==b[index]:
                index+=1
            else:
                break;

        if index==len(a) or index==len(b):
            if len(a)>len(b):
                count+=len(a)-len(b)
                return count
            else:
                count += len(b)-len(a)
                return count


        copy_temp=copy.deepcopy(a)
        copy_temp.pop(index)
        do_remove = copy_temp

        copy_temp = copy.deepcopy(a)
        copy_temp.insert(index,b[index])
        do_insert = copy_temp

        copy_temp = copy.deepcopy(a)
        copy_temp.pop(index)
        copy_temp.insert(index,b[index])
        do_replace = copy_temp

        temp1=get_the_edit_count(do_remove,b,count+1)

        temp2=get_the_edit_count(do_insert, b, count + 1)

        temp3=get_the_edit_count(do_replace, b, count + 1)

        return min(temp1,temp2,temp3)


print(get_the_edit_count(a_array,b_array,0))

