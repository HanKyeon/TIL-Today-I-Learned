'''
노드의 합

입력
테케T
노드 N 리프노드M 출력노드L
노드 번호와 자연수 제시.

출력
지정된 노드에 저장된 값 출력.
'''

for testcase in range(1, int(input())+1):
    n, m, l = map(int, input().rstrip().split())
    nz = [0]*(n+1)
    for _ in range(m):
        nod, val = map(int, input().rstrip().split())
        nz[nod] = val
    for i in range(n, 1, -1):
        if 1 <= i//2 <= n:
            nz[i//2] += nz[i]
    print(f"#{testcase} {nz[l]}")





