# 파이참 string 제출용

# 문장에서 어떤 것을 검색 했을 때 그 갯수

# 10개의 테케
# 문장 길이 1000자 이하
# 검색하는 문자열의 길이는 최대 10을 넘지 않은
# 한 문장에서는 하나의 문자열만 검색

# #1 #2 #3 검색할 문자열 갯수

for testcase in range(1, 11) :
    _ = input()
    f = input()
    s = input()
    c, fl = 0, len(f)
    for i in range(len(s)-fl+1) :
        if f == s[i:i+fl] :
            c += 1
    print(f"#{testcase} {c}")



