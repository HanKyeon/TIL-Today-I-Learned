'''
오큰수

오른쪽에서 젤 큰 숫자로 구해라. 그게 자기 자신이면 -1 출력

입력
N 1이상 100만 이하
N개의 수 스플릿

출력
새 수열 출력
'''
import sys
input = sys.stdin.readline
n = int(input())
nl = list(map(int, input().split()))
a = [-1] * n
st = []
for i in range(n):
    while st and nl[st[-1]] < nl[i]:
        a[st.pop()] = nl[i]
    st.append(i)
print(*a)


'''
4 3 2 4 1 5
5 4 4 5 5 -1
'''







'''
for i in range(n):
    m = nl[i]
    for j in range(i+1, n):
        if nl[i] < nl[j]:
            nl[i] = nl[j]
            break
    if nl[i] == m:
        nl[i] = -1
print(*nl)
'''

'''
m = nl[-1]
for i in range(n-1, -1, -1):
    if nl[i] == m:
        nl[i] = -1
    elif nl[i] < m:
        nl[i] = m
    elif nl[i] > m:
        m = nl[i]
        nl[i] = -1
print(*nl)
'''
