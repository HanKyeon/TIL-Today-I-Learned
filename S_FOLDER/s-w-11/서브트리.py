'''
서브 트리

서브트리 노드 갯수 알아내는 프로그램 작성
부모 없는 노드가 전체의 루트 노드.

입력
테케T
간선 갯수e와 n 제시
E개의 부모 자식 노드 번호 쌍.
1번부터 E+1번까지 노드 존재. 1이상 1000이하 E, 그냥 트리임. 1이상e+1이하n
'''

def sh(nod):
    global cnt
    if not nod:
        return
    cnt += 1
    sh(g[nod][0])
    sh(g[nod][1])

for testcase in range(1, int(input())+1):
    e, n = map(int, input().rstrip().split())
    nl = list(map(int, input().rstrip().split()))
    g = [[0, 0] for _ in range(e+2)]
    for i in range(0, e*2, 2):
        a, b = nl[i], nl[i+1]
        if not g[a][0]:
            g[a][0] = b
        else:
            g[a][1] = b
    cnt = 0
    sh(n)
    print(f"#{testcase} {cnt}")
