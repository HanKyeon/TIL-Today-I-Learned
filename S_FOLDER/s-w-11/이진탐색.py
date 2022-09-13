'''
이진 탐색 = 완전 이진 트리 만들기

1부터 n까지 자연수를 이진 탐색 트리에 저장하려고 한다.
이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 < 현재 노드 < 오른쪽 서브트리 규칙 만족.
추가나 삭제가 없는 경우, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리 만들 수 있음.

완전 이진 트리의 노드 번호는 루트를 1번으로 하고, 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.
N이 주어졌을 때, 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(n이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.

입력
테케T 1이상 50이하
테케N 제시.

출력
#T 루트노드값 n//2노드값
'''

def inorder(idx):
    global num
    if g[idx][0] == 0 and g[idx][0] == 0:
        heap[idx] = num
        num += 1
        return
    if g[idx][0] != 0:
        inorder(g[idx][0])
    heap[idx] = num
    num += 1
    if g[idx][1] != 0:
        inorder(g[idx][1])

for testcase in range(1, int(input())+1):
    num = 1
    n = int(input())
    heap = [0] * (n+1)
    g = [[0,0] for _ in range(n+1)]
    for i in range(1, n//2+1):
        if 0 <= i*2 <= n:
            g[i][0] = i*2
        if 0 <= i*2+1 <= n:
            g[i][1] = i*2+1
    inorder(1)
    print(f"#{testcase}", end=' ')
    print(heap[1], heap[n//2])


'''
# 그냥 이진 탐색 트리를 만드는 것.

from collections import deque


for testcase in range(1, int(input())+1):
    n = int(input())
    heap = [0]
    # for i in range(1, n+1):
    heap = list(range(n+1))
    dp = heap[:]
    ndp = []
    while dp != ndp:
        ndp = heap[:]
        q = deque([1])
        while q:
            p = q.popleft()
            c1, c2 = p*2, p*2+1
            dl = [heap[p]]
            if c1<len(heap):
                dl.append(heap[c1])
            if c2<len(heap):
                dl.append(heap[c2])
            dl = sorted(dl)
            if len(dl) == 1:
                continue
            elif len(dl) == 2:
                heap[c1], heap[p] = dl[0], dl[1]
                q.append(c1)
            elif len(dl) == 3:
                heap[c1], heap[p], heap[c2] = dl[0], dl[1], dl[2]
                q.append(c1)
                q.append(c2)
        dp = heap[:]

    print(heap)
    print(f"#{testcase}", end=' ')
    print(heap[1], heap[n//2])
'''

'''
    q = deque([n])
    while q:
        c = q.popleft()
        p = c//2
        if c%2:
            if heap[c] < heap[p]:
                heap[c], heap[p] = heap[p], heap[c]
        else:
            if heap[c] > heap[p]:
                heap[c], heap[p] = heap[p], heap[c]
        if c != 0:
            q.append(c-1)
'''













