'''
스타트와 링크

스타트팀 vs 링크 팀.
시너지 점수차이 최솟값출력하기.

입력
4이상 20이하 짝수 N
시너지표 제시. i,j j,i가 다를 수 있음. 1이상 100이하

출력
두 팀 능력치 차이의 최솟값
'''
import sys
from itertools import combinations # 부분집합을 반반 나눠 전부 확인하기 위함.
input = sys.stdin.readline

n = int(input()) # 입력
g = [list(map(int, input().split())) for _ in range(n)] # 점수판
mem = list(range(1, n+1)) # 멤버 리스트
memd = set(list(range(1, n+1)))  # 멤버 데이터 세트
Steam = list(combinations(mem, n//2)) # S 팀의 가능성
Lteam = [] # L팀 비워둠
for i in Steam: # 탐색하면서 L팀 목록 채우기
    Lteam.append(tuple(memd - set(i)))
ans = 1000 # 최대 차이는 1000점이라 1000으로 설정
for S, L in zip(Steam, Lteam): # Steam과 Lteam을 동시에 순회
    Sts, Lts = 0, 0 # S팀 스코어, L팀 스코어
    for i in S:
        for j in S:
            Sts += g[i-1][j-1] # S팀 스코어 추가
    for i in L:
        for j in L:
            Lts += g[i-1][j-1] # L팀 스코어 추가
    ans = min(ans, abs(Sts-Lts)) # 기존 값과 두 스코어 차이 중 작은 값이 답.
print(ans) # 출력

'''
시간 짧은 것

from itertools import combinations #조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

#조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N//2)):
    possible_team.append(team)

min_stat_gap = 10000 #갭이 가장 작은 값을 찾기 위하여
for i in range(len(possible_team)//2):
    #A 팀
    team = possible_team[i]
    stat_A = 0 #A팀 능력치
    for j in range(N//2):
        member = team[j] #멤버
        for k in team:
            stat_A += S[member][k] #멤버와 함께할 경우의 능력치들
            
    #A를 제외한 나머지 팀
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]
            
    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))
    
print(min_stat_gap)


---------
from itertools import combinations
from sys import stdin
input = stdin.readline

n = int(input())
pan = [ list(map(int, input().split())) for _ in range(n) ]
team = [ i for i in range(1, n+1) ]
team = list(combinations(team, n//2))
lp, rp = 0, len(team)-1
answer = 1e9

def team_sum(stat):

    sum = 0
    stat = list(combinations(stat, 2))

    for i, j in stat:
        sum += pan[i-1][j-1] + pan[j-1][i-1]

    return sum

while lp <= rp:

    first_team = team_sum(team[lp])
    second_team = team_sum(team[rp])
    answer = min(answer, abs(first_team-second_team))

    lp, rp = lp+1, rp-1

print(answer)

'''