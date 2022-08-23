'''
우원재의 메모리 복구하기

메모리를 바꾸면 하나로 뒤에 쭉 먹는다.
원래 값으로 복구하기 위한 최소 수정 횟수를 구해라.

입력
테케T
원래 메모리

출력
#테케 갯수
'''

for t in range(1,int(input())+1):
    b,a='0',0
    for i in input():
        if i!=b:a,b=a+1,i
    print(f"#{t} {a}")

for testcase in range(1, int(input())+1):
    s = input() # 원래 값
    b, ans = '0', 0 # 처음에는 0이고 바꾸는 횟수도 0이다.
    for i in s: # 훑으면서 숫자 달라질 때마다 ans+1
        if i == b:
            continue
        elif i != b:
            b = i
            ans += 1
    print(f"#{testcase} {ans}")

for t in range(1,int(input())+1):
    b,a='0',0
    for i in input():
        if i!=b:a+=1
    print(f"#{t} {a}")