'''
전위 순회

노드 수 v
간선 v-1개 제시.
부모 자식 순서.
간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열.
1번 정점이 루트.

입력
각 테케 첫줄에 각 테케 정점 총 수 n 제시.
정저 정보

출력
#테케 정답 출력
'''

def preorder(idx):
    if idx:
        print(idx, end=' ')
        preorder(g[idx][0])
        preorder(g[idx][1])

def inorder(idx):
    if idx:
        preorder(g[idx][0])
        print(idx, end=' ')
        preorder(g[idx][1])

def postorder(idx):
    if idx:
        preorder(g[idx][0])
        preorder(g[idx][1])
        print(idx, end=' ')

for testcase in range(1, int(input())+1):
    n = int(input())
    nl = list(map(int, input().rstrip().split()))
    g = [[0, 0] for _ in range(n+1)]
    for i in range(0, len(nl), 2):
        p, c = nl[i], nl[i+1]
        if g[p][0]:
            g[p][1] = c
        else:
            g[p][0] = c
    print(f"#{testcase}", end=' ')
    preorder(1)
    print()

'''
1
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

1 2 4 7 12 3 5 8 9 6 10 11 13
'''