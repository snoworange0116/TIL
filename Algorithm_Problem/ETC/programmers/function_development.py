def solution(progresses, speeds):
    answer = []
    while progresses:
        flag = 0
        tmp_idx = []
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                tmp_idx.append(i)
                flag = 1
            else:
                break
        if flag == 1:
            answer.append(len(tmp_idx))
        for i in range(len(tmp_idx)):
            progresses.pop(0)
            speeds.pop(0)  #speeds의 list도 같이 pop해줘야하는 걸 간과함.
    return answer

progresses = [40, 93, 30, 55, 60, 65]
speeds = [60, 1, 30, 5 , 10, 7]
print(solution(progresses,speeds))
