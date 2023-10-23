'''
베스트셀러

가장 많이 팔린 책 제목 출력

입력
n제시
제목 제시

출력
제목 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
d = {}
for i in range(n):
    name = input()
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1
        
c = max(d.values())
ans = []
for key, value in d.items():
    if value == c:
        ans.append(key)
ans = sorted(ans)
print(ans[0])


