'''
그룹 나누기

앉고 싶은 두 사람의 출석 번호를 종이에 적어 제출.
한 조의 인원에 제한 없음. 여러장 제출 가능, 여러 사람이 한사람 지목 가능. 전부 다 한 조.
1번부터 n번까지 사람, m장의 신청. 몇개 조?
'''

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # find해서
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for tc in range(1, int(input())+1):
    n, m = map(int, input().rstrip().split())
    parent = list(range(n+1))
    nl = list(map(int, input().rstrip().split()))
    for i in range(0, 2*m, 2):
        n1, n2 = find(nl[i]), find(nl[i+1])
        if n1 == n2:
            continue
        union(n1, n2)
    ans = 0
    for i in range(1, n+1):
        if parent[i] == i:
            ans += 1
    print(f"#{tc} {ans}")

