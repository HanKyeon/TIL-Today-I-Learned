'''
탈출

버튼 A를 누르면 n이 1 증가
B를 누르면 *2, 0이 아닌 가장 높은 자릿수의 숫자가 1 감소. 0이면 무반응
99999 넘어가면 탈출 실패
B눌렀을 때 *2되는데 그 때 99999 넘어가도 탈출 실패
최대 T회 버튼 가능, 그 안에 n을 g와 같게 만들어야 한다.
최소로 탈출할 수 있는 횟수

입력
n, t, g 제시. 수 최대버튼클릭수 목표수

출력
최소횟수 출력, 불가능이면 ANG 출력
'''
from collections import deque

def A(num): return num+1 if num < 99999 else -1

def B(num):
    if not num: return -1
    num2 = num*2
    if num2 > 99999: return -1
    return num2-10**(len(str(num2))-1)

def bfs():
    global n, g
    if n == g: return 0
    while q:
        num, cnt = q.popleft()
        if not cnt: continue
        a, b = A(num), B(num)
        if a == g: return t-cnt+1
        if b == g: return t-cnt+1
        if 0<=a and not v[a]: v[a] = 1; q.append((a, cnt-1))
        if 0<=b and not v[b]: v[b] = 1; q.append((b, cnt-1))
    return "ANG"

n, t, g = map(int, input().rstrip().split())
v = [0]*100000
v[n] = 1
q = deque([(n, t)])
print(bfs())
