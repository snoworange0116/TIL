t = int(input())
for tc in range(1, t+1):
    arr = input()
    arr_len = len(arr)
    lst = []
    for i in range(arr_len):
        if arr[i] == '(' or arr[i] == '{':
            lst.append(arr[i])
        elif arr[i] == ')' or arr[i] == '}':
            if len(lst) == 0:
                lst = [arr[i]]
                break
            elif (arr[i] == ')' and lst[-1] != '(') or (arr[i] == '}' and lst[-1] != '{'):
                lst = [arr[i]]
                break
            else:
                lst.pop()

    if len(lst) == 0:
        print('#{} {}'.format(tc,1))
    else:
        print('#{} {}'.format(tc,0))



