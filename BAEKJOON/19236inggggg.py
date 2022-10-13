'''
청소년 상어

4*4 공간. 각 칸의 물고기는 번호가 정해져 있다. 1~16. 방향은 8방향
청소년 상어는 0,0 물고기를 먹고 0,0 진입.
상어의 방향은 0,0에 있던 물고기의 방향과 같다. 이후 물고기 이동.

물고기는 번호가 작은 순서로 이동.
물고기는 한 칸 이동 가능
이동 할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸.
이동 할 수 없는 칸은 상어가 있거나 경계 밖.
이동 불가능 시 가능 할 때까지 방향을 45도 반시계 회전. 이동 할 수 있는 칸이 없으면 이동x 그 외에는 그 칸으로 이동.
물고기가 다른 물고기가 있는 칸으로 이동 할 때는 서로 위치를 바꾸는 방식으로 이동.

이후 상어가 이동한다. 방향에 있는 칸으로 이동 가능. 여러칸 이동 가능.
물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고 그 물고기의 방향 게또다제. 이동 중 칸에 있는 친구는 안먹는다. 물고기가 없는 칸으로 이동 불가능. 이동 할 수 없으면 집에 감.

반복.
상어가 먹을 수 있는 물고기 번호의 최대 합

입력
4개 줄게 각 칸에 들어가있는 물고기 정보 제시.
물고기번호a, 방향b. 12시 기준으로 반시계 방향으로 1 2 3 4 5 6 7 8

출력
물고기 번호 합 최댓값
'''
import sys
input = sys.stdin.readline

dh = [-1, -1, 0, 1, 1, 1, 0, -1]
dw = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(grh, dgrp, val):
    global ans

g = []
dg = []
alive = {}
for i in range(4):
    fsh1, di1, fsh2, di2, fsh3, di3, fsh4, di4 = map(int, input().rstrip().split())
    g.append([fsh1, fsh2, fsh3, fsh4])
    dg.append([di1, di2, di3, di4])
    alive.add(fsh1)
    alive.add(fsh2)
    alive.add(fsh3)
    alive.add(fsh4)

cnt = g[0][0] # 잡아먹으면서
alive.remove(cnt)
g[0][0] = 0 # 상어 등장!
ans = 0

dfs(g, dg, cnt)


'''
def fmove(fijp, figra, digra):
    nfjp, nfg, ndg = [], [], []
    for i in fijp:
        nfjp.append(i[:])
    for i in figra:
        nfg.append(i[:])
    for i in digra:
        ndg.append(i[:])
    shh, shw = nfjp[0]
    shd = ndg[shh][shw]
    
    for i in range(1, 17):
        fh, fw = nfjp[i]
        fd = ndg[fh][fw]
        nfh, nfw = fh+dh[fd], fw+dw[fd]
        if 0<=nfh<4 and 0<=nfw<4 and [nfh, nfw]!=nfjp[0]:
            chidx = 0
            for j in range(1, 17):
                if [nfh, nfw] == nfjp[j]:
                    chidx = j
            g[][], g[][] = g[][], g[][]
            nfjp[i], nfjp[j] = nfjp[j], nfjp[i]

def fmove():
    for i in range(1, 17):
        if fjp[i]:
            fh, fw = fjp[i][0], fjp[i][1]
            fd = dg[fh][fw]
            nfh, nfw = fh+dh[fd], fw+dw[fd]
            if 0<=nfh<4 and 0<=nfw<4 and [nfh, nfw]!=fjp[0]:
                chidx = 0
                for j in range(1, 17):
                    if [nfh, nfw] == fjp[j]:
                        break
                fg[fjp[i][0]][fjp[i][1]], fg[fjp[j][0]][fjp[j][1]] = fg[fjp[j][0]][fjp[j][1]], fg[fjp[i][0]][fjp[i][1]]
                dg[fjp[i][0]][fjp[i][1]], dg[fjp[j][0]][fjp[j][1]] = dg[fjp[j][0]][fjp[j][1]], dg[fjp[i][0]][fjp[i][1]]
                fjp[i], fjp[j] = fjp[j], fjp[i]
            else:
                fla = True
                while fla:
                    dg[fh][fw] = (fd+1) % 8
                    
'''







