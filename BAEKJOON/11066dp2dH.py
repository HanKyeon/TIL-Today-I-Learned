'''
파일 합치기

두개의 파일을 합쳐 하나의 임시 파일을 만들고, 이 임시 파일이나 원래의 파일을 계속 두개씩 합쳐 소설의 여러 장들이 연속되도록 파일을 합쳐나가고, 최종적으로 하나로 합친다.
두개의 파일을 합칠 때 필요한 비용이 두 파일 크기의 합이라고 가정 할 때, 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총합을 계산하시오.

예를 들어 C1, C2, C3, C4 40 30 30 50. 30+30 60. 다음 c1과 x1을 합쳐 100. x2와 c4를 합쳐 150. 310이 된다.
소설의 각 장들이 수록되어있는 파일의 크기가 주어졌을 때, 이 파일들을 하나의 파일로 합칠 때 필요한 최소 비용을 계산하는 프로그램을 작성하시오.

입력
테케.
챕터 수 양정수k
파일크기 k개 제시. 파일 크기는 1만 이하.

출력
테케마다 모든 장을 합치는데 필요한 최소 비용 출력.
'''
'''
2차원 DP로 뻗어나가면 된다. 왜? 고려된 최솟값으러 뻗어나가기 때문에.
[i]에서 [j]까지의 최솟값을 dp[i][j]에 저장.

예를 들어, 1에서 6까지라고 가정하면 수많은 조합이 있지만 그 중 최솟값으로 결정이 되기 때문에.
[1][3] 1에서 3까지 최솟값은 1, 23 12, 3 중 하나.
[1][4] : 12, 34 or 1 234 or 123 4 이 중 123, 1 23 중 작은 값이 이미 DP 테이블에 들어가있음.
[1][6] : 따라서, [1] + [2][6], [1][2] + [3][6], [1][3] + [4][6], [1][4] + [1][5], [1][6] 중 가장 작은 값을 대입해주면 됨.
이 때, 값은
sum(chap[1:6]) + dp[1][1] + dp[2][6]

채워야 하는 순서는 한칸 먼저, 그 다음칸, 다음칸, 다음칸.. \\\\\\\ 이 순서라고 보면 될듯.

필요한 것은 0 2를 표현하기 위해서는 01 + 2 / 0 + 12 를 알아야 하므로 01 12 순회해야함. 02 값 생성.
0 3을 표현하기 위해서 0+13 01+23 02+3 을 알아야 하므로 13 23을 알아야함.
다음은 14 24 34를 알아야 04를 구할 수 있다. 그러므로 34 24 14 04 순으로 dp를 해줘야함.

https://www.youtube.com/watch?v=4OdIDIYLHlY
큰 도움 받음. 없었으면 못풀었음.
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    chap = list(map(int, input().rstrip().split()))
    sumli = [0]
    for i in range(n):
        sumli.append(sumli[-1]+chap[i])
    dp = [[0] * n for _ in range(n)]
    for j in range(1, n):
        for i in range(j-1, -1, -1):
            for k in range(j-i):
                print(i, j, k)
                if dp[i][j] == 0:
                    # i부터 j까지는 
                    # i부터 i+k 까지 비용 + i+k+1부터 j까지 비용 + i부터 j까지의 합
                    # 중에서 최솟값이다.
                    # 즉, [1][6]에서 12 36 / 13 46 / 14 56 중에서 가장 큰 값이다.
                    dp[i][j] = dp[i][i+k] + dp[i+k+1][j] + sumli[j+1]-sumli[i] # sum(chap[i:j+1])
                    # for s in dp:
                    #     print(*s)
                    continue
                dp[i][j] = min(dp[i][i+k] + dp[i+k+1][j] + sumli[j+1]-sumli[i], dp[i][j])
                # for s in dp:
                #     print(*s)
    print(dp[0][-1])






def solve():
    N, A = int(input()), [0] + list(map(int, input().split()))# S[i]는 1번부터 i번까지의 누적합
    S = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i]
    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
    DP = [[0 for i in range(N+1)] for _ in range(N+1)]
    for i in range(2, N+1):# 부분 파일의 길이
        for j in range(1, N+2-i):# 시작점
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1]) #[j:j+i-1]
            for s in DP:
                print(*s)
for _ in range(int(input())):
    solve()








