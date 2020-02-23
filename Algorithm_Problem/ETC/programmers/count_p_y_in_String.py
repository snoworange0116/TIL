def solution(s):
    p_cnt,y_cnt = 0,0
    for i in s.lower():
        if i == 'p':
            p_cnt += 1
        elif i == 'y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    else:
        return False

# s = 'pPoooyY'
# s = 'Pyy'