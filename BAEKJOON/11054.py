'''
가장 긴 바이토닉 부분 수열

1 5 2 1 4 3 1 5 2 1
1 2 3 4 5 2 1 : 가장 긴 바이토닉 수열. 증가하다 감소하는것.

입력
수열크기n 1이상 1000이하
수열a 1이상 1000이하

출력
가장 긴 바이토닉 수열의 길이 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().rstrip().split()))
mnl = list(reversed(nl))
pdp, mdp = [1]*n, [1]*n
for i in range(1, n):
    for j in range(i):
        if nl[i] > nl[j]:
            pdp[i] = max(pdp[i], pdp[j] + 1)
        if mnl[i] > mnl[j]:
            mdp[i] = max(mdp[i], mdp[j] + 1)
mdp = list(reversed(mdp))

ans = max(map(sum, zip(pdp, mdp)))

print(ans-1)
