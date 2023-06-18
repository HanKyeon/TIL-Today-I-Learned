'''
회사에 있는 사람

로그 수 n
이름 enter
이름 leave
회사에 남아있는 사람 사전순의 역순으로 출력
'''
import sys
input = sys.stdin.readline

ans = set()
for _ in range(int(input())):
    a, b = input().rstrip().split()
    if b == "enter":
        ans.add(a)
    else:
        ans.remove(a)
ans = sorted(ans, reverse=True)
for i in ans:
    print(i)
