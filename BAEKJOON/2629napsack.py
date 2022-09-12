'''
양팔저울

양팔 저울과 추가 제시된다.
합, 차 모두 고려한다.

입력
추의 갯수 제시. 30개 이하.
추의 무게 가벼운 것부터 차례로 제시.
같은 무게의 추가 여러개 있을 수도 있다. 추의 무게는 500g 이하.
구슬 7개 이하.
구슬 무게 제시. 구슬 무게는 40000이하 자연수

출력
각 구슬에 대해 잴 수 있는지. 가능하면Y 불가능하면 N
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
m = int(input())
ml = list(map(int, input().rstrip().split()))
dp = [False]*(sum(nl)+1) # dp
dp[0] = True # 무게 0은 무조건 가능
dp[nl[0]] = True # 첫 무게 메모

for i in range(1, n): # 첫무게 메모 했으니 다음 무게부터 진행
    bs = nl[i] # 계속 호출하기 미안해서 변수에 할당
    l = set() # 여기 담아서 한방에 메모 할 것
    for j in range(len(dp)): # dp 전체를 훑으면서 전체의 True에 대해 진행
        if dp[j] == True:
            if 0<=j+bs<=sum(nl): # True인 것과 현재 nl[i]의 합이 범위 내라면
                l.add(j+bs) # 메모 할 것에 저장
            if 0<=j-bs<=sum(nl): # 그 차이가 범위 내면
                l.add(j-bs) # 메모 할 것
            if 0<=bs-j<=sum(nl): # 반대 차가 범위 내면
                l.add(bs-j) # 메모 할 것
    while l: # 메모 할 것들을 하나하나 메모
        nn = l.pop()
        dp[nn] = True

for i in ml:
    if i > sum(nl): # 구슬 전체 합보다 큰 값이면
        print('N', end=' ') # 불가능
        continue
    if dp[i]: # dp[i]가 True라면 Y
        print('Y', end=' ')
    else: # dp[i]가 False라면 N
        print('N', end=' ')
print()





'''
3
1 5 17
18
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

0 1 4 6 
'''





