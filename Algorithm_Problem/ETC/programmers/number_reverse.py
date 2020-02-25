def solution(n):
    answer = list(str(n))
    answer.reverse()
    for i,v in enumerate(answer):
        answer[i] = int(answer[i])

    return answer