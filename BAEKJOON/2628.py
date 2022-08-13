'''
종이 자르기

입력
종이의 가로 세로 최대 100
자를 좌표 갯수
자를 점선 제공 가로는 0 좌표 세로는 1 좌표

출력
최대 넓이 출력
'''

def chais(li) :
    ls = [0] * (len(li)-1)
    for i in range(len(li)-1) :
        ls[i] = li[i+1] - li[i]
    return ls
# 입력
w, h = map(int, input().split())
p = int(input())
ps = [[] for _ in range(p)]
for i in range(p):
    ps[i] = list(map(int, input().split()))
# 가로/세로 점들 차이 최댓값
gs = max(chais(sorted([0] + [t[1] for t in ps if t[0] == 0] + [h])))
ss = max(chais(sorted([0] + [t[1] for t in ps if t[0] == 1] + [w])))
print(gs * ss)
