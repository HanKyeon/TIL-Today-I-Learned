'''
암호 만들기

서로 다른 L개의 알파벳 소문자로 구성.
최소 1개의 모음과 최소 2개의 자음으로 구성. 알파벳은 증가하는 순서로 배열.
즉 abc는 맞지만 bac는 아니다.

이 때 사용했을법한 문자의 종류는 c가지. C개의 문자들이 주어졌을 때, 가능성이 있는 암호를 모두 구하시오.

입력
두 정수 L, C 3<=L<=C<=15
C 개의 문자들이 공백으로 제시 알파벳 소문자. 중복 x

출력
한 줄에 하나씩 사전식으로 가능성 있는 암호를 모두 출력.
'''
bg = 'aeiou'
l, c = map(int, input().split())
s = list(input().split())
# moeum, jaeum = [], []
# for i in s:
#     if i in bg:
#         moeum.append(i)
#     else:
#         jaeum.append(i)
ans = []
for i in range(2**len(s)):
    h = []
    mo, ja = 0, 0
    for j in range(len(s)):
        if i & (1<<j):
            h.append(s[j])
    if len(h) == l:
        for k in h:
            if k in bg:
                mo+=1
            else:
                ja+=1
        if mo>=1 and ja>=2:
            ans.append(''.join(sorted(h)))
ans.sort()
for i in ans:
    print(i)





