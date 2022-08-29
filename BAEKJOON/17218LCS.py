'''
비밀번호 만들기

LCS이다.

입력
한 줄 문자
한 줄 문자

출력
최대 길이 문자열
'''

s1, s2 = ' ' + input().rstrip(), ' ' + input().rstrip()
l1, l2 = len(s1), len(s2)
g = [['']*(l2) for _ in range(l1)] # 여기서 세로 가로 잘 판단하자.....

for i in range(1, l1):
    for j in range(1, l2):
        if s1[i] == s2[j]:
            g[i][j] = g[i-1][j-1] + s1[i]
        else:
            if len(g[i][j-1]) >= len(g[i-1][j]):
                g[i][j] = g[i][j-1] # or pass
            else:
                g[i][j] = g[i-1][j]

print(g[-1][-1])


'''
그래프 짤 때 i, j 위치 잘 잡아줘야 한다!!!!! 그림을 잘 그려ㅑ놔야 편한듯.
추가 할 때는 대각선 위에서. 위에서 붙일 경우 EA EAA EAAA이런식으로 될 수 있음. EA EA EA로 되야 하므로.
대각선!
'''

