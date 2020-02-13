t = int(input())
for tc in range(1,t+1):
    n = int(input())
    n //= 10
    odd_num = 1
    even_num = 3
    sum_num = 0

    if n % 2 == 1:
        for i in range(n//2+1):
            odd_num += sum_num
            if sum_num == 0:
                sum_num = 4
            else:
                sum_num *= 4
        print('#{} {}'.format(tc,odd_num))
    else:
        for i in range(n//2):
            even_num += sum_num
            if sum_num == 0:
                sum_num = 8
            else:
                sum_num *= 4
        print('#{} {}'.format(tc,even_num))
