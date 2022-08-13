'''
방배정

같은 학년, 같은 성별
단일방 가능
한 방에 배정 가능한 최대 인원수 K

입력
학생수n 방당최대인원k n,k는 1이상 1000이하
성별여0남1 학년1~6

출력
방수
'''
# 입력
n, k = map(int, input().split())
# 처리
sts = [[0]*6 for _ in range(2)]
r = 0
for i in range(n):
    se, gr = map(int, input().split())
    sts[se][gr-1] += 1
for stu in sts :
    for i in stu :
        if i % k == 0:
            r += i//k
        else :
            r += i//k + 1
# 출력
print(r)
