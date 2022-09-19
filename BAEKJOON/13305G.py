'''
주유소

n개의 도시. 일직선 도로 위에 존재.
좌에서 우로 이동 예정. 도시간 거리 다름.
처음에 주유소에서 기름을 넣고 출발 예정. 기름통의 크기는 무제한. 1km마다 1리터 사용.
도시에 단일 주유소, 주유소 리터당 가격.
젤 왼쪽에서 젤 오른쪽 가는데 최소 비용.

입력
도시 갯수 n 2이상 10만이하.
도로 길이가 n-1개 자연수 제시. 한줄
주유소 가격 n개 제시.
젤 왼쪽에서 오른쪽 도시까지 거리는 1이상 10억이하.
리터당 가격은 1이상 10억이하.

출력
최소 비용 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
el = list(map(int, input().rstrip().split()))
cl = list(map(int, input().rstrip().split()))

ans = 0
for i in range(n-1):
    if cl[i] < cl[i+1]:
        cl[i+1] = cl[i]
    ans += el[i]*cl[i]

print(ans)






















