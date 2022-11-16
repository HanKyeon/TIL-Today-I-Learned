'''
2*2*2 큐브

2*2*2 큐브. 각 면은 양방향 90도 돌릴 수 있다.
각 면에 있는 색상이 모두 같으면 큐브를 풀었다고 한다.
2*2*2 제시, 한 번 돌려서 큐브를 풀 수 있는지 아닌지?

입력
각 면 색상 제시. 1부터 6까지 자연수. 자연수는 각 총 4번 등장.

       1  2
       3  4
13 14  5  6 17 18 21 22
15 16  7  8 19 20 23 24
       9 10
      11 12

[13, 14, 5, 6, 17, 18, 21, 22]
[15, 16, 7, 8, 19, 20, 23, 24]
[1, 3, 5, 7, 9, 11, 22, 24]
[2, 4, 6, 8, 10, 12, 21, 23]
[3, 4, 17, 19, 10, 9, 16, 14]
[1, 2, 18, 20, 12, 11, 15, 13]

출력
한 번 돌려서 풀 수 있으면 1, 없으면 0 출력.
'''
import sys
input = sys.stdin.readline

def check():
    global di1, di2
    # print(di1, di2)
    li1, li2 = list(range(1,25)), list(range(1, 25))
    for i in range(24):
        if di1.get(li1[i], 0):
            li1[i] = di1[li1[i]]
        li1[i] = zsw[li1[i]]
        if di2.get(li2[i], 0):
            li2[i] = di2[li2[i]]
        li2[i] = zsw[li2[i]]
    # print(li1)
    # print(li2)
    # print('========')
    
    fla = True
    for i in range(0, 24, 4):
        if len(set(li1[i:i+4])) == 1:
            continue
        else:
            fla = False
    if fla:
        return fla

    for i in range(0, 24, 4):
        if len(set(li2[i:i+4])) == 1:
            continue
        else: fla = False
    # print(li1)
    # print(li2)
    return fla

def turn(flr):
    global di1, di2
    li1, li2 = flr[2:]+flr[:2], flr[6:]+flr[:6]
    di1, di2 = {}, {}
    for i in range(8):
        di1[flr[i]] = li1[i]
        di2[flr[i]] = li2[i]
    return check()

def lego(l1,l2,l3,l4, l5, l6):
    li1, li2, li3, li4, li5, li6 = l1[:], l2[:], l3[:],l4[:], l5[:], l6[:]
    a = turn(li1)
    if a: return 1
    a = turn(li2)
    if a: return 1
    a = turn(li3)
    if a: return 1
    a = turn(li4)
    if a: return 1
    a = turn(li5)
    if a: return 1
    a = turn(li6)
    if a: return 1
    return 0

nl = list(map(int, (input().rstrip().split())))
zsw = {}
di1, di2 = {}, {}
for i in range(1, 25):
    zsw[i] = nl[i-1]
line1 = [13, 14, 5, 6, 17, 18, 21, 22]
line2 = [15, 16, 7, 8, 19, 20, 23, 24]
line3 = [1, 3, 5, 7, 9, 11, 22, 24]
line4 = [2, 4, 6, 8, 10, 12, 21, 23]
line5 = [3, 4, 17, 19, 10, 9, 16, 14]
line6 = [1, 2, 18, 20, 12, 11, 15, 13]

print(lego(line1, line2, line3, line4, line5, line6))


'''
       1  1
       1  1
 2  2  2  2  4  4  5  5
 3  3  3  3  4  4  6  6
       6  6
       5  5
1 1 1 1 2 2 3 3 6 6 5 5 2 2 3 3 4 4 4 4 5 5 6 6
'''





