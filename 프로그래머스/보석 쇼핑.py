def solution(gems):
    uniqueGems, parse = set(gems), {}
    for idx, gemName in enumerate(uniqueGems): parse[gemName] = idx
    n = len(uniqueGems)
    ans = [0, len(gems)]
    cnt, v = [0]*n, set([gems[0]])
    sta, end = 0, 0
    cnt[parse[gems[0]]] = 1
    while end < len(gems):
        if len(v) < n:
            end+=1
            if end < len(gems):
                v.add(gems[end])
                cnt[parse[gems[end]]] += 1
        elif len(v) == n:
            if end-sta < ans[1]-ans[0]: ans = [sta+1, end+1]
            cnt[parse[gems[sta]]] -= 1
            if not cnt[parse[gems[sta]]]: v.remove(gems[sta])
            sta+=1
    return ans