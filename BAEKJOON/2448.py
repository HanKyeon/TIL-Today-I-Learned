'''
별 찍기

싸피 처음할 때 파이썬 참고자료에서 먼저 찍는 별 모양이다.
'''
n = int(input())
stars = [[' ']*2*n for _ in range(n)]
def recursion(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"
    else:
        newSize = size//2
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)
recursion(0, n - 1, n)
for star in stars:
    print("".join(star))


n = int(input())
graph = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]


def recursive(N, before):
    after = [[" "] * (2 * 2 * N - 1) for _ in range(2 * N)]
    for i in range(N):
        after[i][N:N+2*N-1] = before[i]

    k = 0
    for i in range(N, 2 * N):
        after[i][:2*N] = before[k]
        after[i][2 * N:2 * N+len(before[k])] = before[k]
        k += 1

    if 2 * N == n:
        return after

    return recursive(2 * N, after)


if n == 3:
    result = graph
else:
    result = recursive(3, graph)

for i in result:
    print("".join(i))

'''
import sys
def a(N):
    if N == 3:
        return ["  *  "," * * ","*****"]
    N //= 2
    x = a(N)
    A = [" " * N + i + " " * N for i in x]
    B = [i + " " + i for i in x]
    return A + B
input = sys.stdin.readline
N = int(input())
print("\n".join(a(N)))
'''
