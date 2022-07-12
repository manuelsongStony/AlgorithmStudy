#text = input().strip()
input_s="Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.[ some_paper_a, some_paper_b ] We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.[ some_book_a, some_paper_a ] We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. [ some_book_b ]"
input_ss="Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.[ some_paper_a, some_paper_b ] We explicitly"
#print(string_A, end='')
#print(input_s)
#print(list(string_A))
answer=""
array=list(input_s)
ref_array=[]
i=0
while i <len(array):
    if array[i]=="[":
        answer=answer+array[i] # add "["
        temp_string=""
        count=0
        for j in range(i+1,len(array)):
            count += 1
            if array[j] =="]":
                break
            else:

                temp_string=temp_string+array[j]

        temp_result = [x.strip() for x in temp_string.split(',')]

        number=[]
        for k in range(len(temp_result)):
            if temp_result[k] not in ref_array:
                ref_array.append(temp_result[k])
            number.append(ref_array.index(temp_result[k]) + 1)


        number.sort()


        for t in range(len(number)):
            answer = answer + " " + str(number[t])
            if t == len(temp_result) - 1:
                answer = answer + " "

            else:
                answer = answer + ","

        i=i+count


    else:



        answer=answer+array[i]
        i+=1


print(answer)


for i in range(len(ref_array)):
    ref_temp_string = "["
    ref_temp_string = ref_temp_string+str(i+1)
    ref_temp_string = ref_temp_string + "] "
    ref_temp_string = ref_temp_string + ref_array[i]

    print(ref_temp_string)
