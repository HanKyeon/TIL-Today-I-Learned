'''
시험 감독

총 n개의 시험장이 있고, 각각 시험장마다 응시자들.
i번 시험장에 있는 응시자 수 Ai명.
감독관은 총감/부감 두종류. 총감은 시험장 당 B명, 부감은 C명 감독.
각각 시험장에 총감은 1명, 무감 자율.
모두 감시 할 때 필요한 감관 수 최솟값

입력
시험장 갯수n
각 시험장 응시자 수 Ai
총감 감독수, 부감 감독수 제시
'''
import sys
input= sys.stdin.readline

n = int(input())
al = map(int, input().rstrip().split())
b, c = map(int, input().rstrip().split())
ans = n
for i in al:
    a = i-b
    if a <= 0:
        continue
    if a % c:
        ans += a//c +1
    else:
        ans += a//c
print(ans)





