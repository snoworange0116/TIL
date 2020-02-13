t = int(input()) # 노선 수

for t_i in range(t):
    k, n, m = map(int, input().split())
    # k = 충전으로 최대이동정류장 수
    # n = 종점정류장 숫자
    # m = 충전기 설치된 정류장 수
    m_lst = list(map(int, input().split()))
    m_lst.append(n)
    last = 0
    cnt = 0

    for j in range(m+1):
        if k >= m_lst[j] - last:
            pass
        else:
            last = m_lst[j-1]
            cnt += 1

    for i in range(m-1):
        if m_lst[i+1] - m_lst[i] > k:
            cnt = 0
            break

    print("#{} {}".format(t_i+1, cnt))