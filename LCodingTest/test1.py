import re


def solution(logs):
    answer = 0
    #print(len(logs))
    #print(logs[0].split()[3])
    p = re.compile('team_name : [a-zA-Z]+ application_name : [a-zA-Z]+ error_level : [a-zA-Z]+ message : [a-zA-Z]+')


    m = p.match("python")

    if len(logs)>100:
        return answer

    for log in logs:

        content=log.split()
        m = p.match(log)
        if not m:
            continue
        if len(content)!=12:
            continue
        elif len(log)>100:
            continue
        elif content[0]!="team_name":
            continue
        elif content[1]!=':':
            continue
        elif not content[2].isalpha():
            continue
        elif content[3]!="application_name":
            continue
        elif content[4]!=':':
            continue
        elif not content[5].isalpha():
            continue
        elif content[6]!="error_level":
            continue
        elif content[7]!=':':
            continue
        elif not content[8].isalpha():
            continue
        elif content[9]!="message":
            continue
        elif content[10]!=':':
            continue
        elif not content[11].isalpha():
            continue

        answer+=1

    return len(logs)-answer

logs1=["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]
logs2=["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]

print(solution(logs1))
print(solution(logs2))
