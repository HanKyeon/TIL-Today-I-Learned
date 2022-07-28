'''
첫줄에 N과 L
N은 10억 이하 양의 정수 + 0
L은 2이상~100이하

합이 N이면서 연속된 L만큼의 수

연속된 수를 첫째줄에 공백으로 출력

l이 100 이하 일 때 리스트 반환. 넘어가면 -1.


2~100까지 시작점과 끝점을 같이 훑으면서
합이 N이상이면 start를 늘리고 N이하면 end를 늘리면서
합이 N일 때 찾는다. 이 때, len()이 L 이상일 때 받아서
len()이 기존 것보다 짧을 때 갱심
'''
#n, l = map(int,(input().split()))

# dt = list(range(n+1))

#sta, end = 0, 0
# le = n
#d = []
# list(range(sta, end)) : 시간초과
# dt[sta:end] : 메모리 초과 dt에서.
'''
while end < n + 1 :
    if sum(dt[sta:end]) < n :
        end += 1
    elif sum(dt[sta:end]) == n :
        if len(dt[sta:end]) >= l and len(dt[sta:end]) < le :
            d = dt[sta:end]
            le = len(d)
        end += 1
    elif sum(dt[sta:end]) > n :
        sta += 1
'''

# for로 만들어보기

# x+1부터 x+i까지의 합은 (i/2) * (2*x+i+1) == N == ix + (i/2) * (i+1)
# (i/2) * (2*x+i+1) == N == ix + (i/2) * (i+1)
# N - (i/2) * (i+1) == ix
# (i/2) * (2*x+i+1) == N
# 위 식을 만족하는 가장 작은 i값을 찾고, x+1부터 x+i까지의 리스트 반환.
# n/i - i/2 - 1/2
n, l = map(int,(input().split()))
le = l
x = 0
for i in range(l, 101) :
    if (2*n - i**2 + i) % (2*i) == 0 :
        le = i
        x = int((2*n - i**2 + i) // (2*i))
        break
d = list(range(x, x+le))
d = map(str, d)

if x < 1 or le > 100 or d == False :
    print('-1')
else :
    print(' '.join(d))


