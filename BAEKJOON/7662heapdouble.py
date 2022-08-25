'''
이중 우선순위 큐

이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는 데이터를 삭제하는 연산이다. 데이터를 삭제하는 연산은 또 두 가지로 구분되는데 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다. 
정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자. 

Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.

입력
테케T
연산 갯수 100만 이하 k
k줄ㄹ에 걸쳐
D 1최댓값 삭제
D -1 최솟값 삭제
I n n 삽입
큐가 비었는데 D연산일 경우 무시

출력
모든 연산을 처리 한 후 Q에 남아있는 값의 최대 최소 출력 한줄에, 공백구분o
Q가 비었다면 EMPTY
'''
import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

'''
최대힙과 최소힙 두가지를 사용하는데, 그 둘을 연계해주기 위해 visited를 사용해준다.
최대값을 뺐는데 이미 최소힙 빼기 작업을 하며 visited가 꺼져있다면 하나 더 빼서 visited를 확인하는 방식.
'''

def inum(num, idx): # I일 때 연산. heap에 더해준다.
    global Mh, mh, v
    v[i] = 1
    heappush(Mh, (-num, idx))
    heappush(mh, (num, idx))

def dp1(): # 빼는 연산. Mh가 없다면 끝내고, 있는데 이미 방문 끝난 상태라면 heappop() 해준다.
    global Mh, v
    while Mh and v[Mh[0][1]] == 0:
        heappop(Mh)
    if not Mh:return
    a = heappop(Mh)
    v[a[1]] = 0

def dm1(): # 빼기연산2. mh가 없다면 끝내고 있는데 이미 방문 끝난 상태라면 heappop() 해준다.
    global mh, v
    while mh and v[mh[0][1]] == 0:
        heappop(mh)
    if not mh:return
    a = heappop(mh)
    v[a[1]] = 0

for testcase in range(int(input())): # 테케
    k = int(input().rstrip()) # 연산 횟수
    Mh, mh,  v = [], [], [0]*(k+1) # 최대힙 최소힙 방문처리
    for i in range(k): # 연산 입력 받기
        y, num = input().rstrip().split()
        if y == 'I': # I라면
            inum(int(num), i) # I 기능 실행
        elif num == '-1': # 나머지는 D가 확실하니 -1이라면
            dm1() # 최소힙 빼기 실행
        elif num == '1': # 1이라면
            dp1() # 최대힙 빼기 실행.
    if sum(v) == 0: # 방문된 상태인것, 안빠진게 없다면
        print("EMPTY") # 비었다고 표시하고
        continue # 다음 테케로
    Ma, mi = -int(10e9), int(10e9) # 최댓값 최솟값 비교를 위해 +-10억 설정.
    while Mh: # 작업 하나로 해도 될듯. 최댓값
        a = heappop(Mh)
        if v[a[1]] == 1:
            Ma = max(Ma, -a[0])
    while mh: # 최솟값
        b = heappop(mh)
        if v[b[1]] == 1:
            mi = min(mi, b[0])
    print(Ma, mi) # 출력

'''
5000ms 정답

import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

def main():
    t = int(input().rstrip())
    for _ in range(t):
        k = int(input().rstrip())
        max_heap = []
        min_heap = []
        item_dict = {}
        item_cnt = 0
        for i in range(k):
            cmd, val = input().rstrip().split()
            val = int(val)
            if cmd == "I":
                item_cnt += 1
                heapq.heappush(max_heap,-val)
                heapq.heappush(min_heap,val)
                if val in item_dict:
                    item_dict[val] += 1
                else:
                    item_dict[val] = 1
            else:
                if item_cnt > 0:
                    item_cnt -= 1
                if val == 1:
                    if len(max_heap) > 0:
                        while max_heap:
                            max_pop = -heapq.heappop(max_heap)
                            if item_dict[max_pop] > 0:
                                item_dict[max_pop] -= 1
                                break
                            else:
                                continue
                else:
                    if len(min_heap) > 0:
                        while min_heap:
                            min_pop = heapq.heappop(min_heap)
                            if item_dict[min_pop] > 0:
                                item_dict[min_pop] -= 1
                                break
                            else:
                                continue
        if item_cnt == 0:
            print("EMPTY\n")
        else:
            max_val = 0
            min_val = 0
            while max_heap:
                max_pop = -heapq.heappop(max_heap)
                if item_dict[max_pop] > 0:
                    max_val = max_pop
                    break
            while min_heap:
                min_pop = heapq.heappop(min_heap)
                if item_dict[min_pop] > 0:
                    min_val = min_pop
                    break
            print(str(max_val) + " " + str(min_val) + "\n")

if __name__ == "__main__":
    main()

'''






