def solution(s):
    result = ''
    tmp = list(s)
    tmp.sort(reverse=True)
    for i in tmp:
        result += i
    return result

