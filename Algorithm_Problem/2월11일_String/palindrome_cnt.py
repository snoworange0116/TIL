
t = int(input())
for tc in range(t):
    a = input()
    b = input()
    cnt = 0
    max = 0
    for i in a:
        cnt = b.count(i)
        if cnt > max:
            max = cnt

    print('#{} {}'.format(tc+1, max))


