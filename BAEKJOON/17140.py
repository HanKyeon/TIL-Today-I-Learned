'''
이차원 배열과 연산

3*3 배열 A. 인덱스는 1부터. 1초마다 배열에 연산 적용.

R : 배열 A의 모든 행에 대해 정렬 수행. 행의 갯수 >= 열의 갯수인 경우 적용.
C : 배열 A의 모든 열에 대해서 정렬을 수행. 행의 갯수 < 열의 갯수인 경우 적용.

행/렬 정렬 하려면 각각의 수가 몇 번 나왔는지 알아야 한다. 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬.
배열 A에서 정렬된 결과를 다시 넣는다. 정렬된 결과를 다시 넣을 때는 수와 등장 횟수를 모두 넣으며 순서는 수가 먼저이다.

예를 들어 3,1,1 에는 3이 1회 1이 2회 등장. 정렬되면 3 1 1 2가 된다. 다시 이 배열에는 3이 한 버 1이 2번 2가 한 번 등자.ㅇ 따라서 2 1 3 1 1 2
정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다.
R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고, C연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다. 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬 할 때 0은 무시한다.
행렬 크기가 100이 넘어가면 처음 100개를 제외한 나머지는 버린다.
배열 A에 들어있는 수와 r,c,k 가 주어졌을 때, A r,c값이 k가 되기 위한 최소 시간 구하자.

입력
r,c,k 제시.
3개 줄에 배열 A에 들어가있는 수 제시.
배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.

출력
A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다. 100초가 지나도 A[r][c] ==k가 되지 ㅇ낳으면 -1 출력한다.
'''
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def R():
    global g
    ng = []
    ml = 0
    for i in g:
        dii = {x: 0 for x in set(i) if x != 0}
        heap = []
        for j in i:
            if j:
                dii[j] += 1
        for k in dii:
            if k == 0:
                continue
            heappush(heap, [dii[k], k])
        ng.append([])
        while heap:
            cnt, num = heappop(heap)
            ng[-1].append(num)
            ng[-1].append(cnt)
        ml = max(ml, len(ng[-1]))
    if ml <= 100:
        for i in ng:
            while len(i) < ml:
                i += [0]
        g = []
        for i in ng:
            g.append(i[:])
    else:
        for i in ng:
            if len(i) <= 100:
                while len(i) < 100:
                    i += [0]
            else:
                i = i[:100]
        g = []
        for i in ng:
            g.append(i[:])

def C():
    global g
    g = list(map(list, zip(*g)))
    ng = []
    ml = 0
    for i in g:
        dii = {x: 0 for x in set(i) if x != 0}
        heap = []
        for j in i:
            if j:
                dii[j] += 1
        for k in dii:
            if k == 0:
                continue
            heappush(heap, [dii[k], k])
        ng.append([])
        while heap:
            cnt, num = heappop(heap)
            ng[-1].append(num)
            ng[-1].append(cnt)
        ml = max(ml, len(ng[-1]))
    if ml <= 100:
        for i in ng:
            while len(i) < ml:
                i += [0]
        ng = list(map(list, zip(*ng)))
        g = []
        for i in ng:
            g.append(i[:])
    else:
        for i in ng:
            if len(i) <= 100:
                while len(i) < 100:
                    i += [0]
            else:
                i = i[:100]
        ng = list(map(list, zip(*ng)))
        g = []
        for i in ng:
            g.append(i[:])

r, c, k = map(int, input().rstrip().split())
r-=1
c-=1
g = [list(map(int, input().rstrip().split())) for _ in range(3)]

if len(g) > r and len(g[0]) > c and g[r][c] == k:
    print(0)
else:
    for i in range(1, 101):
        if len(g) >= len(g[0]):
            R()
            # for ii in g:
            #     print(ii)
            # print('==R', i)
            if len(g) > r and len(g[0]) > c and g[r][c] == k:
                print(i)
                break
        else:
            C()
            # for ii in g:
            #     print(ii)
            # print('==C', i)
            if len(g) > r and len(g[0]) > c and g[r][c] == k:
                print(i)
                break
    else:
        print(-1)


'''
# 빠른 아재

def transpose(board, row_num, col_num):
    temp = [[] * row_num for _ in range(col_num)]
    for i, line in enumerate(board):
        for j, ele in enumerate(line):
            temp[j].append(ele)

        for _ in range(col_num - len(line)):
            j += 1
            temp[j].append(0)

    return temp


i, j, k = map(int, input().split())
i -= 1
j -= 1

board = [list(map(int, input().split())) for _ in range(3)]

row_len = 3
col_len = 3

cnt = 0

trans_flag = False

flag = 1
if row_len > i and len(board[i]) > j and board[i][j] == k:
    flag = 0

while cnt <= 100 and flag == 1:
    if row_len < col_len or (trans_flag and row_len == col_len):
        board = transpose(board, row_len, col_len)

        i, j = j, i
        row_len, col_len = col_len, row_len

        trans_flag ^= True

    cnt += 1

    for r_num, row in enumerate(board):
        r_set = sorted(set(row))

        if r_set[0] == 0:
            r_set.remove(0)

        temp_list = []
        c_list = [row.count(ele) for ele in r_set]

        for r, c in zip(r_set, c_list):
            temp_list.append([r, c])

        temp_list.sort(key=lambda t: t[1])


        if len(temp_list) > 50:
            temp_list = temp_list[:50]

        new_list = []

        [new_list.extend(li) for li in temp_list]

        board[r_num] = new_list

        if col_len < len(new_list) or r_num == 0:
            col_len = len(new_list)

    flag = 1
    if row_len > i and len(board[i]) > j and board[i][j] == k:
        flag = 0

if cnt > 100:
    cnt = -1

print(cnt)
'''











