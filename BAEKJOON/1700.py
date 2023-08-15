'''
멀티탭 스케줄링

플러그 빼는 횟수 최소화 할 것.
사용 순서가 제시되고 플러그 빼는 횟수를 최소화하면 된다.

입력
멀티탭 구멍 갯수n 전기용품 사용횟수 k 제시
전기용품 이름이 k이하 자연수로 제시

출력
하나씩 플러그를 빼는 최소 횟수 출력
'''
import sys
input = sys.stdin.readline

def find(i):
    global k
    ret, idx = 0, -1
    for num in using:
        try:
            nidx = nl.index(num, i)
            if idx < nidx: ret, idx = num, nidx
        except: return num
    return ret

n, k = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
if n >= k:
    print(0)
    exit()
using, ans = set(), 0

for i, num in enumerate(nl) :
    using.add(num)
    if len(using) > n:
        ans += 1
        using.remove(find(i))
print(ans)

'''
# 빠른 코드
n, k = map(int,input().split())
arr = list(map(int,input().split()))
plug = []
c = 0

for i in range(k):
    if arr[i] in plug: 
        continue
    if len(plug)<n: 
        plug.append(arr[i])
        continue

    idxs = []
    for j in range(n):
        try:
            idxs.append(arr[i:].index(plug[j]))
        except:
            idxs.append(101)
    plug[idxs.index(max(idxs))] = arr[i]
    c += 1

print(c)
'''
