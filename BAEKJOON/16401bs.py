'''
과자 나눠주기

최대한 긴 막대과자 나눠주려 한다.
과자를 합칠 수는 없고, 나눌 수는 있다. 막대과자의 길이는 야으이 정수

입력
조카의 수 1이상 100만이하, 과자의 수 1이상 100만이하 M, N 제시.
둘째 줄에 과자 N개의 길이가 공백 구분 제시. 과자 길이는 1이상 10억 이하.

출력
조카 1명에게 줄 수 있는 막대 과자의 최대 길이 출력.
모든 조카에게 같은 길이의 막대과자를 줄 수 없다면 0 출력.
'''
import sys
input = sys.stdin.readline

def 이분탐색(st, en):
    global ans, m, n, nl
    while st <= en: # 시작점이 작거나 같을 동안
        # print(st, en)
        mid = (st + en) // 2 # 중앙값
        if mid == 0: # 0으로 못나누고, 0까지 왓다는건 못준다는 것.
            ans = 0
            break
        # print(mid)
        ret = 0 # 몇명 줄 수 있는지
        for i in nl: # 막대기 돌면서
            ret += i//mid # 몇개 줄 수 있나 더해줌

        if ret == m and ans < mid: # m과 같고, 기존 저장된 ans보다 길다면
            ans = mid # 답 저장

        if ret < m: # 결과가 m보다 작다면
            en = mid-1 # 끝점 올려주고
        elif ret >= m: # 크거나 같으면
            ans = mid # 일단 답 저장해주고
            st = mid+1 # 시작점 늘리기

m, n = map(int, input().split())
nl = list(map(int, input().rstrip().split()))
ans = 0
이분탐색(0, max(nl))
print(ans)

'''
11 3
1 1 20
정답 2가 나와야 함
'''