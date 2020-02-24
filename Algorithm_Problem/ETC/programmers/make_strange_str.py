def solution(s):
    tmp = list(s)
    flag = 0
    res = ''
    for idx,val in enumerate(tmp):
        if val != ' ':
            if flag == 0:
                tmp[idx] = val.upper()
                flag = (flag + 1) % 2
            else:
                tmp[idx] = val.lower()
                flag = (flag + 1) % 2
        else:
            flag = 0
    for i in tmp:
        res += i
    return res

s = 'abc def ghi'
print(solution(s))