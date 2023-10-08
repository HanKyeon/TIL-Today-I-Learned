'''
접미사 배열

모든 접미사 추출해서 사전순 정렬
'''
s, ans = input(), []
for i in range(len(s)): ans.append(s[i:])
ans.sort()
for i in ans: print(i)