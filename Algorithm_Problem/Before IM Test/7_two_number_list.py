t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))
    max_num = 0
    if n <= m:
        for i in range(m - n + 1):  # 3
            temp = 0
            for j in range(n):  # 5
                temp += n_arr[j] * m_arr[i + j]
            if max_num < temp:
                max_num = temp
    else:
        for i in range(n - m + 1):
            temp = 0
            for j in range(m):
                temp += n_arr[i + j] * m_arr[j]
            if max_num < temp:
                max_num = temp

    print('#{} {}'.format(tc + 1, max_num))