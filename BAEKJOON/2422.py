'''
한윤정이 이탈리아에 가서 아이스크림을 사먹는데

n개 종류 아이스크림. 1번부터 n번. 맛없는 조합 피해서 3개 선택할 것. 몇개임?

입력
n, m 제시.
섞어먹으면 안되는 조합 번호 제시. 같은 번호 조합 안나옴.

출력
가능한 방법이 총 몇 개 있는지 출력.
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
g = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    g[a][b], g[b][a] = 1, 1
ans = 0
for three in combinations(list(range(1, n+1)), 3):
    a, b, c = three
    if g[a][b] or g[b][c] or g[a][c]:
        continue
    ans += 1
print(ans)

'''
빠른 사람

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
icecreams = {}
series = []

for n in range(1,N+1):
  icecreams[n] = []
  series.append(n)

series = set(series)

for m in range(M):
  ice1, ice2 = map(int,input().split())
  if ice1 > ice2:
    a = ice1
    ice1 = ice2
    ice2 = a

  icecreams[ice1].append(ice2)

for i in range(1,N+1):
  icecreams[i] = series.difference(icecreams[i] + list(range(1,i+1)))
  #print(icecreams)

count = 0
for n in range(1,N-1):
  for k in icecreams[n]:
    count += len(set(icecreams[n]) & set(icecreams[k]))

print(count)

'''




