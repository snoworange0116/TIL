# sw expert linked_list 5122
t = int(input())
for tc in range(1,t+1):
    N,M,L = map(int,input().split()) # N:수열의길이, M:추가 횟수, L:출력할 인덱스 번호
    arr = list(map(int,input().split()))
    for i in range(M):
        temp_input = (list(input().split()))
        # print(temp_input)
        if temp_input[0] == 'I':
            arr.insert(int(temp_input[1]),temp_input[1])
        elif temp_input[0] == 'D':
            arr.pop(int(temp_input[1]))
        elif temp_input[0] == 'C':
            arr[int(temp_input[1])] = temp_input[2]
    if L >= len(arr):
        result = -1
    else:
        result = arr[L]
    print('#{} {}'.format(tc, result)) 