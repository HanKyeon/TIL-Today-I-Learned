'''
수행 시간

특정 임무를 수행하기 위해 n개로 이루어진 시스템.
1. 1번부터 n번까지 번호. 계급과 동작속도. 모두 양정수
2. i번과 j번 간 전송 시간은 (i-j)**2
3. 각 n개의 컴퓨터 계급은 c1 c2 cn이다. 수어진 컴퓨터 계급을 오름차순 정렬 했을 경우, cj - c(j-1)은 1이하이다.
4. 제일 낮은 계급의 컴퓨터를 제외한 컴퓨터들은 자신보다 한 단계 낮은 계급의 모든 컴퓨터에게 정보를 전달 받아야만 동작을 시작 할 수 있다. 이 때 동작을 시작하기 위해서는 그 컴퓨터의 동작 속도 만큼의 시간이 소요된다.
5. 제일 낮은 계급의 컴퓨터는 전달 받을 정보가 없다. 따라서 시스템 시동과 동시에 동작한다.
6. 모든 컴ㅍ터가 동작을 마치면 c+1 계급을 가진 모든 컴퓨터에 정보를 전달 후 종료된다.
7. 모든 컴퓨터가 동작을 마치고 종료되면 임무수행이 끝난다.
8. 가장 낮은 계급은 1

시스템에 정보가 주어졌을 때, 임무 수행이 끝날 때까지 걸린 시간을 구해라.

입력
컴퓨터 갯수 n.
n개줄 계급과 동작속도 t 제시.

출력
답 출력
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tmz = [0] * (n+1)
lvl = [[] for _ in range(n+1)]
mxlvl = 0
for i in range(1, n+1):
    lv, tm = map(int, input().rstrip().split())
    lvl[lv].append(i)
    tmz[i] = tm
    if lv > mxlvl:
        mxlvl = lv
dp = tmz[:]
nlv = 2
q = deque(lvl[1])
while q and nlv <= mxlvl:
    num = q.popleft()
    for i in lvl[nlv]:
        dp[i] = max(dp[i], dp[num]+(num-i)**2+tmz[i])
    if not q:
        q = deque(lvl[nlv])
        nlv += 1

print(max(dp))











# ans= 0
# svdj = 0
# for i in range(1, mxlvl):
#     val = 0
#     for j in lvl[i]:
#         svdj = max(svdj, tmz[j])
#         for k in lvl[i+1]:
#             val = max(val, tmz[j]+(j-k)**2)
#     svdj = val
#     ans += val
# print(ans)