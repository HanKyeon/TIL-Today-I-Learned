'''
본대 산책2

D분 산책해서 8개 학관에서 딱 정보과학관에 도착하는 경우의 수.

입력
D 제시 10억이하

출력
가능한 경로 수를 1000000007로 나눈 나머지
'''
'''
숫자가 너무 커서 좀 찾아봄.
이산수학 중에, 행렬을 제곱하면서 가면 경로의 수가 나오는 것이 있다고 함.
'''
n = 8
m = {}
D = int(input())
m[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]
def f(d, sta, end):
    if d <= 1:
        return m[d][sta][end]
    m.setdefault(d, [[0 for _ in range(n)] for _ in range(n)])
    if m[d][sta][end]:
        return m[d][sta][end]
    half = d // 2
    other = half + 1 if d % 2 else half # 홀수면 +1
    for k in range(n):
        m[d][sta][end] += f(half, sta, k) * f(other, k, end)
        m[d][sta][end] %= 1000000007
    return m[d][sta][end]

print(f(D, 0, 0))

'''
# 빠른 코드

D = int(input())
#0학생회관, 1진리관, 2형남공학관, 3신양관, 4한경직, 5미래, 6전산, 7정보
graph = [[0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 0, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 1, 1, 0]]
         
def matMul(A, B):
    res = [[0]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            sum = 0
            for k in range(8):
                sum += A[i][k]*B[k][j]
            res[i][j] = sum%1000000007
    return res

def fpow(graph, n):
    if n == 1:
        return graph
    else:
        x = fpow(graph, n//2)
        if n%2 == 0:
            return matMul(x, x)
        else:
            return matMul(matMul(x, x), graph)

graph = fpow(graph, D)
print(graph[7][7])

# 두번째

import sys
input = sys.stdin.readline
mod = 1000000007

D = int(input())

graph = [[0]*8 for i in range(8)]

graph[0][1] = graph[0][2] = 1
graph[1][0] = graph[1][2] = graph[1][3] = 1
graph[2][0] = graph[2][1] = graph[2][3] = graph[2][4] = 1
graph[3][1] = graph[3][2] = graph[3][4] = graph[3][5] = 1
graph[4][2] = graph[4][3] = graph[4][5] = graph[4][7] = 1
graph[5][3] = graph[5][4] = graph[5][6] = 1
graph[6][5] = graph[6][7] = 1
graph[7][4] = graph[7][6] = 1

def multiply(A,B):
  result = [[0]*8 for i in range(8)]
  for i in range(8):
    for j in range(8):
      for k in range(8):
        result[i][j] += A[i][k]*B[k][j]
      result[i][j] %= mod
  return result

def cal(A,n):
  if n == 1:
    return A
  cal2 = cal(A,n//2)
  if n%2 == 0:
    return multiply(cal2,cal2)
  else:
    return multiply(multiply(cal2,cal2),A)

result = cal(graph,D)
print(result[0][0])
'''

