'''
Maaaaaaaaaaaaze

5*5 판 5개 제시.
흰 칸은 참가 가능, 검은 칸은 참가 불가능.
판을 시계방향 / 반시계 방향 자유 회전 가능.
회전 한 뒤 5개를 쌓는다.
현재 위치한 칸에서 면으로 인접한 칸이 참가자가 들어갈 수 있는 칸이면 이동 가능.
참가자 중 본인이 설계한 미로를 가장 적은 이동 횟수로 탈출한 사람이 우승.
미로가 막혀있거나 도달 할 수 없다면 탈출이 불가능.

우승하기 위해서는 가장 적은 이동 횟수로 출구로 도달해야 한다. 몇회?

입력
25줄에 걸쳐 판떼기 제시. 5줄에 걸쳐 제시. 각 줄에는 5개의 숫자가 빈 칸을 사이에 두고 제시. 0은 벽 1은 이동 가능.

출력
가장 적은 이동 횟수로 탈출 가능한 최소 이동 횟수.

조건
임의로 선택한 꼭짓점에 위치한 칸이고, 출구는 입구와 면을 공유하지 않는 꼭짓점에 위치한 칸.

아이디어
맨 윗칸 하나 고정.
아래칸 회전하면서 최소횟수 v 만들기
5 1
4 16
3 12
2 8
1 4
윗판 갈아가면서 확인, 아랫판 바꿔가면서 확인.
ans 값 넣고 return
최솟값은 12이므로 만약 ans가 12라면 return

백트래킹 : 맨 위랑 맨 아래는 모서리에 1이 존재해야 한다.
'''
import sys
input = sys.stdin.readline

sheet1 = [list(map(int, input().rstrip().split())) for _ in range(5)]
sheet2 = [list(map(int, input().rstrip().split())) for _ in range(5)]
sheet3 = [list(map(int, input().rstrip().split())) for _ in range(5)]
sheet4 = [list(map(int, input().rstrip().split())) for _ in range(5)]
sheet5 = [list(map(int, input().rstrip().split())) for _ in range(5)]

permu = [1,2,3,4,5]



