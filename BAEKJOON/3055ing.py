'''
탈출

비어있는 곳 . 물 * 돌 X 비버굴D 고슴도치S
고슴도치는 인접한 네 칸 중 하나로 이동 가능. 물도 매 분 비어있는 칸으로 확장.
물과 도치는 돌 패스 못함. 도치는 물이 찰 예정인 구역도 못간다. 물은 비버 소굴로 이동 못한다.

- 물 먼저 bfs 한 번 한 다음에 하면 될듯?

입력
50이하 자연수 R과 C 제시.
R개 줄에 티떱숲 지도 제시. D와 S는 pk이다.

출력
도치가 비버굴로 이동 할 수 있는 가장 빠른 시간 출력. 이동 못함녀 KAKTUS 출력
'''
import sys
input = sys.stdin.readline


r, c = map(int, input().rstrip().split())
g = [list(input().rstrip()) for _ in range(r)]
wat, bib, had = [], [], []









