'''
두개의 문자열 str1, str2
str1에 포함된 글자들이 str2에 몇개씩 들어있는지 찾고, 그 중 가장 많은 글자 갯수를 출력해라

파이썬 딕셔너리 사용금지

입력
테케 T 1이상 50이하
테케 별 길이 N 5이상 100이하인 문자열 str1이랑 M 10이상 1000이하인 str2

출력
# 최대갯수
'''
def maxv(li):
    c = -10e9
    for i in li:
        if c < i:
            c = i
    return c

for testcase in range(1, int(input())+1):
    s1, s2 = list(set(list(input()))), list(input())
    s1l = len(s1)
    c1 = [0]*s1l
    for i in s2:
        for j in range(s1l):
            if i == s1[j]:
                c1[j] += 1
    print(f"#{testcase} {maxv(c1)}")




