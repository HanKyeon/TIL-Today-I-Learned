'''
좌표 정렬하기 2

2차원 평면 위 n개 점 제시. y좌표 증가하는 순으로, y가 같다면 x가 증가하는 순서로 정렬 출력

입력
n 제시
a, b 제시

출력
ㅇㅇ
'''
import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    ans.append(list(map(int, input().rstrip().split())))
ans.sort(key=lambda x: (x[1], x[0]))
for i in ans:
    print(*i)