'''
마법사 상어와 파이어볼

n*n 격자에 파이어볼 m개 발사.
i번 파이어볼 위치는 ri ci, 질량은mi 방향은 di 속력은 si

방향은 12시부터 시계방향으로 8방, 0부터 7까지.

이동명령시
1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
- 이동하는 중 같은 칸에 여러개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에 대해 다음과 같은 일이 벌어진다.
- 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
- 파이어볼은 4개의 파이어볼로 나눠진다.
- 나눠진 파이어볼의 질량, 속력, 방향은 다음과 같다.
-- 질량은 (합쳐진 파이어볼 질량 합)/5 이다.
-- 속력은 (합쳐진 파이어볼 속력의 합) / 합쳐진 파이어볼 갯수 이다.
-- 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
- 질량이 0인 파이어볼은 소멸되어 없어진다.
마법사 상어가 이동을 k번 명령 한 후, 남아있는 파이어볼 질량의 합

범위 벗어나면 순환한다.

입력
n m k 제시.
m개 줄 파이어볼 정수 제시.
r, c, m, s, d. 행 렬 질량 속력 방향

출력
남아있는 파이어볼 질량의 합
'''
import sys
input = sys.stdin.readline

dh = [-1, -1, 0, 1, 1, 1, 0, -1]
dw = [0, 1, 1, 1, 0, -1, -1, -1]

def magic():
    global n, fb
    nfb = {}
    for i in fb:
        h, w = i
        wgt, spd, di = fb[i]
        for j in di:
            nh, nw = (h+dh[j]*spd)%n, (w+dw[j]*spd)%n
            if nfb.get((nh, nw), 0):
                nfb[(nh, nw)][0] += wgt
                nfb[(nh, nw)][1] += spd
                nfb[(nh, nw)][2].append(j)
            else:
                nfb[(nh, nw)] = [wgt, spd, [j]]
    
    fb = {}
    for i in nfb:
        h, w = i
        wgt, spd, di = nfb[i]
        if len(di) == 1:
            fb[(h, w)] = [wgt, spd, di]
            continue
        nwgt, nspd = wgt//5, spd//len(di)
        if nwgt == 0:
            continue
        flav, fla = di[0]%2, True
        for j in di:
            if j % 2 != flav:
                fla = False
                break
        
        if fla:
            fb[(h, w)] = [nwgt, nspd, [0,2,4,6]]
        else:
            fb[(h, w)] = [nwgt, nspd, [1,3,5,7]]

n, m, k = map(int, input().rstrip().split())
fb = {}
for _ in range(m):
    h, w, wgt, spd, di = map(int, input().rstrip().split())
    fb[(h-1, w-1)] = [wgt, spd, [di]]

for _ in range(k):
    magic()

ans = 0
for i in fb:
    wgt, spd, di = fb[i]
    ans += wgt*len(di)

print(ans)









'''
import sys
def shoot(fireballs):
    moves = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    for _ in range(K):
        temp = {}
        news = []
        for i in range(len(fireballs)):
            r, c, m, s, d = fireballs[i]
            if s and m:
                fireballs[i][0] += moves[d][0]*s
                fireballs[i][1] += moves[d][1]*s
                new_r, new_c = fireballs[i][0] % N, fireballs[i][1] % N
                if temp.get((new_r, new_c)):
                    temp[(new_r, new_c)].append([new_r, new_c, m, s, d])
                else:
                    temp[(new_r, new_c)] = [[new_r, new_c, m, s, d]]

        for key, vals in temp.items():
            if len(vals) > 1:
                new_m = new_s = d_flag_odd = d_flag_even = 0
                for i in range(len(vals)):
                    new_m += vals[i][2]
                    new_s += vals[i][3]
                    if vals[i][4] % 2:
                        d_flag_odd += 1
                    else:
                        d_flag_even += 1
                if d_flag_odd == len(vals) or d_flag_even == len(vals):
                    new_d = (0, 2, 4, 6)
                else:
                    new_d = (1, 3, 5, 7)

                for i in range(4):
                    if new_m // 5:
                        news.append([key[0], key[1], new_m//5, new_s//len(vals), new_d[i]])
            else:
                news.append(*vals)
        fireballs = news
    return fireballs


N, M, K = map(int, sys.stdin.readline().split())
fireballs = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
result = shoot(fireballs)
ans = sum(map(lambda x: x[2], result))
print(ans)
'''