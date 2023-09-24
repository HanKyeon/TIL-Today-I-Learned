'''
트리의 순회

n개 정점 이진 트리. 1부터 n
인오더와 포스트오더 제시, 프리오더 구해라.
프리오더 = 전위 = 루트 좌 우
인오더 = 중위순회 = 좌 루트 우
포스트오더 = 후위 순회 = 좌 우 루트

입력
n 제시
인오더 제시 중위순회
포스트오더 제시 후위순회

출력
프리오더 제시
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

n = int(input().rstrip())
inor, postor = list(map(int, input().rstrip().split())), list(map(int, input().rstrip().split()))
preor = [0]*(n+1)
for i in range(n): preor[inor[i]] = i

def preorder(l1, r1, l2, r2):
    if (l1 > r1) or (l2 > r2): return
    root = postor[r2]
    l = preor[root] - l1
    r = r1 - preor[root]
    print(root, end = " ")
    preorder(l1, l1 + l - 1, l2, l2 + l - 1)
    preorder(r1 - r + 1, r1, r2 - r, r2 - 1)

preorder(0, n - 1, 0, n - 1)



'''
# 시간초과 메모리 초과
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def recursive(l1, r1, l2, r2):
    if l1 - r1 != l2 - r2: return
    if l1 >= r1 and l2 >= r2: return
    for i in range(r1-l1):
        if inor[l1+i] == postor[r2-1]:
            preor.append(postor[r2-1])
            recursive(l1, l1+i, l2, l2+i)
            recursive(l1+i+1, r1, l2+i, r2-1)

n = int(input().rstrip())
inor, postor = list(map(int, input().rstrip().split())), list(map(int, input().rstrip().split()))
preor = []
recursive(0, n, 0, n)
print(*preor)
'''