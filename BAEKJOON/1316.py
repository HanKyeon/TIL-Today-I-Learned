'''
그룹 단어 체커

aabbbccb 그룹 단어 아님
그룹단어 갯수 찾아주삼

입력
단어갯수n 100이하저연수
n개 단어 소문자로만 중복x 최대길이 100
'''
c = 0 # 카운트
for testcase in range(1, int(input())+1): # 입력 받은 만큼 반복
    s = input() # 받은 문자열
    sls = list(set(s)) # 문자열에 있는 단어들
    tf = True # 판별
    for i in sls: # 세트를 돌면서
        b = [idx for idx, v in enumerate(s) if v == i] # 그 문자열 인덱스 뽑아서
        if len(b) == 1: # 길이가 1이면 pass
            continue
        for j in range(1, len(b)): # 1 아니면
            if b[j] != b[j-1]+1: # 앞의 인덱스와 뒤의 인덱스가 연속인지 판별
                tf = False 
                break # 아니라면 바로 끝내면 됨.
    if tf:
        c += 1
print(c)
