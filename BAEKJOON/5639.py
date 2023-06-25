'''
이진 검색 트리

노드 왼쪽 은 부모보다 작다.
오른쪽은 부모보다 크다.
자식도 이진검색트리이다.
전위순회 (루트 좌 우) 방문한다.
후위는 좌 우 루트

이진검색트리 제시. 전위순회한 결과 제시. 트리를 후위순회한 결과를 구해라.

입력
트리 전위순회 결과 제시. 한 줄에 하나

출력
트리 후위순회 결과 출력
'''
'''
50 / 30 24 5 28 45 / 98 52 60

전위는 루트 좌 우
후위는 좌 우 루트

좌 먼저 실행해주고 출력
이후 우 실행 출력
이후 루트 출력
'''
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def lego(sta, end):
    if sta > end:
        return
    mid = end+1
    for i in range(sta+1, end+1):
        if nl[i] > nl[sta]: # 루트보다 크다면 우측 시작임
            mid = i
            break
    # 후위순회
    lego(sta+1, mid-1)
    lego(mid, end)
    print(nl[sta])

nl = []
while True:
    try:
        nl.append(int(input()))
    except:
        break
lego(0, len(nl)-1)
