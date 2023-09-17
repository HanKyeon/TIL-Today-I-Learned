'''
요세푸스 문제 0

1~n명 사람 원. 양정수 제시. k번째 사람 제거. 반복.

입력
n, k 제시

출력
요세푸스 순열 출력
'''
'''
1 2 4 5 6 7
'''
n, k = map(int, input().split())
nl = list(range(1, n+1))
ans, cnt = [], 0
while nl: cnt += (k-1); cnt%=len(nl); ans.append(str(nl.pop(cnt)))
print(f"<{', '.join(ans)}>")
'''
# 빠름
import sys
n, k = map(int, sys.stdin.readline().split())
idx = 0
queue = [i for i in range(1, n+1)]
res = []

while queue:
    idx += k - 1
    if idx >= len(queue):
        idx %= len(queue)
    res.append(str(queue.pop(idx)))
print("<", ", ".join(res), ">", sep="")
'''
