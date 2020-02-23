def solution(s):
    res = ''
    if int(s) >= 0:
        return int(s)
    else:
        for i in s:
            if i.isdecimal():
                res += i
            else:
                pass
        return -1 * int(res)

