def solution(record):
    answer = []
    id_set = set()
    id_dic = {}

    for sen in record:
        sen_list = list(sen.split())

        if len(sen_list) > 2:
            id_set.add(sen_list[1])
            id_dic[sen_list[1]] = sen_list[2]
            """
            if sen_list[0] == "Change":
                id_dic[sen_list[1]] = sen_list[2]
            else:
                if sen_list[1] not in id_set:
                    id_set.add(sen_list[1] )
                    id_dic[sen_list[1]] = sen_list[2]
            """
    #print(id_set)
    #print(id_dic)
    for sen in record:
        sen_list = list(sen.split())
        if sen_list[0] == "Enter":
            answer.append(id_dic[sen_list[1]]+"님이 들어왔습니다.")
        elif sen_list[0] == "Leave":
            answer.append(id_dic[sen_list[1]] + "님이 나갔습니다.")



    return answer





record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
#["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(record))