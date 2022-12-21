

import sys
from collections import deque
input = sys.stdin.readline

dh = [0,1,1,0,-1,-1]
dw = [-1,-1,0,1,1,0]
nz = [0, 6, 18, 36, 60, 90, 126, 168, 216, 270, 330, 396, 468, 546, 630, 720, 816, 918, 1026, 
1140, 1260, 1386, 1518, 1656, 1800, 1950, 2106, 2268, 2436, 2610, 2790, 2976, 3168, 3366, 3570, 3780, 3996, 4218, 4446, 4680, 4920, 5166, 5418, 5676, 5940, 6210, 6486, 6768, 7056, 7350, 7650, 7956, 8268, 8586, 8910, 9240, 9576, 9918, 10266, 10620, 10980, 11346, 11718, 12096, 12480, 12870, 13266, 13668, 14076, 14490, 14910, 15336, 15768, 16206, 16650, 17100, 17556, 18018, 18486, 18960, 19440, 19926, 20418, 20916, 21420, 21930, 22446, 22968, 23496, 24030, 24570, 25116, 25668, 26226, 26790, 27360, 27936, 28518, 29106, 29700, 30300, 30906, 31518, 32136, 32760, 33390, 34026, 34668, 35316, 35970, 36630, 37296, 37968, 38646, 39330, 40020, 40716, 41418, 42126, 42840, 43560, 44286, 45018, 45756, 46500, 47250, 48006, 48768, 49536, 50310, 51090, 51876, 52668, 53466, 54270, 55080, 55896, 56718, 57546, 
58380, 59220, 60066, 60918, 61776, 62640, 63510, 64386, 65268, 66156, 67050, 67950, 68856, 69768, 70686, 71610, 72540, 73476, 74418, 75366, 76320, 77280, 78246, 79218, 80196, 81180, 82170, 83166, 84168, 85176, 86190, 87210, 88236, 89268, 90306, 91350, 92400, 93456, 94518, 95586, 96660, 97740, 98826, 99918, 101016, 102120, 103230, 104346, 105468, 106596, 
107730, 108870, 110016, 111168, 112326, 113490, 114660, 115836, 117018, 118206, 119400, 120600, 121806, 123018, 124236, 125460, 126690, 127926, 129168, 130416, 131670, 132930, 134196, 135468, 136746, 138030, 139320, 140616, 141918, 143226, 144540, 145860, 147186, 148518, 149856, 151200, 152550, 153906, 155268, 156636, 158010, 159390, 160776, 162168, 163566, 164970, 166380, 167796, 169218, 170646, 172080, 173520, 174966, 176418, 177876, 179340, 180810, 182286, 183768, 185256, 186750, 188250, 189756, 191268, 192786, 194310, 195840, 197376, 198918, 200466, 202020, 203580, 205146, 206718, 208296, 209880, 211470, 213066, 214668, 216276, 217890, 219510, 221136, 222768, 224406, 226050, 227700, 229356, 231018, 
232686, 234360, 236040, 237726, 239418, 241116, 242820, 244530, 246246, 247968, 249696, 251430, 253170, 254916, 256668, 258426, 260190, 261960, 263736, 265518, 267306, 269100, 270900, 272706, 274518, 276336, 278160, 279990, 281826, 283668, 285516, 287370, 289230, 291096, 292968, 294846, 296730, 298620, 300516, 302418, 304326, 306240, 308160, 310086, 312018, 313956, 315900, 317850, 319806, 321768, 323736, 325710, 327690, 329676, 331668, 333666, 335670, 337680, 339696, 341718, 343746, 345780, 347820, 349866, 351918, 353976, 356040, 358110, 360186, 362268, 364356, 366450, 368550, 370656, 372768, 374886, 377010, 379140, 381276, 383418, 385566, 387720, 389880, 392046, 394218, 396396, 398580, 400770, 402966, 
405168, 407376, 409590, 411810, 414036, 416268, 418506, 420750, 423000, 425256, 427518, 429786, 432060, 434340, 436626, 438918, 441216, 443520, 445830, 448146, 450468, 452796, 455130, 457470, 459816, 462168, 464526, 466890, 469260, 471636, 474018, 476406, 478800, 481200, 483606, 486018, 488436, 490860, 493290, 495726, 498168, 500616, 503070, 505530, 507996, 510468, 512946, 515430, 517920, 520416, 522918, 525426, 527940, 530460, 532986, 535518, 538056, 540600, 543150, 545706, 548268, 550836, 553410, 555990, 558576, 561168, 563766, 566370, 568980, 571596, 574218, 576846, 579480, 582120, 584766, 587418, 590076, 592740, 595410, 598086, 600768, 603456, 606150, 608850, 611556, 614268, 616986, 619710, 622440, 
625176, 627918, 630666, 633420, 636180, 638946, 641718, 644496, 647280, 650070, 652866, 655668, 658476, 661290, 664110, 666936, 669768, 672606, 675450, 678300, 681156, 684018, 686886, 689760, 692640, 695526, 698418, 701316, 704220, 707130, 710046, 712968, 715896, 718830, 721770, 724716, 727668, 730626, 733590, 736560, 739536, 742518, 745506, 748500, 751500, 754506, 757518, 760536, 763560, 766590, 769626, 772668, 775716, 778770, 781830, 784896, 787968, 791046, 794130, 797220, 800316, 803418, 806526, 809640, 812760, 815886, 819018, 822156, 825300, 828450, 831606, 834768, 837936, 841110, 844290, 847476, 850668, 853866, 857070, 860280, 863496, 866718, 869946, 873180, 876420, 879666, 882918, 886176, 889440, 
892710, 895986, 899268, 902556, 905850, 909150, 912456, 915768, 919086, 922410, 925740, 929076, 932418, 935766, 939120, 942480, 945846, 949218, 952596, 955980, 959370, 962766, 966168, 969576, 972990, 976410, 979836, 983268, 986706, 990150, 993600, 997056, 1000518, 1003986, 1007460]
def check(num):
    for i in range(580):
        if num > nz[i]+1:
            continue
        return i

