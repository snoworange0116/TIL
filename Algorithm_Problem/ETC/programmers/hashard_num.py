def solution(x):
    answer = False
    tmp = sum(list(map(int,str(x))))
    if x % tmp == 0:
        answer = True
    return answer

arr = 12
print(solution(arr))