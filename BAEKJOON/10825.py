'''
국영수

n명의 이름과 국영수 점수 제시
1. 국어점수 감소
2. 같으면 영어 증가
3. 같으면 수학 감소
4. 같으면 이름 사전순 증가

입력
학생 수 n 제시
이름 국 영 수 공백 제시

출력
n개 줄 학생 이름 출력
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())
g = sorted([list(input().rstrip().split()) for _ in range(n)], key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in g: print(i[0])
