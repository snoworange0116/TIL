def solution(n):
    tmp = list(str(n))
    tmp.sort(reverse=True)
    tmp = ''.join(tmp)
    return int(tmp)

n = 1123048
print(solution(n))