'''
교환

0으로 시작하지 않는 정수 n 제시.
이 대 m을 정수 n의 자릿수라고 했을 때 다음과 같은 연산 k번 수행.
1. 1<=i<j<=m인 i와 j를 고른다.
그 다음 i번 위치와 숫자 j번 위치의 숫자를 바꾼다. 이 때, 바꾼 수가 0으로 시작하면 안된다.
위의 연산을 k번 했을 때 나올 수 있는 수의 최댓값ㅇ르 구해라.

입력
정수 n과 k 제시. n은 100만 이하 자연수, k는 10보다 작거나 같은 자연수.

출력
연산 k번 했을 때, 만들 수 있는 가장 큰 수 출력. 연산을 k번 할 수 없다면 -1 출력.
'''
# from collections import deque

# def 큐사용():
#     global n
#     tenten = [10**(len(nl)-i-1) for i in range(len(nl))]
#     combi = [] # 갈 수 있는 경우의 수
#     for i in range(len(nl)-1):
#         for j in range(i+1, len(nl)):
#             combi.append((i, j))
#     sets = set() # 중복처리용.
#     ret = 0
#     sets.add((tuple(nl), 0))
#     q = deque()
#     q.append((nl, 0))
#     while q:
#         li, dep = q.popleft()
#         if dep == n+1:
#             break
#         if dep%2 == n%2:
#             vcal = [li[i]*tenten[i] for i in range(len(nl))]
#             ret = max(sum(vcal), ret)
#         for i, j in combi:
#             li[i], li[j] = li[j], li[i]
#             if (tuple(li), (dep+1)%2) not in sets:
#                 sets.add((tuple(li), (dep+1)%2))
#                 q.append((li[:], dep+1))
#             li[i], li[j] = li[j], li[i]
#     return ret
# nl, n = input().rstrip().split() # 입
# nl, n = list(map(int, list(nl))), int(n) # 력
# print(큐사용())


from collections import deque

def changeval(nu:list):
    ret = 0
    for i, v in enumerate(nu):
        ret += v * 10**i
    return ret

def lego(num):
    global k, nlen
    for i in (10,20,30,40,50,60,70,80,90):
        if i == num:
            return -1
    if num < 10:
        return -1
    v0 = [0] * 10**nlen
    v1 = [0] * 10**nlen
    q = deque([(nl, k)])
    if k % 2:
        v1[num] = 1
    else:
        v0[num] = 1
    while q:
        nz, cnt = q.popleft()
        if not cnt:
            continue
        for i in range(nlen-1):
            for j in range(i+1, nlen):
                nnz = nz[:]
                nnz[i], nnz[j] = nnz[j], nnz[i]
                if not nnz[-1]:
                    continue
                nnzval = changeval(nnz)
                if cnt > 0 and (cnt-1)%2 and not v1[nnzval]:
                    v1[nnzval] = 1
                    q.append((nnz, cnt-1))
                elif cnt > 0 and not (cnt-1)%2 and not v0[nnzval]:
                    v0[nnzval] = 1
                    q.append((nnz, cnt-1))
    vv1 = [i for i, v in enumerate(v0) if v]
    return vv1[-1]

n, k = map(int, input().rstrip().split())
nn = n
nl = []
nlen = 0
while nn:
    nl.append(nn%10)
    nn //= 10
    nlen += 1
print(lego(n))


'''
40069 3
96400

10042 2
42010

740792 2
970742
'''

