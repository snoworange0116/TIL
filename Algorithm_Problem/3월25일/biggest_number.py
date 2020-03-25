def solution(numbers):
    result = ''
    # numbers.sort(key=lambda x : (str(x)[0]),reverse=True)
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x : (x*4)[:4],reverse=True)
    print(numbers)
    for i in numbers:
        result += str(i)
    return int(result)

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))