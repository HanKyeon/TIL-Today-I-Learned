def lego():
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    bf = h1*60*60 + m1*60 + s1
    af = h2*60*60 + m2*60 + s2
    t = af - bf
    print(t//60//60 % 24, t//60 % 60, t%60)
lego()
lego()
lego()
# a, b = map(int, input().split())
# c, d = map(int, input().split())
# print(min(a+d, b+c))

# import sys
# input = sys.stdin.readline

di = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
while True:
    s = input().rstrip()
    if s == '#':
        break
    ans = 0
    for i in s:
        if i in di:
            ans += 1
    print(ans)

# for _ in range(int(input())):
#     k, n = int(input()), int(input())
#     dp = [[i for i in range(n+1)]] + [[0]*(n+1) for _ in range(k)]
#     for i in range(1, k+1):
#         for j in range(1, n+1):
#             dp[i][j] = dp[i-1][j]+dp[i][j-1]
#     print(dp[-1][-1])


# while True:
#     try:
#         print(f"{input()}")
#     except:
#         break

# while True:
#     a, b, c = sorted(map(int, input().rstrip().split()))
#     if not a and not b and not c:
#         break
#     print("right" if c**2 == a**2+b**2 else "wrong")


# x, y, w, h = map(int, input().rstrip().split())
# print(min(abs(x-w), abs(y-h), x, y))

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     nl = list(map(int, input().rstrip().split()))
#     n = nl.pop(0)
#     a = sum(nl[1:])/n
#     ans = len([i for i in nl if i > a])
#     print(f'{ans/n*100:.3f}%')

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     nl = list(map(int, input().rstrip().split()))
#     a = sum(nl[1:])/nl[0]
#     ans = 0
#     for score in nl[1:]:
#         if score > a:
#             ans+=1
#     print(f'{ans/nl[0]*100:.3f}%')

# import sys
# input = sys.stdin.readline
# n, m = map(int, input().rstrip().split())
# k = int(input())
# a = n*60+m+k
# print(a//60 if a<24 else (a//60)%24, a%60)

# import sys
# from collections import deque
# input = sys.stdin.readline
# n, m = map(int, input().rstrip().split())
# nl = list(map(int, input().rstrip().split()))
# dupQ = deque()
# q = deque()
# v = [0]*(n+1)
# ans = ["Y" for _ in range(n)]
# ansIdx = 0
# # 개숫만큼 넣기
# while len(q) < n:
#     num = nl.pop(0)
#     v[num] += 1
#     if v[num] > 1:
#         if ans[0] == "Y":
#             ans[0] = "N"
#         dupQ.append(num)
#     q.append(num)
# # 우선 중복처리
# while dupQ and nl:
#     ansIdx = 0 if ansIdx+1 == n else ansIdx+1
#     oldNum = q.popleft()
#     v[oldNum] -= 1
#     if oldNum == dupQ[0]:
#         dupQ.popleft()
#     newNum = nl.pop(0)
#     v[newNum] += 1
#     q.append(newNum)
#     if v[newNum] > 1:
#         dupQ.append(newNum)
#         while dupQ and v[dupQ[0]] == 1:
#             dupQ.popleft()
#     if dupQ:
#         ans[ansIdx] = "N"
#     print(ans, dupQ, q)
# # 남은거 처리
# while nl:
#     ansIdx = 0 if ansIdx == n-1 else ansIdx+1
#     oldNum = q.popleft()
#     v[oldNum] -= 1
#     newNum = nl.pop(0)
#     q.append(newNum)
#     v[newNum] += 1
#     if v[newNum] > 1:
#         dupQ.append(newNum)
#         ans[ansIdx] = "N"
#     while dupQ and nl:
#         ansIdx = 0 if ansIdx+1 == n else ansIdx+1
#         oldNum = q.popleft()
#         v[oldNum] -= 1
#         if oldNum == dupQ[0]:
#             dupQ.popleft()
#         newNum = nl.pop(0)
#         v[newNum] += 1
#         q.append(newNum)
#         if v[newNum] > 1:
#             dupQ.append(newNum)
#             while dupQ and v[dupQ[0]] == 1:
#                 dupQ.popleft()
#         if dupQ:
#             ans[ansIdx] = "N"
# a = ans.pop(0)
# ans += [a]
# print("".join(ans))
# '''
# 6 12
# 1 2 3 4 5 6 6 5 4 3 2 1
# '''
# n,m = map(int, input().split())
# print("Yes" if n*100 >= m else "No")

# print(int(input())%20000303)

# a,b,c,d=input().split()
# print(int(a+b)+int(c+d))

# a, b, c = int(input()), int(input()), int(input())
# if a+b+c != 180:
#     print("Error")
# elif a==b==c:
#     print("Equilateral")
# elif a!=b and b!=c and a!=c:
#     print("Scalene")
# else:
#     print("Isosceles")


# for i in range(1, 8):
#     print(bin(1<<i))

# print(input()[int(input())-1])

# while True:
#     a = input().rstrip()
#     if a == "END": break
#     print(a[::-1])


# n=int(input())
# print(int(n*0.78), int(n*0.956))

# n,m,k = map(int, input().split())
# print(k//m, k%m)

# n=int(input())
# print(n//5+1 if n%5 else n//5)

# n,m=map(int,input().split())
# print(1 if n*(100-m)/100 < 100 else 0)
# for i in range(int(input())):print("yes" if 6<=len(input())<10 else "no") 




# print("                                                           :8DDDDDDDDDDDDDD$.                                           ")
# print("                                                      DDDNNN8~~~~~~~~~~=~7DNNDNDDDNNI                                   ")
# print("                                                  ?NNDD=~=~~~~~~~~~~~~~~~~~=~~==~=INNDNN7                               ")
# print("                                               +NDDI~~~~~~~~~~~~~~~~~~~~~~~=~~========~ODND+                            ")
# print("                                            :NND~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~============7NDN                          ")
# print("                                          $DD$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~==============~DNN                        ")
# print("                                        $DD=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~=================NND                      ")
# print("                                       ND7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~===================DD7                    ")
# print("                                     ~DD=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=======================8DN.                  ")
# print("                                    8DO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=========================DD                  ")
# print("                                   8N~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=~~=======================DN                 ")
# print("                                  NN::::::::~~~~~~~~~~~=~~~~~~~~~~~~~~~~~~~=~~========================DDO               ")
# print("                                 $D$:::::::::::::::~~~~DD~~~~~~~~~~~~~~~~~~=~~=========================DN.              ")
# print("                                 D8:::::::::::::::::::DN=::~~~~~~~~~~~~~~~~=~~======================~~:~DN              ")
# print("                                DN:::::::::::::::::::ONO::::::::::::::::::::~~~~~~~~~~~~:::::::::::::::::DN             ")
# print("                               DN::::::::::::::::::::NN.:::::::::::::::::::::::::::DN::::::::::::::::::::$DO            ")
# print("                               DD:::::::::::::::::::DNI:::::::::::::::::::::::::::::D=::::::::::::::::::::NN            ")
# print("                              NN~~~~:::::$N?:::::::.NN::::::::::::::::::::::::::::::ND.:::::::::::::::::::+N8           ")
# print("                              N7~~~~~~~~OD7::::::::~DD::::::::::::::::::::::::::::::~D$::::::::::::::::::::DN           ")
# print("                             NN~~~~~~~~IDZ~~~~~::::DN~:::::::::::::::::::::::::::::::DN::::::::::::::::::::=N~          ")
# print("                             DD~~~~~~~~NN~~~~~~~~~=NN::::::::::::::::::::::::::::::::DN:::::::::::::::~~====NN          ")
# print("                            8D~~~~~~~~ND~~~~~~~~~~~ND~~~~~~~~:::::::::::::::::::::::::N7:::~~===============NN          ")
# print("                            DD~~~~~~~ON+~~~~~~~~~~~ND~~~~~~~~~~~~~~~~~~~=+NZ==========NN====================~ND         ")
# print("               :DD7   DNDD. N8~~~~~~~NN~~~~~~~~~~DDND~~~~~~~~~~~~~~~~~~~~ND~~=========DD=====================ND         ")
# print("               N~:DDNNN .8NDN~~~~~~~$D=~~~~~~~~+ND.DD~~~~~~~~~~~~~~~~~~~=DD~~=========~D+====================DN         ")
# print("              :D     .  ..~ND~~~~~~~NN~~~~~~~+NN$..ND~~~~~~~~~~~~~~~~~~~7N=~~=========~ND=======~============ON         ")
# print("              NN       ...:N?~~~~~~~N=~~~~~NNNI.. .7D+~~~~~~~~~~~~~~~~~=8NN~~==========NN=======N============$N         ")
# print("         N  ODN       ....DN~~~~~~~DD=8NNND$..     .DD~~~=~~~~~~~~~~~~~=NNDD=~=========8D~======NN===========~N$        ")
# print("    N? =NN  ND      .....NND~~~~~~~DDNN:...        .ND=~DNN~~~~~~~~~~~~=DN.DN~=========?N+======NN============ND        ")
# print("   $D? DN    DZ    ....ND8NN~~~~~~$D                .DD~NNDD~~~~~~~~~~~~D8..DN=========~DN======NN============DN        ")
# print("   DN ~N~   NN    ..:~NN..NZ~~~~~~DN                  NNN8.ND~~~~NDN?~~~DZ...7DD=======~NN======NN============DN        ")
# print("   ND DD    :DN.  ..ND$  .N?~~~~~=NNN                   . ..DDD$~N8OND8=N+   ..DDDZ~====NN======+D+===========ND        ")
# print("   NO         DD  ZDN    8NO~~~~~~NNN..DDDNN7               ...NND...:DDD:     .:.NDND=~DD======~DO===========DN        ")
# print("              DNDDN:.    DN~~~~~~=NNNN.ODNNNNDDNNO              ...     .         ...DNNNN=======ND===========DD        ")
# print("       INDN7    DD.     .DD~~~~~=IDND:.:~.....?DNDNN.                        ...... ....$D=======ND===========ND        ")
# print("       NN        ND.    8N=~~~~$ND::.:=~:.~=......=ND~                 .NNNNNNNNNNNNNNN.~N+======NN===========DN        ")
# print("       $DD        DN:   DD~~~~7NO...~==.:~~:.....                      NNNND? ..::..7NZ.:N?======8D~==========ZN        ")
# print("       DN?     ~D: DND.?D~~~~~DD....~:.~=~.......                            ....~=:.:~..ND======~N$==========~DO       ")
# print("       ND    ..DD.  .DNDN=~~~~DI.......:.........                           ....=~..~~~..DN======~DD===========NN       ")
# print("       DDD  :.:DD.  . DDI~~~~~ND................        .DNNNNNNNNNN7      ....=~:.:~~...NN=======ND===========?D~      ")
# print("       8D. ...OD..    DD~~~~~~+ND ............          NN:~::::~~~8N      ........~~...:ND=======DN============NN      ")
# print("       DDI:...ND     .D7~~~~~~~7NN ..........           ID8::::::::8D      .............:DN=======ON============NN      ")
# print("        ~NNND.N=.   .NN~~~~~~~~~NDN8                       ~::::::~N8       .............DN========D=============NI     ")
# print("               DDNNN.ND~~~~~~~~DD =DND                                       ............DN========N+~===========NN     ")
# print("                   ~:N=~~~~~~~~DD   .DDDD                                       ........ NN========DD============8D     ")
# print("                    8N~~~~~~~~~ND    . .7NDDD? .                                      .8DDN========NN=============D:    ")
# print("                    DD~~~~~~~~~DND:         IDNNND$.                           .+DNNNNDNIDN========DD=============DD    ")
# print("                    ND~~~~~~~~ZN 7DD .. .:DDNDDNNDNNNNDDNDND8$?===+$8DDNNNDDDDDN8I~DN====8N========NN=============NN    ")
# print("                    DD~~~~~~~~8N   DD.  .NN~~~~.~~=DNDNO.:7ODDDDNNDD8DDDND=~~~ =~~~ON====8N========DN=============DN    ")
# print("                    ND~~~~~~~~DN    ZDD  DN~~~ ~~~~~=.7DDD+.......8NNN==~~~~~ ~~~~~ONN$==DN========8N=============ON    ")
# print("                    ND~8N~=~~~ZN      DDODN=~.~~~~~=.~~~~INDNNNNDNN~~~~~~~~:~~~~~~~DN~ND=DN========DD=========~ND=8N    ")
# print("                    IN=NDDI~~~~D8       DNN::~~~~~.~~~~~=.~~ND~~ND~~~~~~~~.~~~~~~~~NN  NDNN====ND==ND~D?======DNN=ND    ")
# print("                     DNNI8ND=~~DN:       ZN=~~~~~ ~~~~~.~~~~DD~=DD~~~~~~~ ~~~~~~~=.ND. . ND===DNDD=NDDNN=====8NZDDDN    ")
# print("                      NND  IDNDNNN+       D+~~~:~~~~~~ ~~~~~DDNNN+~~~~~~~~~~~~~~:=?N7   .ND=~ND  DNNN~ID====ND7 NNN     ")
# print("                       ID                 ND~~ ~~~~~:.~~~7DDN7IDNN==~~ ~~~~~~~~ ~~DN   .:N?DDDDD NND  8N~=DDD  ZNN      ")
# print("                                          NN~:~~~~~ =7DDDD+8N  :N8DDZ.~~~~~~~~.~~~DD.   NDD+ . DN=     OND+             ")
# print("                                          DND~~~=8DNDDZ=~~ ND   NN~INND~~~~~.~~~~ND .    .    ..IDD                     ")
# print("                                         DDNNNDNNN+~~~~~~.7N.    ND~~~NDDI~ ~~~~=NNN             .DDI                   ")
# print("                                        DN=~~~~.=~~~~~~ ~~DN     +N+~~~~+DNDD~~~NNNND.            ..ND                  ")
# print("                                         DDI~~ ~~~~~~~ ~~~ND..  ..ND~~~~:~~~DNDNNNN+            ..7O8ND+                ")
# print("                                          .DND=~~~~=::~~=NN.   . . 8D~~.~~~~~~=DN$ODNDNDNNNDNNNNND8+~..                 ")
# print("                                             8DNNI=.~~~~=NDDNNNNDDNDNN.~~~~~IDDNDND7:.                                  ")
# print("                                                ?DNNDD?~DD          ~NN~~=NDD$                                          ")
# print("                                                     :DDD.            NNNN=                                             ")


# n=sum([int(input()) for _ in range(4)])
# print(f"{n//60}\n{n%60}")

# n,m=map(int,input().split())
# nl=list(map(lambda x:int(x)-n*m,input().split()))
# print(*nl)

# if int(input()):
#     print("Leading the Way to the Future")
# else:
#     print("YONSEI")

# n, m = map(int, input().split())
# nl = list(range(n+1))
# for _ in range(m):
#     a, b = map(int, input().split())
#     nl[a], nl[b] = nl[b], nl[a]
# nl.pop(0)
# print(*nl)
# import sys
# input = sys.stdin.readline
# n = int(input())
# nl = list(map(int, input().rstrip().split()))
# print(sum(nl)/max(nl)*100/n)

# a,b,c = map(int, input().split())
# if a==b==c:print(10000+a*1000)
# elif a==b or c==a:print(1000+100*a)
# elif b==c:print(1000+100*b)
# else:print(max(a,b,c)*100)


# a,b,c=map(int,input().split())
# a=a*b-c
# print(a if a>0 else 0)

# print("SHIP NAME      CLASS          DEPLOYMENT IN SERVICE")
# print("N2 Bomber      Heavy Fighter  Limited    21        ")
# print("J-Type 327     Light Combat   Unlimited  1         ")
# print("NX Cruiser     Medium Fighter Limited    18        ")
# print("N1 Starfighter Medium Fighter Unlimited  25        ")
# print("Royal Cruiser  Light Combat   Limited    4         ")


# n, m = int(input()), int(input())
# if n==2 and m==18:print("Special")
# elif n > 2 or (n==2 and m>18): print("After")
# else : print("Before")

# print("     /~\\")
# print("    ( oo|")
# print("    _\\=/_")
# print("   /  _  \\")
# print("  //|/.\\|\\\\")
# print(" ||  \\ /  ||")
# print("============")
# print("|          |")
# print("|          |")
# print("|          |")


# n, m = map(int, input().rstrip().split())
# if m or not 12<=n<=16:
#     print(280)
# else:
#     print(320)

# import sys
# input = sys.stdin.readline
# # print = sys.stdout.writelines
# for _ in range(int(input())):
#     a, b = map(int, input().rstrip().split())
#     ans = a+b
#     print(ans)
    # print("\n")

# n, m = map(int, input().split())
# print(n//m)
# print(n%m)



# print(".  .   .")
# print("|  | _ | _. _ ._ _  _")
# print("|/\|(/.|(_.(_)[ | )(/.")

# T = int(input())
# for test_case in range(1, T + 1):
#     b = map(int, input().split())
#     a = round(sum(b)/10)
#     print(f'#{test_case} {a}')
#     print(type(a))

# for tc in range(1, int(input())+1):
#     print(f"#{tc} {round(sum(list(map(int, input().split())))/10)}")

# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")

# a = [1,1,2,2,2,8]
# nl = list(map(int, input().split()))
# a = list(map(lambda x: a[x]-nl[x], range(6)))
# print(*a)

# while True:
#     try:
#         print(input())
#     except:
#         break

# nl = list(map(lambda x: int(x)**2, input().split()))
# print(sum(nl)%10)

# from math import factorial
# print(factorial(int(input())))

# n, x = map(int, input().split())
# nl = list(map(int, input().split()))
# nnl = [i for i in nl if i < x]
# print(*nnl)

# for tc in range(1, int(input())+1):
#     a, b = map(int, input().split())
#     print(f"Case #{tc}: {a} + {b} = {a+b}")

# while True:
#     a, b = map(int, input().split())
#     if not a and not b:
#         break
#     print(a+b)

# n = int(input())
# print(n*(n+1)//2)

# print("|\\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\\__|")

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|

# a, b, c = map(int, input().rstrip().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)


# 60개를 만들자.
# nl = [0]
# for i in range(1, int(input())):
#     # nl.append(nl[i-1] + (i*(i+1))//2 * 6)
#     nl.append(nl[i-1] + i * 6)
# print(nl)

# for i in range(1, int(input())+1):
#     print('*'*i)

# ans, midx = 0, 0
# for i in range(1, 10):
#     n = int(input())
#     if n > ans:
#         ans, midx = n, i
# print(ans)
# print(midx)


# s, b = map(int, input().split())
# if b >= 45:
#     print(f"{s} {b-45}")
# elif s > 0:
#     print(f"{s-1} {b-45+60}")
# elif not s:
#     print(f"23 {b-45+60}")


# import heapq


# res = []
# for t in range(int(input())):
#     N = int(input())
#     arr = [[0 for i in range(N)] for i in range(N)]
#     cnt = N
#     num, row, col, sw = 0, 0, -1, 1

#     while cnt > 0:

#         for i in range(cnt):
#             num += 1
#             col += sw
#             arr[row][col] = num

#         cnt -= 1

#         for i in range(cnt):
#             num += 1
#             row += sw
#             arr[row][col] = num

#         sw = -sw
#     str_res = ""
#     for i in range(N):
#         for j in range(N):
#             str_res += str(arr[i][j])+" "
#         str_res += "\n" if i < N-1 else ""
#     res.append(str_res)

# for i in range(len(res)):
#     print("#{}\n{}".format(i+1,res[i]))

# 테스트용 추가
# 테스트용 추가 2
# 테스트용 추가 3
# 테스트용 추가 4
# 테스트용 추가 5
# 테스트용 추가 6