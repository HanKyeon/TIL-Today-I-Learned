'''
가장 긴 증가하는 부분 수열 LIS

LIS 구하기. 시간 복잡도 개선이 안되는 dp밖에 떠오르지 않아서 참고했음.
https://jainn.tistory.com/90
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
ans = [0]

for i in nl:
    if ans[-1] < i:
        ans.append(i)
    else:
        sta = 0
        end = len(ans)
        while sta < end:
            mid = (end+sta)//2
            if ans[mid] < i:
                sta = mid+1
            else:
                end = mid
        ans[end] = i
print(ans)
print(len(ans)-1)

'''
기존에 들어간 값을 치환 해주면서 간다.
why? : 이분탐색으로 그 값보다 크고 작은 값 사이에서 가장 가까운 수의 위치를 찾아간다. 그 곳에 대신 넣게 되는데, 원래는 그러면 갱신 안해도 되지만 해준다는 것 같다.
더 큰 값이라면 우측에 붙이고, 큰 값보다 작다면 그 사이의 값에 치환되는 방식인듯.
'''



