t = int(input())
for tc in range(1, t+1):
    n,m = map(int,input().split())
    tmp_arr = list(map(int,input().split())) # 대기 피자 리스트
    arr = tmp_arr[:n] # 화덕의 크기인 n만큼만 피자를 넣어줌
    arr_idx = list(range(n)) # 마지막 나오는 피자의 idx를 출력해야 하므로 화덕에 처음 넣어지는 피자 idx 초기화
    idx = n # idx는 다음 넣어질 피자의 idx 값
    while True:
        for i in range(n): # n번 도는건 화덕이 1회전 하는걸 의미
            tmp = arr[i] // 2
            if tmp == 0:
                if idx < m: # 현재 idx가 전체 대기 피자만큼의 수보다 작거나 같게되면
                    arr[i] = tmp_arr[idx] # 치즈가 다 녹은곳에 새로운 피자를 넣어주고
                    result = (arr_idx[i] + 1) # 방금 빼낸 피자의 idx값을 결과로 저장
                    arr_idx[i] = idx # 새로 넣은 피자의 idx를 arr_idx자리에 저장
                    idx += 1 # 한개의 피자를 새로 넣었으므로 다음 피자로 넘어가기 위해 idx를 1 증가
                else:
                    arr[i] = 0 # 새로 넣을 피자가 없기때문에 현재 인덱스의 피자 값을 0으로 수정
                    if arr_idx[i] != -1: # arr_idx[i]가 -1이 아니라면 마지막으로 남은 피자가 녹았다는 뜻이 된다.
                        result = arr_idx[i] + 1 # 그러므로 마지막 피자의 idx의 값을 result에 저장
                    arr_idx[i] = -1 # 초과된 피자의 idx값은 -1을 할당
            else:
                arr[i] = tmp # 나누기 2 한 값이 0이 아니면 그 값으로 재할당
        if sum(arr) == 0: # n개 화덕의 모든 피자의 합이 0이되면 무한루프 탈출
            break
    print('#{} {}'.format(tc,result))