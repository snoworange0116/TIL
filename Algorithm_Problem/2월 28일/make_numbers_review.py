import math

def calc(val,idx):
    global max_val
    global min_val
    if idx == n:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    else:
        if operator_lst[0] > 0:
            operator_lst[0] -= 1
            calc(val + numbers[idx] , idx+1)
            operator_lst[0] += 1
        if operator_lst[1] > 0:
            operator_lst[1] -= 1
            calc(val - numbers[idx] , idx+1)
            operator_lst[1] += 1
        if operator_lst[2] > 0:
            operator_lst[2] -= 1
            calc(val * numbers[idx] , idx+1)
            operator_lst[2] += 1
        if operator_lst[3] > 0:
            operator_lst[3] -= 1
            calc(math.trunc(val / numbers[idx]) , idx+1)
            operator_lst[3] += 1
    return
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    operator_lst = list(map(int,input().split())) # 더하기,빼기,곱하기,나누기
    numbers = list(map(int,input().split()))
    max_val = -999999999
    min_val = 999999999
    calc(numbers[0],1)
    print('#{} {}'.format(tc,abs(max_val - min_val)))