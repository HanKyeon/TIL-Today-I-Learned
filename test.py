


import heapq


res = []
for t in range(int(input())):
    N = int(input())
    arr = [[0 for i in range(N)] for i in range(N)]
    cnt = N
    num, row, col, sw = 0, 0, -1, 1

    while cnt > 0:

        for i in range(cnt):
            num += 1
            col += sw
            arr[row][col] = num

        cnt -= 1

        for i in range(cnt):
            num += 1
            row += sw
            arr[row][col] = num

        sw = -sw
    str_res = ""
    for i in range(N):
        for j in range(N):
            str_res += str(arr[i][j])+" "
        str_res += "\n" if i < N-1 else ""
    res.append(str_res)

for i in range(len(res)):
    print("#{}\n{}".format(i+1,res[i]))

# 테스트용 추가
# 테스트용 추가 2
# 테스트용 추가 3
# 테스트용 추가 4
# 테스트용 추가 5
# 테스트용 추가 6