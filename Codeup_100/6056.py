a, b = int(input().split())
c, d = bool(a), bool(b)

print((c and (not d)) or ((not c) and d))