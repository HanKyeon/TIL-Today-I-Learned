'''
병든 나이트

n*m 체스판 좌하단 시작. 4가지로 이동 가능
-2,1 -1,2 1,2 2,1
이동횟수가 4번보다 적지 않다면 모두 한 번 씩 사용해야 한다. 적은 경우 제약 없음
방문 최대칸 갯수 제시.

입력
n, m 제시

출력
방문할 수 있는 칸 최대값 출력
'''
def lego(n, m):
    if m == 1 or n == 1:
        return 1
    if n == 2:
        return min(4, (m+1)//2)
    if m < 7:
        return min(4, m)
    return m-2
n, m = map(int, input().rstrip().split())
print(lego(n, m))
