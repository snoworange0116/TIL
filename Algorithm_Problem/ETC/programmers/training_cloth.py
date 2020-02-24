def solution(n, lost, reserve):
    for i in lost:
        if i not in reserve:
            if i-1 in reserve and i-1 not in lost:
                reserve.remove(i-1)
                continue
            elif i+1 in reserve and i+1 not in lost:
                reserve.remove(i+1)
                continue
            else:
                n -= 1
        else:
            reserve.remove(i)
            continue
    return n

n = 10
lost = [3,9,10]
reserve = [3,8,9]
print(solution(n,lost,reserve))