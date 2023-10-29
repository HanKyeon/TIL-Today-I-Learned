'''
뒤집기

0과 1로만 이루어진 문자열 존재.
뒤집기는 0을 1로 1을 0으로 바꿈.
하나의 숫자로 바꾸는데 걸리는 최소 뒤집기 수

입력
s 제시

출력
최소 행동 횟수 출력
'''
s = input()
cnt = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]: continue
    cnt += 1
print(cnt//2)


