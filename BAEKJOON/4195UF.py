'''
친구 네트워크

민혁이는 sns 친구 만들기를 좋아한다.
친구 관계가 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
친구 네트워크란, 친구 관계만으로 이동 할 수 있는 사이를 말한다.

입력
테케T
친구 관계 수 F, 10만이하.
친구 관계 제시. 알파벳으로 이루어진 20이하 문자열.

출력
친구 관계가 생길 때 마다 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램 작성.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x): # 파인드
    if parents[x] != x: # 부모가 다르다면 (들어온 idx)
        parents[x] = find(parents[x]) # 그 값으로 찾으러 가라 # idx가 배열or 딕트에서 가르키는 값
    return parents[x] # 최상위 부모값이 반환되서 대입되므로 그 값 반환

def union(a, b): # 유니온
    a = find(a) # 부모 찾기
    b = find(b) # 부모 찾기
    if a != b: # 두 부모가 다르다면
        parents[b] = a # 한쪽의 부모를 a로 주고
        count[a] += count[b] # 그 값을 더해준다. 원래라면 크기에 따라서 부모만 설정하고 끝내는듯하다.

for _ in range(int(input())):
    n = int(input()) # 친구 수
    parents = {} # 부모
    count = {} # 사람
    for i in range(n):
        a, b = input().rstrip().split()
        if a not in parents: # 없는 값이면
            parents[a] = a # 만들어준
            count[a] = 1 # 다
        if b not in parents: # 없으면
            parents[b] = b # 만든
            count[b] = 1 # 다
        union(a, b) # 두 친구는 친구이므로 부모를 통일시킨다.
        print(count[find(a)]) # 값 출력해준다. 유니온에서 부모를 a로 갱신하기에 find(a)로 해야한다.

'''
# 시간 초과

import sys
input = sys.stdin.readline

def find_parent(x):
    if di[x] != x:
        return find_parent(di[x])
    return x

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        di[b] = a
    else:
        di[a] = b

for _ in range(int(input())):
    n = int(input()) # 친구 수
    di = {}
    i = 0
    for _ in range(n):
        f1, f2 = input().rstrip().split()
        if di.get(f1, 0):
            di[f2] = find_parent(di[f1])
        elif di.get(f2, 0):
            di[f1] = find_parent(di[f2])
        else:
            di[f1] = f1
            di[f2] = f1 
        root = find_parent(f1)
        root2 = find_parent(f2)
        ret = 2
        for i in di:
            if i == f1 or i == f2:
                continue
            c = find_parent(i)
            if c == root or c == root2:
                ret+=1
        print(ret)
'''

'''
1
8
a b
b c
d e
e f
g h
h i
a f
c i
'''






