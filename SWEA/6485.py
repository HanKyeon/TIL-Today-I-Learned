'''
삼성시의 버스 노선

5000개의 버스정류장
N은 1이상 500이하
Ai Bi는 1이상 5000이하
P 1이상 500이하
Cj 1이상 5000이하

#t 정류장버스노선갯수 정류장버스노선갯수 정버노 정버노

'''
# 
for testcase in range(1, int(input())+1):
    N = int(input())
    buz = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    cz = [0] * 5001
    cs = [int(input()) for _ in range(P)]
    print(f"#{testcase}",end=' ')
    for i in range(P) :
        for x, y in buz :
            if cs[i] > x and cs[i] > y :
                continue
            elif cs[i] < x and cs[i] < y :
                continue
            else :
                cz[cs[i]] += 1
        print(cz[cs[i]], end=' ')
    print()
    







