for t_i in range(10):
    n = int(input())
    box_lst = list(map(int, input().split()))

    for i in range(n):
        a = box_lst.index(max(box_lst))
        box_lst[a] -= 1
        b = box_lst.index(min(box_lst))
        box_lst[b] += 1

    print("#{} {}".format(t_i + 1, max(box_lst) - min(box_lst)))