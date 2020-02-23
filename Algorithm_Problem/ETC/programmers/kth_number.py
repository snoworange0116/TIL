def solution(array,commands):
    tmp = []
    answer = []
    for i in range(3):
        tmp.append([])
        tmp[i] = array[commands[i][0]-1:commands[i][1]]
        tmp[i].sort()
        answer.append(tmp[i][commands[i][2]-1])
    return answer

# 입력
# array = [1,5,2,6,3,7,4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array,commands))
