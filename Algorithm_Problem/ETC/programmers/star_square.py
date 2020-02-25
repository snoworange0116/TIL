a, b = map(int,input().split())
for i in range(b):  # answer = ('*'*a +'\n')*b
    arr = ''
    for j in range(a):
        arr += '*'
    print(arr)