'''
스도쿠

가로 세로 1~9 한 번만, 정사각형에도 1~9 한 번만

입력
빈 칸 0 제시

출력
스도쿠 완성판 출력
'''
import sys
input = sys.stdin.readline

def setting(h, w):
    v = {1,2,3,4,5,6,7,8,9}
    for i in range(9):
        if g[h][i]:
            v.discard(g[h][i])
        if g[i][w]:
            v.discard(g[i][w])
        if len(v) == 1:
            g[h][w] = v.pop()
            return
    for i in range(h//3*3, h//3*3+3):
        for j in range(w//3*3, w//3*3+3):
            if g[i][j]:
                v.discard(g[i][j])
            if len(v) == 1:
                g[h][w] = v.pop()
                return
    if len(v) == 1:
        g[h][w] = v.pop()
        return
    return v

def check(h, w, num):
    v = {1,2,3,4,5,6,7,8,9}
    for i in range(9):
        if g[h][i]:
            v.discard(g[h][i])
        if g[i][w]:
            v.discard(g[i][w])
        if num and not num in v:
            return []
    for i in range(h//3*3, h//3*3+3):
        for j in range(w//3*3, w//3*3+3):
            if g[i][j]:
                v.discard(g[i][j])
            if num and not num in v:
                return []
    return v

def dfs(idx):
    if idx == len(blank):
        for i in g:
            print(*i)
        exit()
    h, w = blank[idx]
    for i in check(h, w, 0):
        g[h][w] = i
        dfs(idx+1)
        g[h][w] = 0

g = [list(map(int, input().rstrip().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if g[i][j]:
            continue
        a = setting(i, j)
        if a:
            blank.append((i, j))
if blank:
    dfs(0)
else:
    for i in g:
        print(*i)

'''
# 빠른 코드

# ref : https://www.acmicpc.net/source/28503659
import sys
speed_input = sys.stdin.readline


def some(seq):
    for e in seq:
        if e:
            return e
    return False


def cross(set_a, set_b):
    return [a + b for a in set_a for b in set_b]


class Solver:
    def __init__(self):
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.cols = self.digits
        self.squares = cross(self.rows, self.cols)
        self.unit_list = ([cross(self.rows, c) for c in self.cols] +
                     [cross(r, self.cols) for r in self.rows] +
                     [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
        self.units = dict((s, [u for u in self.unit_list if s in u]) for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s], [])) - {s}) for s in self.squares)
        self.__board = [list(speed_input()) for _ in range(9)]

    def grid_values(self):
        chars = []
        for l in self.__board:
            temp = [c for c in l if c in self.digits or c in '0.']
            chars += temp
        return dict(zip(self.squares, chars))

    def parse_grid(self):
        values = dict((s, self.digits) for s in self.squares)
        for s, d in self.grid_values().items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    def assign(self, values, s, d):
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, s, d):
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')
        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    def search(self, values):
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in self.squares):
            return values
        n, s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return some(self.search(self.assign(values.copy(), s, d)) for d in values[s])

    def __display(self, values):
        for r in self.rows:
            print(' '.join(values[r + c] for c in self.cols))

    def solve(self):
        self.__display(self.search(self.parse_grid()))


if __name__ == '__main__':
    Solver().solve()
'''
'''
board = [list(input()) for _ in range(9)]

def cross(A, B):
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

def grid_values(board):
    chars = []
    for l in board:
        temp = [c for c in l if c in digits or c in '0.']
        chars += temp
    return dict(zip(squares, chars))

def parse_grid(board):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(board).items():
        if d in digits and not assign(values, s, d):
            return False
    return values
    
def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def display(values):
    width = 1+max(len(values[s]) for s in squares)
    for r in rows:
        print(' '.join(values[r+c] for c in cols))

def solve(board): return search(parse_grid(board))

def search(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s]) 

def some(seq):
    for e in seq:
        if e: return e
    return False

display(solve(board))
'''
'''
from sys import stdin
from typing import Any, Iterable, List, Optional

input = lambda: stdin.readline().strip()

class Node:
    column: 'Column'
    row: int
    up: 'Node'
    down: 'Node'
    left: 'Node'
    right: 'Node'

    def __init__(self, column: 'Column', row: int):
        self.column = column
        self.row = row
        self.up = self
        self.down = self
        self.left = self
        self.right = self

    def iterup(self):
        it = self.up
        while it != self:
            yield it
            it = it.up

    def iterdown(self):
        it = self.down
        while it != self:
            yield it
            it = it.down

    def iterleft(self):
        it = self.left
        while it != self:
            yield it
            it = it.left

    def iterright(self):
        it = self.right
        while it != self:
            yield it
            it = it.right

    def appendright(self, node: 'Node'):
        node.left = self.left
        node.right = self
        self.left.right = node
        self.left = node


class Column(Node):
    size: int
    left: 'Column'
    right: 'Column'

    def __init__(self):
        super().__init__(None, -1)
        self.column = self
        self.size = 0

    def iterleft(self):
        it = self.left
        while it != self:
            yield it
            it = it.left

    def iterright(self):
        it = self.right
        while it != self:
            yield it
            it = it.right

    def appenddown(self, node: Node):
        node.up = self.up
        node.down = self
        self.up.down = node
        self.up = node
        self.size += 1

    def cover(self):
        self.left.right = self.right
        self.right.left = self.left

        for it in self.iterdown():
            for jt in it.iterright():
                jt.down.up = jt.up
                jt.up.down = jt.down
                jt.column.size -= 1
                assert jt.column.size >= 0

    def uncover(self):
        for it in self.iterup():
            for jt in it.iterleft():
                jt.down.up = jt
                jt.up.down = jt
                jt.column.size += 1

        self.left.right = self
        self.right.left = self

    def __repr__(self) -> str:
        return f'Column (size={self.size})'


class DancingLinks:
    head: Column
    columns: List[Column]
    row_counter: int

    def __init__(self, col_size: int):
        self.head = Column()
        self.columns = [Column() for _ in range(col_size)]
        self.row_counter = 0

        self.head.right = self.columns[0]
        self.head.left = self.columns[-1]

        self.columns[0].left = self.head
        self.columns[0].right = self.columns[1]
        self.columns[-1].right = self.head
        self.columns[-1].left = self.columns[-2]

        for i in range(1, col_size - 1):
            self.columns[i].left = self.columns[i - 1]
            self.columns[i].right = self.columns[i + 1]

    def appendrow(self, row: List[bool]):
        assert len(row) == len(self.columns)

        first = None
        for i, value in enumerate(row):
            if not value:
                continue

            node = Node(self.columns[i], self.row_counter)
            self.columns[i].appenddown(node)

            if first is None:
                first = node
            else:
                first.appendright(node)

        self.row_counter += 1

    def solve(self) -> Optional[List[int]]:
        solution = []
        def _solve():
            if self.head.right == self.head:
                return True

            lowest = self.head.right
            for it in self.head.iterright():
                if it.size == 0:
                    return False

                if it.size < lowest.size:
                    lowest = it

            lowest.cover()

            for it in lowest.iterdown():
                for jt in it.iterright():
                    jt.column.cover()

                solution.append(it.row)
                if _solve():
                    return True
                solution.pop()

                for jt in it.iterleft():
                    jt.column.uncover()

            lowest.uncover()
            return False

        if not _solve():
            return None

        return solution


def range2d(width: int, height: int):
    for y in range(height):
        for x in range(width):
            yield x, y


def problem_2580():
    sudoku = [list(map(lambda number: int(number) - 1, input().split())) for _ in range(9)]
    # matrix column size: 324 (81 + 81 + 81 + 81)
    #   * 9x9 positional = 81
    #   * 9 vertical = 81
    #   * 9 horizontal = 81
    #   * 3x3 cubic = 81

    vertical = [[False for _ in range(9)] for _ in range(9)]
    horizontal = [[False for _ in range(9)] for _ in range(9)]
    cubic = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]
    
    for x, y in range2d(9, 9):
        value = sudoku[y][x]
        if value != -1:
            vertical[x][value] = True
            horizontal[y][value] = True
            cubic[y // 3][x // 3][value] = True

    dlx = DancingLinks(324)
    coords = []

    def makerow(x: int, y: int, value: int):
        row = [False for _ in range(324)]
        for pos in [
            81 * 0 + (y * 9 + x),
            81 * 1 + (x * 9 + value),
            81 * 2 + (y * 9 + value),
            81 * 3 + (((y // 3) * 3 + (x // 3)) * 9 + value),
        ]:
            row[pos] = True

        return row

    for x, y in range2d(9, 9):
        value = sudoku[y][x]
        if value != -1:
            dlx.appendrow(makerow(x, y, value))
            coords.append((x, y, value))

        else:
            for candidate in range(0, 9):
                if vertical[x][candidate] or horizontal[y][candidate] or cubic[y // 3][x // 3][candidate]:
                    continue

                dlx.appendrow(makerow(x, y, candidate))
                coords.append((x, y, candidate))

    for row in dlx.solve():
        x, y, value = coords[row]
        sudoku[y][x] = value

    for y in range(9):
        for x in range(9):
            value = sudoku[y][x] + 1
            print(value, end=' ')
        print()


problem_2580()
'''
'''
import sys

def remove_number(loc, n):
    r, c = loc
    row[r] &= ~(1 << n-1)
    col[c] &= ~(1 << n-1)
    sqr[(r//3)*3 + c//3] &= ~(1 << n-1)


def set_number(loc, n):
    r, c = loc
    row[r] |= (1 << n-1)
    col[c] |= (1 << n-1)
    sqr[(r//3)*3 + c//3] |= (1 << n-1)

def get_number(loc):
    r, c = loc
    return row[r] & col[c] & sqr[(r//3)*3 + c//3]

def dfs(start):
    global board
    if start >= len(check_list):
        for b in board: print(" ".join(map(str, b)))
        sys.exit(0)
    loc = check_list[start]
    number = get_number(loc)
    cnt = 1
    while(number):
        if (number & 1):
            board[loc[0]][loc[1]] = cnt
            remove_number(loc, cnt)
            dfs(start+1)
            set_number(loc, cnt)
        number >>= 1
        cnt += 1

board, check_list = [], []
b = 0b111111111
row, col, sqr = [b] * 9, [b] * 9, [b] * 9

for r in range(9):
    board.append(list(map(int, input().split())))
    for c in range(9):
        if board[r][c]: remove_number((r,c), board[r][c])
        else: check_list.append((r,c))
dfs(0)
'''
'''
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

0 0 0 0 0 0 0 0 9
0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 0 7
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 4
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 1

0 0 0 0 0 0 0 0 0
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
0 0 0 0 0 0 0 0 0
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
0 0 0 0 0 0 0 0 0

0 0 0 0 4 3 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 5 0 0 0 0
0 8 0 7 0 0 0 2 0
0 6 0 0 0 0 0 0 3
0 0 0 0 0 0 0 4 0
0 0 5 8 0 0 6 0 0
4 0 0 1 0 0 0 0 0
3 0 0 0 0 0 5 0 0
'''
