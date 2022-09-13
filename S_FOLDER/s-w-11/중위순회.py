'''
중위순회

in-order
10개 테케.
노드 갯수 100개 이하.
완전 이진 트리 형식. 노드 당 하나의 알파벳.

입력
테케
노드 수 n, n개 줄에 걸쳐 정점 정보 제시.
해당 정점의 알파벳, 해당 정점의 좌식, 우식 정점 번호 제시.

처ㅜㄹ력
#테케 문자
'''

def inorder(idx):
    if idx:
        inorder(g[idx][0])
        print(dli[idx], end='')
        inorder(g[idx][1])

for testcase in range(1, 11):
    n = int(input())
    dli = ['' for _ in range(n+1)]
    g = [[0, 0] for _ in range(n+1)]
    for _ in range(n):
        li = list(input().rstrip().split())
        if len(li) == 2:
            dli[int(li[0])] = li[1]
        elif len(li) == 3:
            dli[int(li[0])] = li[1]
            g[int(li[0])][0] = int(li[2])
        elif len(li) == 4:
            dli[int(li[0])] = li[1]
            g[int(li[0])][0] = int(li[2])
            g[int(li[0])][1] = int(li[3])

    print(f"#{testcase}", end=' ')
    inorder(1)
    print()



'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''