def lego(num):
    if num <= 7:
        if num == 6:
            return 2
        if num == 7:
            return 3
        return num
    size = check(num)
    mtr = [1, 1, 0, 0, 0] # 0 1 2 3 4 로 재료 표기.
    size2 = 1+size*2
    g = [[-1]*(size2) for _ in range(size2)]
    g[size][size] = 0
    g[size-1][size+1] = 1
    q = deque([(size-1, size+1, 0)]) # h, w, di
    num-=2
    while q and num:
        h, w, di = q.popleft()
        num -= 1
        if di == 6:
            di = 0
        ndi = (di+1)%6
        nh, nw = h+dh[di], w+dw[di]
        nnh, nnw = h+dh[ndi], w+dw[ndi]
        if g[nnh][nnw] < 0:
            hbg = {0,1,2,3,4}
            for i in range(6):
                nnnh, nnnw = nnh+dh[i], nnw+dw[i]
                if 0<=nnnh<size2 and 0<=nnnw<size2 and g[nnnh][nnnw] in hbg:
                    hbg.remove(g[nnnh][nnnw])
            # 보드에 가장 적게 나타난 자원
            tg, val = -1, 10001
            hbg = sorted(list(hbg))
            for i in hbg:
                if mtr[i] < val:
                    tg = i
                    val = mtr[i]
            mtr[tg] += 1 # 카운트 증가
            # 큐 삽입
            g[nnh][nnw] = tg
            q.append((nnh, nnw, di+1))
        else:
            hbg = {0,1,2,3,4}
            for i in range(6):
                nnnh, nnnw = nh+dh[i], nw+dw[i]
                if 0<=nnnh<size2 and 0<=nnnw<size2 and g[nnnh][nnnw] in hbg:
                    hbg.remove(g[nnnh][nnnw])
            # 보드에 가장 적게 나타난 자원
            tg, val = -1, 10001
            hbg = sorted(list(hbg))
            for i in hbg:
                if mtr[i] < val:
                    tg = i
                    val = mtr[i]
            mtr[tg] += 1 # 카운트 증가
            # 큐 삽입
            g[nh][nw] = tg
            q.append((nh, nw, di))

    return tg+1


for _ in range(int(input())):
    n = int(input())
    print(lego(n))