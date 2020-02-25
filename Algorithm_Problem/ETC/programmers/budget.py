def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    for idx,val in enumerate(d):
        if val <= budget:
            d[idx] = 0
            budget -= val
            cnt += 1
    return cnt