'''
N-QUEEN
'''
def nqueen(h): # 인자는 y축의 값ㅇㅣ다. 합, 차 계산을 위해 받아준다.
    global n, v, hap, cha, ans
    if sum(v) == n: # sum이 n까지 안오면 애초에 탈락해서 실행 안한다.
        ans += 1
        return
    for i in range(n):
        if v[i] == 0 and hap.get(h+i, 0) == 0 and cha.get(h-i, 0) == 0:
            v[i], hap[h+i], cha[h-i] = 1, 1, 1
            nqueen(h+1)
            v[i], hap[h+i], cha[h-i] = 0, 0, 0

for testcase in range(1, int(input())+1):
    n = int(input())
    v = [0]*n # 세로 방문 확인용
    hap, cha = {}, {} # 대각선 방문 확인용
    ans = 0 # 정답
    nqueen(0)
    print(f"#{testcase} {ans}")










