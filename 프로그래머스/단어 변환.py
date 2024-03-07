from collections import deque

def check(word1, word2):
    if len(word1) != len(word2): return False
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]: cnt+=1
        if cnt > 1: return False
    return True if cnt else False

def solution(begin, target, words):
    endPoint = 0
    if begin == target: return 0
    try: endPoint = words.index(target)+1
    except: return 0

    words = [begin] + words
    n = len(words)
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if check(words[i], words[j]):
                g[i].append(j)
                g[j].append(i)
    v = [0]*n
    q, ans, v[0] = deque([(0, 0)]), 0, 1
    while q:
        num, cnt = q.popleft()
        for i in g[num]:
            if v[i]: continue
            q.append((i, cnt+1))
            v[i] = 1
            if i == endPoint: return cnt+1
    return ans