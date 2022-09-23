'''
플로이드 2

n개의 도시. 1이상 100이하
한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스.
모든 도시 쌍 A, B에 대해 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구해라.

입력
도시 갯수 n 100이하자연수
버스 갯수 m 10만이하
m줄의 버스 정보. 시작도시a 도착도시b 비용c 비용 10만이하

출력
n개 줄 출력. i에서 j로 가는데 필요한 최소 비용
i에서 j로 갈 수 없는 경우 그 자리는 0
n*n 개의 줄 출력. i*n+j 번째 줄 도시에는 도시 i에서 도시 j로 가는 최소 비용에 포함되어있는 도시 갯수 k 출력.
도시 i에서 도시 j로 가는 경로를 공백으로 구분해 출력. 도시 i와 j도 출력. 갈 수 없다면 0 출력.
'''
'''
아까 dijkstra 한 것처럼 자기 값을 들고 가서 더해주면 되는게 아닐지?
'''
import sys
input = sys.stdin.readline

n, m = int(input()), int(input())

vst = [[[i] for _ in range(n)] for i in range(n)]
dst = [[int(100)]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    dst[a-1][b-1] = min(dst[a-1][b-1], c)
    vst[a-1][b-1] = [b]
for i in range(n):
    dst[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dst[i][j] > dst[i][k] + dst[k][j]:
                dst[i][j] = dst[i][k] + dst[k][j]
                vst[i][j] = vst[i][k] + vst[k][j]

for i in vst:
    print(i)
print('==============')
for i in dst:
    print(*i)

for i in range(n):
    for j in range(n):
        if i==j:
            print(0)
            continue
        print(len(vst[i][j])+1, end=' ')
        print(str(i+1), end=' ')
        print(*vst[i][j])










