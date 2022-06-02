# import sys
# # 아이디의 길이는 3자 이상 15자 이하
# # 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# # 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
# new_id = sys.stdin.readline().strip('\n')
def solution(new_id):
    # 1
    one =new_id.lower()
    # 2
    two =''
    for word in one:
        if word.isalnum() or word in'-_.':
            two+=word
    # 3
    while '..' in two:
        two = two.replace('..','.')
    three = two

    # 4
    if three[0]=='.' and len(three)>1:
        four = three[1:]
    else:
        four = three

        if three[-1]=='.':
            four = three[:-1]
        else:
            four = three
    # 5
    if four=='':
        five ='a'
    else:
        five = four
    # 6
    if len(five)>=16:
        six =five[:15]
        if six[-1]=='.':
            six = six[:-1]
    else:
        six = five

    # 7
    while len(six)<3:
        six += six[-1]
    seven = six
    answer = seven
    return answer

