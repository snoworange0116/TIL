def solution(priorities, location):
    pos = []
    for i in range(len(priorities)):
        if i == location:
            pos.append(True)
        else:
            pos.append(False)
    cnt = 0
    max_val = max(priorities)
    while True:
        if max_val > priorities[0]:
            priorities.append(priorities.pop(0))
            pos.append(pos.pop(0))
        else:
            cnt += 1
            priorities.pop(0)
            if pos.pop(0) == True:
                return cnt
            max_val = max(priorities)

priorities = [2, 1, 3, 2]
location = 2
