# 쵣 ㅐ힙

# 부모 노드는 n//2 자식 노드는 n//2, n//2+1

from heapq import heappush


def enq(n):
    global last
    last += 1
    heap[last] = n
    # 부모가 있고, 부모<자식 인 경우 자리 교환
    c = last
    p = c//2 # 완전 이진트리라 부모 노드 번호.
    while p and heap[p] < heap[c]: # 최상위 루트 노드인 0이 아니고, 부모<자식인 경우 자리 교환.
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1

    p = 1
    # c1, c2 = p*2, p*2+1
    c = p*2
    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]:
            c+=1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
        else:
            break
        p = c
        c = p*2
    return tmp

heap = [0] * 100
last = 0
a = [2,5,7,3,4,6]
for i in a:
    enq(i)
print(heap[:len(a)+1])
while last:
    print(deq(), end=' ')
print()



from heapq import heappush, heappop
nheap = []
a = [2,5,7,3,4,6]
for i in a:
    heappush(nheap, -i)
print(nheap)
while nheap:
    print(heappop(nheap), end=' ')
print()



























