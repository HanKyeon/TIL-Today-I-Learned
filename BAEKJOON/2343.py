'''
기타 레슨

n개 강의. 강의 순서 바꾸면 안됨. i번과 j번을 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의를 같은 블루레이에 녹화해야 한다.
블루레이 갯수 줄이려 함. m개 블루레이에 모든 동영상 녹화. m개 블루레이 크기는 같아야 한다.
각 강의 길이가 분단위로 제시, 가능한 블루레이 크기 중 최소를 구해라.

입력
강의 수 n m 제시

출력
가능한 블루레이 크기 중 최소 출력
'''
import sys
input = sys.stdin.readline

def check(num):
    global m
    cnt, hap = 0, 0
    for i in nl:
        if hap+i > num: cnt+=1; hap = i; continue
        hap+=i
        if cnt > m: return False
    return False if cnt and cnt+1 > m else True

n, m = map(int, input().rstrip().split())
nl = list(map(int, input().rstrip().split()))
sta, end = max(nl), sum(nl)
ans = 0

while sta <= end:
    mid = (sta+end)//2
    if not check(mid): sta = mid+1; continue
    end = mid-1; ans = mid

print(ans)