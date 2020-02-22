# Collections Module

### 1. deque

```python
import collections
d = collections.deque([1,2,3,4,5])

#오른쪽 추가
d.append(6)

#왼쪽에 추가
d.appendleft(0)

#입력값 순환하며 오른쪽에 추가
d.extend([6,7])

#입력값 순환하며 왼쪽에 추가
d.extendleft([0,-1,-2])

#값 삭제
d.remove(3)

#오른쪽의 끝 값 가져오면서 deque에서 제거
val = d.pop()

#왼쪽의 끝 값 가져오면서 deque에서 제거
d.popleft()

# 값 회전
d.rotate(1)
## 출력 : [5,1,2,3,4]
d.rotate(-1)
## 출력 : [2,3,4,5,1]
```

