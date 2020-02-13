n = int(input())
for tc in range(n):
    a = input()
    b = input()

    len_a = len(a)
    if a in b:
        print('#{} {}'.format(tc+1,1))
    else:
        print('#{} {}'.format(tc+1,0))