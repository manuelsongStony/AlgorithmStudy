def solution(survey, choices):
    answer = ''
    table=[[0,0,0,0],[0,0,0,0]]

    for i in range(len(survey)):

        if survey[i]=='RT':
            if choices[i]<=4:
                table[0][0]+=(4-choices[i])
            else:
                table[1][0] += (choices[i]-4)
        elif survey[i]=='TR':
            if choices[i]<=4:
                table[1][0]+=(4-choices[i])
            else:
                table[0][0] += (choices[i]-4)

        elif survey[i]=='CF':
            if choices[i]<=4:
                table[0][1]+=(4-choices[i])
            else:
                table[1][1] += (choices[i]-4)
        elif survey[i]=='FC':
            if choices[i]<=4:
                table[1][1]+=(4-choices[i])
            else:
                table[0][1] += (choices[i]-4)

        elif survey[i]=='JM':
            if choices[i]<=4:
                table[0][2]+=(4-choices[i])
            else:
                table[1][2] += (choices[i]-4)
        elif survey[i]=='MJ':
            if choices[i]<=4:
                table[1][2]+=(4-choices[i])
            else:
                table[0][2] += (choices[i]-4)

        elif survey[i]=='AN':
            if choices[i]<=4:
                table[0][3]+=(4-choices[i])
            else:
                table[1][3] += (choices[i]-4)

        elif survey[i]=='NA':
            if choices[i]<=4:
                table[1][3]+=(4-choices[i])
            else:
                table[0][3] += (choices[i]-4)


    if table[0][0]>=table[1][0]:
        answer=answer+'R'
    else:
        answer = answer + 'T'

    if table[0][1]>=table[1][1]:
        answer=answer+'C'
    else:
        answer = answer + 'F'

    if table[0][2]>=table[1][2]:
        answer=answer+'J'
    else:
        answer = answer + 'M'

    if table[0][3]>=table[1][3]:
        answer=answer+'A'
    else:
        answer = answer + 'N'




    return answer



survey=["AN", "CF", "MJ", "RT", "NA"]
choices=[5, 3, 2, 7, 5]

print(solution(survey, choices))