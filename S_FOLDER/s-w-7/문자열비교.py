'''
str2 안에 str1과 일치하는 것이 있는지 확인
'''

for testcase in range(1, int(input())+1):
    str1, str2 = list(input()), list(input())
    ln1, ln2 = len(str1), len(str2)
    c = 0
    for i in range(ln2-ln1+1):
        ss = str2[i:i+ln1]
        if ss == str1:
            c += 1
    print(f"#{testcase} {c}")