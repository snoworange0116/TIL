import sys

sys.stdin = open('sample_input.txt','r')

numbers = int(input())

for number in range(1,numbers+1):
    result = 0
    length = int(input())
    a = list(map(int,input().split(" ")))
    max = a[0]
    for i in range(1, length):
        if a[i] >= max:
            max = a[i]

    min = a[i]
    for i in range(1, length):
        if a[i] <= min:
            min = a[i]

    result = max - min
    print("#{} {}".format(number, result))
