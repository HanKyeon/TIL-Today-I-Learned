'''
통나무 자르기

나무를 종이공장에 옮겨야 한다. 길이 l, K개의 위치에서만 자를 수 있다. 자를 수 있는 위치 제시. 좌측부터, 최대 C번 자를 수 있다.
가장 긴 조각을 작게 만들고, 그 길이를 구해라.

입력
l, k, c 제시

출력
첫째 줄에 두 개의 수 출력. 가장 긴 조각 길이, 그 때 처음 자르는 위치 출력. 가능이 여러개라면 처음 자르는 위치가 작은 것을 출력.
'''
'''
0111110000000000000000 이런 형태이면 5번 자르기 가능할 경우 다 자르면 되고 최장 길이가 길다.
1111111111111111111111 이런 형태이고 5번 자르기 가능할 경우 l//5에 근사하게 한다.
'''
from sys import stdin
input = stdin.readline

def lego(mid):
    global fla
    if fla > mid:   # 현재 기준으로 자를 수 없는 나무 조각이 있는 경우.
        return 10001, 0
    ret, cnt = 0, 0
    for piece in cha[::-1]: 
        ret += piece      # 나무조각 길이를 누적 합
        if ret > mid:     # 기준이 넘어가면
            ret = piece   # 새로운 조각으로 취급
            cnt += 1
    return cnt, ret if cnt == c else cha[0]

l, k, c = map(int, input().rstrip().split())
nl = [0, *sorted(map(int, input().rstrip().split())), l]
cha = [nl[idx+1] - nl[idx] for idx in range(k+1)]
fla = max(cha) # 가장 먼저 잘라야하는 길이

sta, end = 0, l
ans = [l, -1]
while sta <= end:
    mid = (sta + end) // 2   # 나무조각 하나의 최대 길이
    cnt, front = lego(mid)
    if cnt <= c:             # 조각을 더 작게 자를 수 있는 방향으로 update
        ans = [mid, front]
        end = mid - 1
    else:                    # 조각을 더 크게 자를 수 있는 방향으로 update
        sta = mid + 1
print(*ans)

'''
# 빠른 코드
L, K, C = map(int, input().split())
posit = [0] + sorted(map(int, input().split())) + [L]
pieces = [posit[i + 1] - posit[i] for i in range(K+1)][::-1]
max_piece = max(pieces)

left, right = 0, L

def cutting(x):
    if max_piece > x:
        return C+1, 0
    total, count = 0, 0
    for piece in pieces:
        total += piece
        if total > mid:
            total = piece
            count += 1
    return count, total if count == C else pieces[-1]
while left <= right:
    mid = (left + right) // 2
    cnt, result = cutting(mid)
    if C < cnt:
        left = mid + 1
    else:
        answer = mid
        start = result
        right = mid - 1
print(answer, start)
'''
