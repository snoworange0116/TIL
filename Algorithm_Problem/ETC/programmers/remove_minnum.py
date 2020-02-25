def solution(arr):
    num = min(arr)
    arr.remove(num)
    if len(arr) >= 1:
        return arr
    else:
        return [-1]