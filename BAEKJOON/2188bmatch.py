'''
축사 배정

축사를 m개 칸으로 구분 한 칸 당 한마리의 소만 입주.
소가 희망하는 축사 외에는 들어가기 싫어함.
최대한 많은 수의 소가 축사에 들어갈 수 있도록 하는 프로그램 작성.
축사의 번호는 1부터 m까지.

입력
소의 수 n, 축사 수 m 1이상 200이하
n개 줄에는 소가 들어가기 원하는 축사 정보 제시.
i번째 소가 들어가기 원하는 축사의 수 S가 제시되고 이후 S개의 축사 번호 제시. 중복 번호는 없음.

출력
축사에 들어갈 수 있는 소의 최댓값 출력
'''
import sys
input = sys.stdin.readline

def matching(idx):
    for i in g[idx]:
        if v[i]:
            continue
        v[i] = 1
        if not connect[i] or matching(connect[i]):
            connect[i] = idx
            return True
    return False

n, m = map(int, input().rstrip().split())
g = [[]]
for _ in range(n):
    s = list(map(int, input().rstrip().split()))
    s.pop(0)
    g.append(s)
connect = [0] * (m+1)
for i in range(1, n+1):
    v = [0] * (m+1)
    matching(i)

print(len(connect)-connect.count(0))





