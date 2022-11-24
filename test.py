
n, x = map(int, input().split())
nl = list(map(int, input().split()))
nnl = [i for i in nl if i < x]
print(*nnl)

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