t = int(input())
for tc in range(1, t + 1):
    a = input()
    dic = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
    lst = []
    result2 = 0

    for i in a:
        if i in dic.keys():
            dic[i] += 1

    for i in range(len(a) // 3):
        lst.append(a[i * 3:(i + 1) * 3])

    while (lst):
        temp = lst.pop(0)
        if temp in lst:
            result2 = 'ERROR'
            break

    result = [13 - dic['S'], 13 - dic['D'], 13 - dic['H'], 13 - dic['C']]

    if result2 == 'ERROR':
        print("#{} {}".format(tc, result2))
    else:
        print("#{} {}".format(tc, " ".join(map(str, result))))