'''
톱니바퀴

8개 톱니. 4개가 일렬로 있다.
톱니 4개
톱니 k번 회전 할 것. 한 칸 기준.
톱니를 회전 시키려면, 회전 시킬 톱니바퀴와 회전 시킬 방향을 결정해야 한다.
옆에 있는 톱니바퀴의 극과 같다면 회전하지 않고, 옆 톱니바퀴의 극이 다르면 회전 방향과 반대로 회전한다.

입력
1번 톱니바퀴 상태
2번 톱니 상태
3번 톱니 상태
4번 톱니 상태
12시부터 시계방향 순서대로 제시. N극은 0 S극은 1
회전 횟수k 제시.
회전 시킨 방법 순서대로 제시.
회전 시킨 톱니 번호, 방향. 1시계 -1반시계

출력
k번 시킨 후 네 바퀴 점수의 합 출력.
1번 톱니바퀴 12시방향이 n이면0 s면1
2번 12시 n이면 0 s면 2
3번 0 4
4번 0 8

'''
import sys
input = sys.stdin.readline

t1, t2, t3, t4 = input().rstrip(), input().rstrip(), input().rstrip(), input().rstrip()

one3 = 2
di = {0:[0, 2, 6], 1:[0, 2, 6], 2:[0, 2, 6], 3:[0, 2, 6]}

def tick(tg, direc):
    if tg == 0:
        if not v[tg+1] and t1[di[tg][1]] != t2[di[tg+1][2]]:
            v[tg+1] = 1
            tick(tg+1, -direc)
        di[tg] = list(map(lambda x: (x-direc)%8, di[tg]))
        return
    elif tg == 3:
        if not v[tg-1] and t4[di[tg][2]] != t3[di[tg-1][1]]:
            v[tg-1] = 1
            tick(tg-1, -direc)
        di[tg] = list(map(lambda x: (x-direc)%8, di[tg]))
        return
    elif tg == 1:
        if not v[tg+1] and t2[di[tg][1]] != t3[di[tg+1][2]]:
            v[tg+1] = 1
            tick(tg+1, -direc)
        if not v[tg-1] and t2[di[tg][2]] != t1[di[tg-1][1]]:
            v[tg-1] = 1
            tick(tg-1, -direc)
        di[tg] = list(map(lambda x: (x-direc)%8, di[tg]))
        return
    elif tg == 2:
        if not v[tg+1] and t3[di[tg][1]] != t4[di[tg+1][2]]:
            v[tg+1] = 1
            tick(tg+1, -direc)
        if not v[tg-1] and t3[di[tg][2]] != t2[di[tg-1][1]]:
            v[tg-1] = 1
            tick(tg-1, -direc)
        di[tg] = list(map(lambda x: (x-direc)%8, di[tg]))
        return

for k in range(int(input())):
    a, b = map(int, input().rstrip().split())
    v = [0, 0, 0, 0]
    v[a-1] = 1
    tick(a-1, b)
ans = int(t1[di[0][0]])*1 + int(t2[di[1][0]])*2 + int(t3[di[2][0]])*4 + int(t4[di[3][0]])*8
print(ans)

'''
    if tg == 1:
        if t1[di[tg][1]] != t2[di[tg+1][2]]:
            di[tg+1] = list(map(lambda x: (x+direc)%8, di[tg+1]))
        di[tg] = list(map(lambda x: (x-direc)%8, di[tg]))
        return
    elif tg == 4:
        if t1[di[tg][2]] != t2[di[tg-1][1]]:
            di[tg-1] = list(map(lambda x: (x+direc)%8, di[tg-1]))
        di[tg] = list(map(lambda x: (x-direc)%8, di[tg]))
        return
    if t1[di[tg][1]] != t2[di[tg+1][2]]:
        di[tg+1] = list(map(lambda x: (x+direc)%8, di[tg+1]))
    if t1[di[tg][2]] != t2[di[tg-1][1]]:
        di[tg-1] = list(map(lambda x: (x+direc)%8, di[tg-1]))
'''


















