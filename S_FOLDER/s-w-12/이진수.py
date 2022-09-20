'''
이진수

16진수를 이진수로 만들어라

입력
자릿수n 16진수

출력
#T 답
'''
for tc in range(1, int(input())+1):
    s = input().split()
    a,b = bin(int(s[1],16))[2:],int(s[0])
    while len(a) != b*4:
        a='0'+a
    print(f"#{tc} {a}")