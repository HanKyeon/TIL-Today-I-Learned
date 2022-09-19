'''
0과 1로 이루어진 1차 배열에서 7개 bit를 묶어서 10진수로 출력해라.
ex
00000010001101 입력 시 1 13 출력
입력되는 이진수의 갯수는 7배수로 출력.

입력
테케T
입력 테케마다 한 줄 씩 10진수로 변환된 값 출력

출력
10진수로 변환된 값 출력.
'''
ex = [64, 32, 16, 8, 4, 2, 1]

for testcase in range(1, int(input())+1):
    s = input()
    print(f"#{testcase}", end=' ')
    for i in range(0, len(s), 7):
        ans = 0
        l = s[i:i+7]
        for j in range(7):
            ans += int(l[j]) * ex[j]
        print(ans, end=' ')
    print()

















