'''
스위치 켜고 끄기

남학생은 스위치 번호가 자기가 받은 수의 배수 스위치들의 상태를 바꾼다.
여학생은 자기가 받은 수를 기준으로 좌우가 대칭이면서 가장 긴 만큼 스위치 상태를 바꾼다.
- 남학생은 쉬울 듯 하고.
- 여학생은 while로 구현하면 좋을 듯 하다.
- 남학생도 while로. 범위를 모르니.

입력
스위치 갯수 100이하 자연수
스위치 상태. 켜졌으면 1 꺼졌으면 0 빈칸 존재.
학생수
남1여2, 받은 자연수가 한 줄로 학생 수만큼 반복 표현

출력
스위치 상태 출력.
출력 시 20개씩, 띄어쓰기해서 출력.
켜진건1 꺼진건0
'''
# 입력
n = int(input())
g = list(map(int, input().split()))
m = int(input())
stu = []
for _ in range(m) :
    stu.append(list(map(int, input().split())))
# 남자일 때 g 변경 함수
def male(num) :
    k = 1
    while num * k - 1 <= len(g)-1 :
        if g[num * k - 1] == 1 :
            g[num * k - 1] = 0
        else :
            g[num * k - 1] = 1
        k += 1
    return
# 여자일 때 g 변경 함수
def female(num) :
    k = 0
    # 양옆이 같다면 k증가, 아니면 탈출
    while num - 1 - k >= 0 and num - 1 + k <= len(g) - 1 :
        nx, px = num - 1 - k, num - 1 + k
        if g[nx] == g[px] :
            k += 1
        else : 
            break
    k -= 1 # 증가한 k가 조건 만족 못했으니 1 빼기
    for i in range(num - 1 - k, num + k) :
        if g[i] == 1:
            g[i] = 0
        else :
            g[i] = 1
    return

# 실행
for bg, number in stu :
    if bg == 1 :
        male(number)
    else :
        female(number)
# 출력
for i in range(n) :
    print(g[i], end=' ')
    if (i + 1) % 20 == 0 :
        print()


