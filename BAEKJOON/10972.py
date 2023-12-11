'''
다음 순열

1부터 n까지의 수로 이루어진 순열.
사전순으로 다음에 오는 순여릉ㄹ 구해라.

입력
n 제시
순열 제시

출력
주어진 순열의 다음에 오는 순열 출력. 마지막인 경우 -1 출력
'''
n = int(input())
nl = list(map(int, input().split()))

for i in range(n-1, 0, -1): # 맨 뒤 값부터 시작
    if nl[i-1] < nl[i]:
        for j in range(n-1, 0, -1): # 다시 맨 뒤 값부터 큰 값찾기
            if nl[i-1] < nl[j]:
                nl[i-1], nl[j] = nl[j], nl[i-1] # 둘 값을 swap
                nl = nl[:i] + sorted(nl[i:])
                for i in nl:
                    print(i, end=' ')
                exit()
print(-1)