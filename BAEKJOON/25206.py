'''
너의 평점은

전공 평점구해라.
A+	4.5
A0	4.0
B+	3.5
B0	3.0
C+	2.5
C0	2.0
D+	1.5
D0	1.0
F	0.0

입력
20줄 제시

출력
전공 평점 출력
학점*과목평점 합을 학점의 총합으로 나눈 값
'''
import sys
input = sys.stdin.readline
parse = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0,
    "P":0.0
}
hak, gwa = 0, 0
for _ in range(20):
    a, b, c = input().rstrip().split()
    if c == "P":
        continue
    b=int(b[0])
    hak += b
    gwa += parse[c]*b
print(f"{gwa/hak}")
