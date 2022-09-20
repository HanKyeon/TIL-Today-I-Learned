'''
전국시대

전국시대엔 n개의 국가 존재. 1부터 n까지 번호.
병력 보유. m개 기록 제시.
동맹 : 두 나라 동맹 맺기. 병력 하나로
전쟁 : 두 나라 전쟁. 병력이 더 많은 나라가 승리, 패배하면 속국. 남은 병력은 승리한 나라의 병력에서 패배한 나라의 병력을 뺀 수치. 병력이 같을 경우 멸망.

친구친구는 친구 속국도 마찬가지임.
끝났을 때 남아있는 국가의 수, 국가의 남은 병력 수를 오름차순 출력하는 프로그램 작성하시오.
동맹/속국은 하나로 취급

입력
국가 수 n ㅣㄱ록 수m 1이상 10만이하
n개 줄에 i번째 국가 병력 Ai 자연수 제시.
m개 줄에 기록 3개 opq 제시. o가 1이면 p랑 q 동맹 o가 2면 p랑 q 전쟁 재동맹 및 동맹전쟁 없음.
출력
남은 국가 수
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # 역시 find해서 넣자.
    if x < y:
        parent[y] = x
        count[x] += count[y]
    else:
        parent[x] = y
        count[y] += count[x]

def war(x, y): # 마찬가지로 find해서 넣기
    if count[x] == count[y]:
        parent[x], parent[y] = 0, 0
        return
    if count[x] < count[y]: # x가 속국화
        count[y] -= count[x]
        parent[x] = y
    else:
        count[x] -= count[y]
        parent[y] = x

n, m = map(int, input().rstrip().split())
parent = list(range(n+1))
count = [0]+[int(input()) for _ in range(n)]
for _ in range(m):
    o, p, q = map(int, input().rstrip().split())
    if o % 2:
        p, q = find(p), find(q)
        if p==0 or q==0:continue
        if p==q: continue
        union(p, q)
    else:
        p, q = find(p), find(q)
        if p==0 or q==0:continue
        if p==q: continue
        war(p, q)
cnt = 0
ans = []
for i in range(1, n+1):
    if parent[i] == i:
        cnt+=1
        ans.append(count[i])
print(cnt)
print(*sorted(ans))