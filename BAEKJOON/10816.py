'''
숫자 카드 2

정수 한 ㅏ적혀있는 카드 n개. 정수 m개 제시, 해당 숫자 카드를 몇 개 갖고 있는지 구해라.

입력
n 제시
정수들 제시 -천만~천만
m 제시.
m개 정수 제시 -천만~천만

출력
m개 수에 대해 몇 개 갖고 있는지 공백 구분 출력
'''
import sys
input = sys.stdin.readline

def check(x): cnt[int(x)+10000000]+=1
def lego(x): print(cnt[int(x)+10000000], end=' ')

cnt = [0]*20000001
n, nl = int(input()), list(map(check, input().rstrip().split()))
m, ml = int(input()), list(map(lego, input().rstrip().split()))

'''
# 왜 내꺼보다 빠른지 모르겠음. 해시에서 꺼내나 list 인덱싱이나 같을텐데... +천만 때문인가?
import sys
stdin = sys.stdin.read().splitlines()
A = map(int,stdin[1].split())
B = map(int,stdin[3].split())
dic = {}
for n in A:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
print(' '.join(str(dic[n]) if n in dic else '0' for n in B))
'''



