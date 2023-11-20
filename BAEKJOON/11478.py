'''
서로 다른 부분 문자열의 개수

문자열 s 제시, 서로 다른 부분 문자열 구해라. 길이 1이상

입력
'''
s = input()
zh = set()
for i in range(len(s)):
    for j in range(i,len(s)):
        zh.add(s[i:j+1])#i번째 문자부터 부분문자열 구하기
print(len(zh))