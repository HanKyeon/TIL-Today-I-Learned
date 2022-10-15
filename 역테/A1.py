'''
나무의 키

N개의 나무. 나무 키 제시.
하루 한 나무 물.
홀수 날은 키가 1 자라고
짝수 날은 2 자란다.
모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 할 수 있는 최소 날짜 수.

물을 안줄 수도 있다.
나무 갯수는 2이상 100이하
초기 높이는 1이상 120이하

입력
테케T
나무 갯수 n
나무 높이 리스트

출력
#테케T 가능한 최소 날짜 수
'''

# 물주기 함수
def watering(tree_heights):
    biggest_tree = max(tree_heights) # 첫째날 가장 큰 나무
    if biggest_tree == min(tree_heights): # 가장 큰 나무가 가장 작은 나무와 같다면
        return 0 # 0일이 걸린다.
    # 자라야 할 부분으로 리스트 만들기.
    growing_hieghts = list(map(lambda x: biggest_tree-x, tree_heights))
    count_of_2, count_of_1 = 0, 0
    # 필요한 2의 갯수와 1의 갯수 세어주기
    for now_height in growing_hieghts:
        count_of_2 += now_height // 2
        count_of_1 += now_height % 2
    # 2의 갯수가 2개 이상 더 많을 때, 1의 갯수로 바꿔주기.
    while count_of_2 - count_of_1 >= 2:
        count_of_2 -= 1
        count_of_1 += 2
    # 반환
    if count_of_2 == count_of_1:
        return count_of_2 * 2
    if count_of_2 - count_of_1 == 1:
        return count_of_2 * 2
    if count_of_1 > count_of_2:
        return count_of_1 * 2 - 1

# 본체
for testcase in range(1, int(input())+1):
    _ = int(input()) # 나무의 갯수. 사용하지 않는 변수이기에, _에 할당.
    original_tree_heights = list(map(int, input().split())) # 원본 나무 높이 리스트.
    print(f"#{testcase} {watering(original_tree_heights)}") # 출력






# [2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,2,1,120,]

# 120
# 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 2 1 120 
'''
def water(li):
    global n
    d1M = max(li) # 첫째날 가장 큰 나무
    if d1M == min(li): # 가장 큰 나무가 가장 작은 나무와 같다면
        return 0 # 0일이 걸린다.

    # 자라야 할 부분으로 리스트 만들기.
    nli = list(map(lambda x: d1M-x, li))
    print(nli)
    zzak, hol = 0, 0
    for i in nli:
        zzak += i // 2
        hol += i % 2
    print(zzak, hol, "변환 전")
    while zzak - hol >= 2:
        if zzak > hol:
            zzak -= 1
            hol += 2
        else:
            break
    print(zzak, hol, "변환 후")
    if zzak == hol:
        return zzak * 2
    if zzak - hol == 1:
        return zzak*2
    if hol > zzak:
        return hol*2 - 1

for tc in range(1, int(input())+1):
    n = int(input())
    nl = list(map(int, input().split()))
    print(f"#{tc} {water(nl)}")
'''


