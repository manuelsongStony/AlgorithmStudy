import copy


def solution(id_list, report, k):
    rec_dic = {}
    answer_dictionary = {}

    for id in id_list:
        rec_dic[id] = []
        answer_dictionary[id] = 0

    for r in report:
        sender = (r.split())[0]
        receiver = (r.split())[1]

        if sender not in rec_dic[receiver]:
            rec_dic[receiver].append(sender)

    for rec in rec_dic:
        if len(rec_dic[rec]) >= k:

            for ele in rec_dic[rec]:
                answer_dictionary[ele] = answer_dictionary[ele] + 1

    answer = []
    for ans in answer_dictionary:
        answer.append(answer_dictionary[ans])

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],2))