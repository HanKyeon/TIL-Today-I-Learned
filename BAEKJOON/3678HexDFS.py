'''
카탄의 개척자

벌집모양으로 만들어 갈 것이다.
새 타일은 이미 채워진 인접한 타일에 들어있는 자원과 다른 자원
보드에 존재하는 자원 중 가장 적은 자원 선택.
가능한 자원이 여러가지라면 가 작은 것을 선택.

빙글빙글 돌면서 시작한다. n번째 타일에 어떤 자원이 나타나는가?

입력
테케 t 제시.
정수 n 제시.

출력
n번째 타일에 들어있는 자원 출력.
'''
'''
0 0 0 0 0 0 0
0 0 0 A 9 8 0
0 0 B 2 1 7 0
0 C 3 0 6 I 0
0 D 4 5 H 0 0
0 E F G 0 0 0
0 0 0 0 0 0 0
'''
import sys
from collections import deque
input = sys.stdin.readline

dh = [0,1,1,0,-1,-1]
dw = [-1,-1,0,1,1,0]
nz = [0, 6, 18, 36, 60, 90, 126, 168, 216, 270, 330, 396, 468, 546, 630, 720, 816, 918, 1026, 1140, 1260, 
1386, 1518, 1656, 1800, 1950, 2106, 2268, 2436, 2610, 2790, 2976, 3168, 3366, 3570, 3780, 3996, 4218, 4446, 4680, 4920, 5166, 5418, 5676, 5940, 6210, 6486, 6768, 7056, 7350, 7650, 7956, 8268, 8586, 8910, 9240, 9576, 9918, 10266]
def check(num):
    for i in range(59):
        if num > nz[i]+1:
            continue
        return i

def lego(num):
    if num <= 7:
        if num == 6:
            return 2
        if num == 7:
            return 3
        return num
    size = check(num)
    mtr = [1, 1, 0, 0, 0] # 0 1 2 3 4 로 재료 표기.
    size2 = 1+size*2
    g = [[-1]*(size2) for _ in range(size2)]
    g[size][size] = 0
    g[size-1][size+1] = 1
    q = deque([(size-1, size+1, 0)]) # h, w, di
    num-=2
    while q and num:
        h, w, di = q.popleft()
        num -= 1
        if di == 6:
            di = 0
        ndi = (di+1)%6
        nh, nw = h+dh[di], w+dw[di]
        nnh, nnw = h+dh[ndi], w+dw[ndi]
        if g[nnh][nnw] < 0:
            hbg = {0,1,2,3,4}
            for i in range(6):
                nnnh, nnnw = nnh+dh[i], nnw+dw[i]
                if 0<=nnnh<size2 and 0<=nnnw<size2 and g[nnnh][nnnw] in hbg:
                    hbg.remove(g[nnnh][nnnw])
            # 보드에 가장 적게 나타난 자원
            tg, val = -1, 10001
            hbg = sorted(list(hbg))
            for i in hbg:
                if mtr[i] < val:
                    tg = i
                    val = mtr[i]
            mtr[tg] += 1 # 카운트 증가
            # 큐 삽입
            g[nnh][nnw] = tg
            q.append((nnh, nnw, di+1))
        else:
            hbg = {0,1,2,3,4}
            for i in range(6):
                nnnh, nnnw = nh+dh[i], nw+dw[i]
                if 0<=nnnh<size2 and 0<=nnnw<size2 and g[nnnh][nnnw] in hbg:
                    hbg.remove(g[nnnh][nnnw])
            # 보드에 가장 적게 나타난 자원
            tg, val = -1, 10001
            hbg = sorted(list(hbg))
            for i in hbg:
                if mtr[i] < val:
                    tg = i
                    val = mtr[i]
            mtr[tg] += 1 # 카운트 증가
            # 큐 삽입
            g[nh][nw] = tg
            q.append((nh, nw, di))

    return tg+1


for _ in range(int(input())):
    n = int(input())
    print(lego(n))

