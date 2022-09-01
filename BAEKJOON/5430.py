'''
AC

R D
R은 reversed D는 pop(0)

입력
테케T
함수P 1이상 10만이하
배열 수 n
[배,열,정,수] 1이상 100이하
전체 테케에 주어지는 p 길이 합과 n의 합은 70만 이하.

출력
수행결과. 에러 시 error 출력
'''
'''
불친절했다.
빈 배열에 R을 해도 에러인지 아닌지 등 설명이 부족했다.

아이디어
배열을 실제로 뒤집지 않고 인덱싱만 0과 -1로 해주면 pop을 해주기 편하다.
R 마다 D를 0과 1로 바꿔주고, D마다 pop(0) 혹은 pop(-1)을 해주면 된다.

그 뒤로는 성실한 구현.
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    mr = input().rstrip() # 명령
    n = int(input()) # 배열의 길이
    # nl = [0] * n
    s = list(input().rstrip(']\n')[1:].split(','))
    if s == ['']:
        s = []
    else:
        s = list(map(int, s))
    d = 0
    fla = True
    for i in mr:
        if i == 'R':
            d = (d+1)%2
            continue
        elif i == 'D':
            if s != []:
                s.pop(-d)
            elif s == []:
                fla = False
                break
    if fla:
        if d == 1:
            s=list(reversed(s))
        print("[",end='')
        for i in range(len(s)):
            print(s[i], end='')
            if i != len(s)-1:
                print(',',end='')
        print("]")
    else:
        print('error')

'''
# 매우 빠른 식.
from collections import deque
import sys
T = int(sys.stdin.readline().strip())
for testcase in range(T):
    ps = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    nums = sys.stdin.readline().strip()
    if n==0:
        nums = deque([])
    else:
        nums = deque(list(map(int, nums[1:-1].split(","))))
    
    is_error = False

    # p 최적화
    p = deque([])
    d_cnt = 0
    r_cnt = 0
    for pc in ps:
        if pc=="D":
            if r_cnt %2 == 1:
                p.append("R")
            r_cnt = 0
            p.append(pc)
            d_cnt +=1
            if d_cnt > n:
                is_error = True
                break
        else:
            r_cnt +=1

    if is_error:
        print("error")
        continue
    
    if r_cnt %2 == 1:
        p.append("R")
        
    if d_cnt == n:
        print("[]")
        continue
    pop_lr = False
    for pcmd in p:
        if pcmd == "R":
            pop_lr = False if pop_lr else True
        else:
            if pop_lr:
                nums.pop()
            else:
                nums.popleft()
    if pop_lr:
        nums.reverse()
    print(f"[{','.join(map(str, nums))}]")
'''

