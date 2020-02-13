
test_num = int(input())

for t in range(test_num):
    num = int(input())
    numbers = input()
    dic = {}
    lst = []
    for val in numbers:
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 1

    temp = 0
    for i,v in dic.items():
        if v >= temp:
            temp = v
    for i2,v2 in dic.items():
        if v2 == temp:
            lst.append(i2)
    max_num = max(lst)

    print("#{} {} {}".format(t+1,max_num,temp))
