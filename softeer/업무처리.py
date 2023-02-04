'''
업무 처리

부서 업무 조직 와전 이진 트리.
부서장이 루트이고 각 직원은 좌우 부하 가짐. 부하 없는게 말단.
모든 말단은 부서장까지의 거리가 동일하다. 조직도 트리의 높이는 H이다.

업무는 R일 동안 진행.
말단 직원들만 K개의 순서가 정해진 업무를 가지고 있다. 각 업무는 업무 번호가 존재.
각 날짜에 남은 업무가 있는 경우, 말단 직원은 하나의 업무를 처리.
타 직원도 대기 업무가 있는 경우ㅡ 업무가 올라온 순서대로 하나 처리해서 상사에게 올린다.
단, 홀수 번째 날짜에는 좌부하, 짝수에는 우부하 업무 처리.
부서 조직과 대기하는 업무를 입력 받아 처리가 완료된 업무들의 번호 합을 계산해라.

트리 높이는 최대 10 업무 갯수 최대 10, 업무 최대 진행 날짜 1000

h, k, r 제시. 조직도 높이, 말단 대기 업무 갯수 k, 업무 진행 되는 날짜 수 r
말단 직원에 대해 대기하는 업무가 순서대로 제시. 최좌측 말단 직원부터 순서대로 제시.

출력
완료된 업무들의 번호 합을 정수로 출력
'''
import sys
input = sys.stdin.readline

h, k, r = map(int, input().rstrip().split())
tree = [[[], []] for _ in range(2**(h+1)-1)]

for i in range(2**h-1, 2**(h+1)-1):
    li = list(map(int, input().rstrip().split()))
    flag = False
    while li:
        tree[i][flag].append(li.pop(0))
        flag = not flag

ans = 0
for day in range(1, r+1):
    q = [0]
    holzzak = (day+1)%2
    if tree[0][holzzak]:
        ans += tree[0][holzzak].pop(0)
    while q:
        nod = q.pop(0)
        ln, rn = nod*2+1, nod*2+2
        if ln < len(tree):
            q.append(ln)
            if tree[ln][holzzak]:
                tree[nod][0].append(tree[ln][holzzak].pop(0))
        if rn < len(tree):
            q.append(rn)
            if tree[rn][holzzak]:
                tree[nod][1].append(tree[rn][holzzak].pop(0))

print(ans)




