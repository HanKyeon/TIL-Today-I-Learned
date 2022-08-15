'''
동전 0

준규가 가지고 있는 동전은 N종류, 굉장히 많음.
적절히 사용하여 그 가치의 합을 K로 만들려 한다.
필요한 동전 최소 갯수는

입력
첫째줄에 N, K. N은 1이상 10이하 K는 1이상 1억이하
둘째줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 제시.
Ai는 1이상 100만이하 A1 = 1 i>=2인 경우 Ai는 Ai-1의 배수
A1이 1인 경우에는 쭉 배수로 주어져서 그리디한 방법이 먹힌다..... 는것 같다.

출력
K원을 만드는데 필요한 동전 갯수 최솟값
'''
n, k = map(int, input().split())
nl = [int(input()) for _ in range(n)]
c = 0

gl = sorted(nl, reverse=True)
for i in gl:
    if k == 0 :
        break
    if k >= i:
        c += k//i
        k %= i

print(c)


