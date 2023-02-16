'''
크로아티아 알파벳

몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
c= c- dz= d- lj nj s= z=
c, d, s, z, j만 앞

입력
100글자의 단어 제시. 소문자와 -=로 이루어짐.
단어는 크로아티아 알파벳으로 이루어져 있다.

출력
단어 중 몇 개가 크로아티아 알파벳으로 이루어져 있는지 출력
'''
import sys
input = sys.stdin.readline

s = input().rstrip()
cl = len(s)
p = 0
ans = 0
while p < cl-1:
    v = s[p]
    v2 = s[p+1]
    if v == "c":
        if v2 == "=" or v2 == "-":
            ans += 1
            p += 2
            continue
    elif v == "d":
        if v2 == "-":
            ans += 1
            p+=2
            continue
        elif v2 == "z":
            try:
                v3 = s[p+2]
                if v3 == "=":
                    ans += 1
                    p += 3
                    continue
            except:
                pass
    elif v == "s" and v2 == "=":
        ans += 1
        p+=2
        continue
    elif v == "z" and v2 == "=":
        ans += 1
        p+=2
        continue
    elif v == "l" and v2 == "j":
        ans += 1
        p+=2
        continue
    elif v == "n" and v2 == "j":
        ans += 1
        p+=2
        continue
    ans += 1
    p += 1
if p == cl-1:
    ans += 1
print(ans)



