'''
개미 전사

창고를 터는데, 연속으로 털 수 없으먀, 2칸 떨어져서 털어도 되고 3칸 떨어져서 털어도 된다.
가장 많이 털 수 있는 식량의 최댓값
창고 갯수 n은 3이상 100이하
각 창고내 식량의 값은 0이상 1000 이하
'''
# 창고 갯수
n = int(input())
# 창고 별 식량의 양
arr = list(map(int, input().split()))
# 최대 누적 식량을 기록하는 dp 테이블. 창고 갯수가 최대 100이므로 100개면 됨. 인덱스는 n-1
d = [0] * 100
# n은 3 이상이므로, 
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
# i-1번째 창고에서 얻을 수 있는 최대 식량의 수는
# d[i]와 d[i-1]과 d[i-2]+arr[i] 두 값을 비교해서 큰 값이다. i-3부터는 이미 앞쪽에서 고려된다.
for i in range(2, n) :
    d[i] = max(d[i - 1], d[i - 2] + arr[i])

print(d[n-1])


