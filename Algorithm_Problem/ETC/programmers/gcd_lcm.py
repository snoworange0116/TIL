def solution(n, m):
    x,y = n,m
    if x < y:
        x, y = y, x
    while y:
        x,y = y, x % y
    gcd = x
    lcm = n*m // gcd
    return [gcd,lcm]

print(solution(12,6))