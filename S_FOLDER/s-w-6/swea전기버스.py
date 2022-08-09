'''
전기버스

이동한도 k
0에서 n까지 가야함
m개의 충전기
충전기 위치

출력
#t 최소 충전 횟수
#t 도착 못할 시 0
'''
# k 거리 이내에 뒤부터 확인하여 처음 있는 정류소에 정차
def ml(x, c) :
    global k # k 쓸라고
    ln = len(cl) # n 땜빵
    if x+1 < ln-k and sum(cl[x+1:x+k+1]) == 0 : # 받은 x값 뒤 k개가 다 0이면
        return 0 # 못간다
    elif x+1 >= ln-k : # 종착지가 k범위 안이면 c 리턴
        return c
    if x+1 < ln-k : # 아니면 뒤에서 훑어서 처음 만나는 1에서 충전한 뒤, 재귀
        for i in range(x+k, x, -1) :
            if cl[i] == 1 :
                c += 1
                return ml(i, c)
# 테케
for testcase in range(1, int(input())+1):
    # 입력
    k, n, m = map(int, input().split())
    cl = [0] * (n+1)
    for i in list(map(int, input().split())) :
        cl[i] = 1
    # 출력
    print(f"#{testcase} {ml(0, 0)}")