'''
육각형 2차원을 만든다.
만든 뒤 확인 할 칸은 자신 주위 6칸으로 하기는 싫다.
내가 이전에 온 방향, 가려는 방향, 그 사이 방향

0 0 0 0 0 0 0
0 0 0 A 9 8 0
0 0 B 2 1 7 0
0 C 3 0 6 I 0
0 D 4 5 H 0 0
0 E F G 0 0 0
0 0 0 0 0 0 0

# 기본 육각형 순회.
# 이거는 일단 size를 정하는 함수
nl = [0]
for i in range(1, int(input())):
    # nl.append(nl[i-1] + (i*(i+1))//2 * 6)
    nl.append(nl[i-1] + i * 6)
print(nl)
# 육각형 만들기.
def lego(num):
    if num == 1: # 1개면 수동 계산해라.
        return
    size = check(num)
    mtr = [1, 1, 0, 0, 0] # 0 1 2 3 4 로 재료 표기.
    size2 = 1+size*2
    g = [[-1]*(size2) for _ in range(size2)]
    g[size][size] = 0
    g[size-1][size+1] = 1
    q = deque([(size-1, size+1, 0)]) # h, w, di, rot
    cnt = 1
    while q:
        h, w, di = q.popleft()
        cnt+=1
        if cnt == num:
            break
        if di == 6:
            di = 0
        ndi = (di+1)%6
        nh, nw = h+dh[di], w+dw[di]
        nnh, nnw = h+dh[ndi], w+dw[ndi]
        if g[nnh][nnw] < 0:
            g[nnh][nnw] = cnt
            q.append((nnh, nnw, di+1))
        else:
            g[nh][nw] = cnt
            q.append((nh, nw, di))
'''
'''
1등의 코드

HEX = 6
NUM_RESOURCE = 5
CENTER_RESOURCE = 0


def flatten_list(xs_list):
    return [x for xs in xs_list for x in xs]


class ResourceCounter:
    def __init__(self, num_resource):
        self.counter = [0] * num_resource

    def select_resource(self, excludes):
        candidates = sorted(enumerate(self.counter), key=lambda x: (x[1], x[0]))
        for resource, _ in candidates:
            if resource not in excludes:
                return resource

    def increase(self, resource):
        self.counter[resource] += 1

    def __str__(self):
        return str(self.counter)


def init_katan_table(num_layers):
    counter = ResourceCounter(NUM_RESOURCE)
    layers = [[CENTER_RESOURCE]]
    counter.increase(CENTER_RESOURCE)

    for layer_idx in range(1, num_layers + 1):
        pre_layer = layers[layer_idx - 1]
        line_len = layer_idx
        layer = [None] * (line_len * HEX)
        pos_in_layer = 0
        pos_in_pre_layer = 0
        for line_idx in range(HEX):
            for idx in range(line_len):
                excludes = []
                if pos_in_layer > 0:
                    excludes.append(layer[pos_in_layer - 1])
                    excludes.append(pre_layer[pos_in_pre_layer - 1])
                else:
                    excludes.append(pre_layer[-1])

                if idx < line_len - 1:
                    excludes.append(pre_layer[pos_in_pre_layer])
                    pos_in_pre_layer += 1
                elif line_idx == HEX - 1:
                    excludes.append(layer[0])

                selected_resource = counter.select_resource(excludes)
                # print(f"{layer_idx:02d} - {pos_in_layer:03d} : {selected_resource}, {counter}, {excludes}")
                layer[pos_in_layer] = selected_resource
                counter.increase(selected_resource)

                pos_in_layer += 1
        layers.append(layer)

    return flatten_list(layers)


def calc_num_layers(pos):
    cur_pos = 1
    num_layers = 0
    while cur_pos < pos:
        num_layers += 1
        cur_pos += num_layers * HEX
    return num_layers


def katan(pos_list):
    max_pos = max(pos_list)
    num_layers = calc_num_layers(max_pos)
    table = init_katan_table(num_layers)
    return [table[pos - 1] + 1 for pos in pos_list]


def read_input_lines_with_count_header():
    import sys
    _ = int(sys.stdin.readline())
    inputs = [line.rstrip() for line in sys.stdin.readlines()]
    return inputs


def main():
    res = katan([int(x) for x in read_input_lines_with_count_header()])
    for x in res:
        print(x)


if __name__ == "__main__":
    main()


################################################################

def findPoints():
    s = cur + layer - 1
    for a in range(6):
        points[a] = s
        s += layer - 1


resource = [10000, 1, 2, 2, 1, 1]
board = [0, 1, 2, 3, 4, 5, 2, 3] + [0] * 9993
cur = 7
k = 12
layer = 3
prevPoints = [2, 3, 4, 5, 6, 7]
while True:
    near1 = cur
    near2 = cur - 6 * (layer - 2) + 1
    points = [0] * 6
    findPoints()
    for _ in range(k):
        options = [True] * 6
        options[board[cur]] = False
        cur += 1
        if cur > 10000:
            break
        if cur in points:
            near1 = prevPoints[points.index(cur)]
            near2 = near1 + 1
            if cur == points[-1]:
                options[board[cur - 6 * (layer - 1) + 1]] = False
                options[board[prevPoints[-1]]] = False
            else:
                options[board[prevPoints[points.index(cur)]]] = False
        else:
            options[board[near1]] = False
            options[board[near2]] = False
            near1, near2 = near2, near2 + 1
        chosen = 0
        for t in range(5, 0, -1):
            if options[t]:
                if resource[chosen] >= resource[t]:
                    chosen = t
        board[cur] = chosen
        resource[chosen] += 1
    else:
        prevPoints = points[:]
        layer += 1
        k += 6
        continue
    break

for tc in range(int(input())):
    print(board[int(input())])
'''

