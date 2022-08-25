'''
집합

비어있는 공집합 S가 주어졌을 때 아래 연산을 수행하는 프로그램 작성.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

입력
수행해야하는 연산의 수 1이상 300만이하
M개 주렝 연산 한 줄에 ㅎ나씩

출력 check 연산이 주어질 때마다 결과 출력
'''
import sys
input = sys.stdin.readline

def ad(x):
    global sets
    sets.add(x)
def re(x):
    global sets
    if not x in sets: return
    sets.remove(x)
def ch(x):
    global sets
    if x in sets:
        print(1)
    else:
        print(0)
def to(x):
    global sets
    if x in sets:
        sets.remove(x)
    else:
        sets.add(x)
def al():
    global sets
    sets = set({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
def em():
    global sets
    sets = set()

n = int(input().rstrip())
sets = set()

for i in range(n):
    s = input().rstrip()
    if s == 'all':al()
    elif s == 'empty':em()
    else:
        ys, x = s.split()
        if ys == 'add':ad(int(x))
        if ys == 'remove':re(int(x))
        if ys == 'check':ch(int(x))
        if ys == 'toggle':to(int(x))

