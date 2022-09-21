'''
꿀 따기

N개의 장소. 서로 다른 벌 두 마리. 하나는 벌통
벌통으로 가며 지나가는 모든 칸에서 꿀 땀. 시작장소는 못 땀.

입력
장소 수 n
꿀 딸  수 있는 양 제시.

출력
가능한 최대 꿀
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
suml = [nl[0]]+[0]*(n-1)
for i in range(1, n):
    suml[i] = suml[i-1]+nl[i]
# suml[j]-suml[i-1] -> 인덱스 i부터 j까지 합. i가 0이라면 suml[j] 로 표현.
# sum[i] -> i번째까지 합.
ans = 0
for i in range(1, n-1):
    bbh = suml[n-1] - nl[i] - nl[0] + suml[n-1] - suml[i]
    bhb = suml[i] - nl[0] + suml[n-2] - suml[i-1]
    hbb = suml[i-1] + suml[n-2] - nl[i] 
    ans = max(bbh, bhb, hbb, ans)
print(ans)


























