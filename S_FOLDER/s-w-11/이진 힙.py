'''
이진 최소힙.

완전 이진트리 유지를 위해 마지막 노드 뒤에 새 노드를 추가.
부모 < 자식 유지.
완전 이진트리.
1000000 이하인 N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램 작성.

입력
테케T
n
자연수 n개

출력
#테케 막노드의 조상 노드에 저장된 정수의 합 출력
'''
from heapq import heapify, heappush


def enq(x):
    heap.append(x)
    c = len(heap)-1
    p = c//2
    while p and heap[c] < heap[p]:
        heap[c], heap[p] = heap[p], heap[c]
        c = p
        p = c//2


for testcase in range(1, int(input())+1):
    n = int(input())
    nl = list(map(int, input().rstrip().split()))
    heap = [0]
    while nl:
        a = nl.pop(0)
        enq(a)
    i = n//2
    ans = 0

    while i>0:
        ans += heap[i]
        i //= 2
    print(f"#{testcase} {ans}")

for testcase in range(1, int(input())+1):
    n = int(input())
    nl = list(map(int, input().rstrip().split()))
    heap = []
    while nl:
        a = nl.pop(0)
        heappush(heap, a)
    heap = [0]+heap
    i = n//2
    ans = 0
    while i>0:
        ans += heap[i]
        i //= 2
    print(f"#{testcase} {ans}")


