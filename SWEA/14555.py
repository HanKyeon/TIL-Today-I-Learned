'''
공과 잡초
'''

for testcase in range(1, int(input())+1):
    s = input()
    c = 0
    for i in range(0, len(s)-1):
        if s[i:i+2] == '(|' or s[i:i+2] == '|)' or s[i:i+2] == '()':
            c += 1
    print(f"#{testcase} {c}")