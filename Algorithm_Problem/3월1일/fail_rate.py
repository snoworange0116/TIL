def solution(N, stages):
    answer = []
    tmp = {}
    n = len(stages)
    for i in range(1,N+1):
        if n != 0:
            tmp[i] = stages.count(i)/n
            # print(stages.count(i)/n)
            n -= stages.count(i)
        else:
            tmp[i] = 0
    res = sorted(tmp.items(), key = lambda x : (-x[1],x[0]))
    for j in res:
        answer.append(j[0])
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = [3,4,2,1,5]
print(solution(N,stages))