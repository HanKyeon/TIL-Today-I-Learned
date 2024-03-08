def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    ans = 0
    while routes:
        _, end = routes.pop(0)
        while routes and end >= routes[0][0]:
            routes.pop(0)
        ans += 1
    return ans