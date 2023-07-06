'''
30

30 배수 중 가장 큰 수.

입력
n

출력
30배수 중 가장 큰 수 출력. 없다면 -1 출력
'''
n = input()
if "0" not in n:
    print(-1)
    exit()
ans = 0
hap = 0
for i in n:
    hap += int(i)
if hap%3:
    print(-1)
else:
    print("".join(sorted(n, reverse=True)))