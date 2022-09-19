'''
단어 수학

n개의 단어로 이뤄져 있으며, 각 단어는 대문자로만. 대문자를 0부터 9 중 하나로 바꿔서 n개의 수를 합해야한다. 같은 알파벳은 같은 숫자로, 두 개 이상의 알파벳이 같은 숫자로 바뀌면 안된다.
예를 들어 GCF + ACDEB를 계산한다고 할 때, a9 b4 c8 d6 e5 f3 g7로 하면 두 수의 합은 99437이 된다.
n개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성해라.

입력
단어 갯수 n 1이상 10이하 제시.
n개 줄에 단어가 한 줄에 하나씩 제시. 단어는 알파벳 대문자로만. 단어에 포함 된 알파벳은 최대 10개. 최대 길이는 8.

출력
주어진 단어 합의 최댓값.
'''
import sys
input = sys.stdin.readline

n = int(input())
di = {}
for _ in range(n):
    s = input().rstrip()
    s = 'x' * (8-len(s)) + s
    for i in range(len(s)):
        if s[i] == 'x':
            continue
        if di.get(s[i], 0):
            di[s[i]] += 10**(7-i)
        else:
            di[s[i]] = 10**(7-i)

a = sorted(list(di.values()))
ans = 0
val = 9
while a:
    num = a.pop()
    ans += num*val
    val -= 1
print(ans)


'''
예외처리
ACC
CC
CC
CC
CC
CC
CC
CC
CC
CC

1780 : A가 9 C가 8
1790 : A가 8 C가 9
'''