'''
30
2
5 5
2
4 2
2
3 4
4
2 3 10 5
4
1 2 3 4
20
26 19 23 2 24 2 17 15 1 27 6 29 18 23 27 13 26 21 9 1
20
4 5 3 4 2 4 4 3 5 2 2 3 5 5 5 2 5 2 5 5
20
1 3 6 5 5 1 5 4 3 5 4 2 4 6 5 5 4 5 5 3
20
4 5 6 6 5 3 1 3 3 3 3 5 3 3 3 4 5 1 4 3
20
26 6 8 15 10 15 14 6 19 16 5 13 9 12 14 29 28 3 12 27
30
8 27 2 32 19 16 19 11 33 35 7 9 6 12 7 1 1 28 38 32 25 14 5 15 34 30 14 24 7 24
30
3 2 5 5 5 4 4 5 2 4 3 4 3 5 5 2 5 4 2 5 2 1 5 4 4 3 2 4 2 4
30
6 4 6 5 6 1 1 6 4 5 6 6 5 1 3 6 5 5 5 4 6 1 1 5 3 3 6 1 5 5
30
1 6 3 5 6 1 4 5 4 5 5 5 6 5 2 3 6 2 3 5 5 1 5 4 6 5 6 4 6 6
30
35 8 19 40 12 17 11 29 14 21 31 39 28 33 16 19 34 12 12 10 28 40 6 19 36 19 10 2 34 22
50
37 59 11 13 18 30 22 53 35 18 27 7 50 19 57 38 54 24 31 38 4 8 9 54 37 29 32 27 11 7 19 57 36 54 35 31 45 2 10 54 27 14 51 27 34 51 1 58 4 6
50
2 2 5 2 3 2 3 1 3 5 5 3 2 2 2 3 4 4 4 2 1 5 4 4 4 2 3 4 2 5 4 3 5 3 5 2 2 4 4 4 5 5 3 4 2 3 4 4 5 4
50
6 6 5 4 6 6 1 4 2 1 4 6 2 3 5 6 5 5 1 5 5 4 5 3 1 6 3 6 5 3 5 1 3 5 3 6 3 5 5 2 4 3 6 3 5 5 3 5 5 6
50
5 5 5 1 4 5 3 2 4 5 5 5 6 3 2 5 5 6 3 5 3 5 4 6 5 5 3 3 6 5 6 1 3 4 4 6 1 6 3 3 6 3 2 6 6 1 5 4 5 4
50
11 17 35 37 41 2 8 20 40 5 25 58 54 7 36 33 46 44 37 53 15 8 42 56 35 2 40 55 50 58 49 2 35 19 32 54 18 12 22 56 23 17 47 4 30 56 48 4 36 33
70
37 26 72 57 38 33 9 6 66 71 59 55 21 58 65 57 27 36 14 27 7 76 34 34 8 55 23 80 41 35 39 38 8 5 17 23 42 1 27 78 77 26 74 51 13 27 32 11 75 37 37 62 75 73 41 28 29 57 56 18 79 27 48 9 1 30 31 65 73 63
70
3 4 4 3 4 5 4 1 5 4 4 5 5 5 4 4 2 3 3 4 4 2 3 2 5 1 2 5 4 4 4 5 2 2 4 2 3 2 3 5 4 5 4 4 1 2 3 4 4 4 5 3 5 5 4 5 4 3 5 5 2 4 1 4 2 4 5 3 5 3
70
6 5 1 3 3 5 5 5 3 5 3 4 2 6 5 5 1 2 1 3 5 4 6 1 1 5 5 5 5 5 6 6 5 1 1 5 3 5 4 5 3 5 2 4 3 1 2 5 6 3 6 3 4 4 5 3 5 5 3 3 6 5 2 1 3 5 6 5 4 5
70
5 5 4 6 6 3 4 1 1 1 3 6 6 1 5 5 1 5 3 5 6 3 5 3 4 6 1 5 2 6 3 5 6 5 3 5 1 3 4 4 6 5 2 1 6 5 4 5 5 4 5 6 3 5 2 4 3 3 3 3 3 6 3 5 5 3 5 4 5 5
70
47 25 56 22 41 75 1 47 39 28 48 52 43 50 56 2 50 41 35 6 36 23 60 67 73 3 30 52 31 8 60 34 10 55 35 24 28 75 45 5 37 49 24 1 59 7 6 20 77 4 5 67 5 25 18 61 29 54 41 69 68 16 33 48 65 18 22 34 70 2
100
30 108 8 61 17 56 54 29 50 72 9 97 67 36 75 110 88 99 75 93 19 44 39 45 72 53 115 106 1 20 25 118 117 51 89 72 116 33 76 26 6 47 35 55 45 89 78 69 56 78 58 95 34 9 1 14 2 9 8 64 12 85 117 49 40 44 8 2 89 36 12 56 89 18 38 63 3 57 29 110 25 46 98 20 119 52 114 107 23 11 105 35 119 55 82 115 56 85 68 28
100
2 4 4 3 1 3 4 5 5 2 3 2 4 4 4 4 4 2 4 1 5 3 5 3 2 3 4 4 2 2 3 5 2 4 2 4 3 4 4 2 4 5 4 5 4 4 4 5 5 3 3 4 4 1 2 1 5 2 4 4 4 1 2 4 1 2 1 4 5 2 4 5 5 2 4 5 1 4 3 5 4 5 2 3 2 5 4 4 5 3 2 4 4 2 2 5 5 1 2 2
100
4 5 2 6 6 1 5 2 1 1 3 5 3 3 5 6 5 6 3 5 5 5 1 1 6 3 5 5 6 5 4 4 6 6 1 5 1 5 1 4 5 5 2 5 5 5 5 3 6 3 2 5 5 6 6 3 5 3 1 2 5 1 4 6 4 6 1 3 4 3 6 1 1 5 2 3 1 5 3 5 6 5 5 5 5 3 5 6 2 6 5 4 3 5 5 3 5 6 5 6
100
3 6 5 1 6 5 6 1 6 5 5 6 6 5 5 6 3 5 3 5 6 6 3 5 5 6 3 3 3 2 4 6 4 4 5 4 5 6 6 5 1 5 2 3 3 3 5 3 6 5 4 3 6 5 6 6 5 5 5 2 3 5 1 6 1 6 3 3 6 5 2 6 3 2 3 3 5 1 6 5 5 6 1 3 4 3 3 5 2 1 1 6 1 5 6 4 6 5 4 5
100
68 88 9 43 34 56 114 65 16 83 42 2 120 94 45 100 44 110 47 34 16 112 24 108 22 78 88 120 65 69 108 81 36 53 82 15 67 56 82 95 74 95 14 77 29 97 68 103 32 109 88 115 80 107 15 116 81 78 82 17 98 100 47 103 30 41 55 72 100 24 11 19 105 12 64 102 100 22 21 106 50 8 66 14 20 58 43 14 78 82 21 5 1 81 89 65 35 20 87 47

'''
'''
    global n
    d1M = max(li)
    if d1M == min(li):
        return 0
    vst = {(tuple(li), 2)}
    q = deque()
    q.append((li, 0, 2))
    while True:
        li, cnt, eo = q.popleft()
        nli = li[:]
        mval = min(nli)
        if mval == d1M:
            print(vst)
            return cnt
        if eo == 1:
            eo = 2
        else:
            eo = 1
        if (tuple(nli), eo) not in vst:
            q.append((nli, cnt+1, eo))
            vst.add((tuple(nli), eo))
        nnli = nli[:]
        for i in range(n):
            if d1M > eo + nnli[i]:
                nnli[i] += eo
                if (tuple(nnli), eo) not in vst:
                    q.append((nnli, cnt+1, eo))
                    vst.add((tuple(nnli), eo))
                nnli[i] -= 1
'''




