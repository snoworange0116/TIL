def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isnumeric():
                pass
            else:
                return False
        return True
    else:
        return False

# s = 'a234'
# s = '1234