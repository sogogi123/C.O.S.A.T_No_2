def solution(s):
#     n_dic={0:"zero", 1:"one", 2:"two",3:"three",4:"four",
# 5:"five",6:"six",7:"seven",8:"eight", 9:"nine"}
    nlist= ["zero","one","two","three","four",
"five","six","seven","eight", "nine"]
    for i, j in enumerate (nlist): 
        if j in s:
            s =s.replace(j, str(i))
        
    answer = int(s)
    return answer
# s=input()
# print(solution(s))