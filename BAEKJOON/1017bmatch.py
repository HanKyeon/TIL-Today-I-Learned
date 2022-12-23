'''
수 리스트 존재.
이를 짝지어 각 쌍의 합이 소수가 되게 하려 한다.
모든 수를 다 짝지었을 때, 첫번째 수와 어떤 수를 짝지었는지 오름차순으로 출력하는 프로그램 작성.

입력
리스트 크기 n 50이하 짝수 자연수
숫자 리스트, 1000이하 자연수, 중복x

출력
정답 출력. 없으면 -1 출력
'''
import sys
input = sys.stdin.readline

def matching(idx):
    global n
    for i in range(n):
        if v[i] or nl[idx]+nl[i] not in sosu or i == idx or (idx == 0 and i in ans) or (i == 0 and idx in ans):
            continue
        v[i] = 1
        if connect[i] < 0 or matching(connect[i]):
            connect[i] = idx
            return True
    return False

sosu = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 
1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 
1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999}

n = int(input())
nl = list(map(int, input().rstrip().split()))
ans = set()
fla = False
while True:
    connect = [-1]*n
    for i in range(n):
        v = [0]*n
        matching(i)
    for i in connect:
        if i < 0:
            fla = True
            break
    if fla:
        break
    ans.add(connect[0])
ans = list(map(lambda x: nl[x], ans))
ans.sort()
if ans:
    print(*ans)
else:
    print(-1)



# # 에라토스테네스의 체
# numz = [False]*2 + [True]*1999
# for i in range(2001):
#     if numz[i]:
#         k = 2
#         while i*k <= 2000:
#             numz[i*k] = False
#             k+=1
# numz = [i for i, v in enumerate(numz) if v == True]
# print(numz)
'''
# 3년 전 가장 빠른 것
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().strip().split()))

E = list(range(2000))
E[1] = 0
for i in range(2,int(2000**(1/2))+1) :
    if E[i] :
        for j in range(2 * i, 2000, i) :
            E[j] = 0

graph = [[] for _ in range(N)]
for i in range(N-1) :
    for j in range(i+1,N) :
        if E[array[i]+array[j]] :
            graph[i].append(j)
            graph[j].append(i)

def dfs(idx) :
    for nidx in graph[idx] :
        if not visit[nidx] :
            visit[nidx] = 1
            if result[nidx] == -1 or dfs(result[nidx]) :
                result[nidx] = idx
                result[idx] = nidx
                return True
    return False

org_result = [-1]*N
res = []
for idx in graph[0] :
    result = org_result[:]
    result[0],result[idx] = idx,0
    c = 2
    for i in range(1,len(array)) :
        if i == idx : continue
        visit = [0]*N
        visit[0],visit[idx] = 1,1
        if result[i] == -1 and dfs(i) : c += 2
    if c==N : res.append(array[idx])
print(" ".join(map(str,sorted(res))) or -1)
'''
