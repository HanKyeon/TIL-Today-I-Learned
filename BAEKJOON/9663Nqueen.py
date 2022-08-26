'''
N-QUEEN

갑자기 구현 할 자신감 생김
N*N 체스판에 퀸N개를 서로 공격 할 수 없게 놓는 문제.
퀸을 놓는 방법의 수.

입력
N 제시. 1이상 15미만

출력
N개를 서로 공격 할 수 없게 놓는 경우의 수
'''

def Nqueen(h):
    global ans, n, hai
    if sum(v) == n:
        ans+=1
        return
    for i in range(n):
        if v[i] == 1:
            continue
        if v[i] == 0 and cro.get(h+i, 0) == 0 and chai.get(h-i, 0) == 0:
            v[i] = 1 # 세로
            cro[h+i] = 1 # //대각선
            chai[h-i] = 1 # \\대각선
            Nqueen(h+1) # 실행
            chai[h-i] = 0 # \\대각선
            cro[h+i] = 0 # //대각선
            v[i] = 0 # 세로

n = int(input())
v = [0]*n
garo, sero = [0]*n, [0]*n
cro, chai = {}, {} # //대각선 방문여부 처리, \\ 대각선 방문 여부 처리
ans = 0 # 정답
Nqueen(0)
print(ans)

'''
/// 이 방향은 제거했는데 i+w
\\\ 이 방향 제거를 못햇다! -> 딕트로 제거 완료. i-w
딕트와 리스트 중 어떤게 빠르지?
  0 1 2 3
0 0 1 2 3
1 1 2 3 4
2 2 3 4 5
3 3 4 5 6
'''

'''
# 정석 코드

n = int(input())
sol = 0
map = [0]*n

def is_promising(x):
    for i in range(x): #x번째 깊이까지
        if map[i] == map[x] or abs(map[i]-map[x]) == abs(i-x): return False
    return True

def n_queen(x):
    global sol
    if x == n :
        sol += 1
        return
    else:
        for i in range(n): #x번째 깊이에서 하나씩 넣어보는중
            map[x] = i
            if is_promising(x): n_queen(x+1)

n_queen(0)
print(sol)
'''


