def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report = set(report)
    report_dic={}
    id_dic = {}
    for i in report:
        a,b = i.split(" ")
        if b not in report_dic:
            report_dic[b]= 1
        else:
            report_dic[b]+=1
        if a not in id_dic:
            id_dic[a] = b
        else:
            if b not in id_dic[a]:
                id_dic[a]+= [b]
    for id, n in report_dic.items():
        if n >=k:
            for u1,u2 in  id_dic.items():
                if id in u2:
                    answer[id_list.index(u1)] +=1

    return answer
a= ["muzi", "frodo", "apeach", "neo"]
b= ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
c=2
print(solution(a,b,c))