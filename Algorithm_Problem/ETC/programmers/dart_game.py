def solution(dartResult):
    tmp = []
    flag = 0
    for i,v in enumerate(dartResult):
        if flag == 0:
            if v.isnumeric():
                if not dartResult[i+1].isnumeric():
                    tmp.append(int(v))
                else:
                    tmp.append(int(v + dartResult[i+1]))
                    flag = 1
            else:
                if v == 'S':
                    pass
                elif v == 'D':
                    tmp[-1] = int(tmp[-1]) ** 2
                elif v == 'T':
                    tmp[-1] = int(tmp[-1]) ** 3
                elif v == '*':
                    if len(tmp) == 1:
                        tmp[-1] = int(tmp[-1]) * 2
                    elif len(tmp) >= 2:
                        tmp[-1],tmp[-2] = int(tmp[-1]) *2, int(tmp[-2]) *2
                elif v == '#':
                    tmp[-1] = int(tmp[-1]) * -1
        else:
            flag = 0
    return sum(tmp)

dartResult = '1D2S3T*'
print(solution(dartResult))