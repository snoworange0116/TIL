# itertools Module

### itertools를 이용한 순열

```python
from itertools import permutations
lst = ['a','b','c']
lst2 = list(itertools.permutations(lst,2))
print(lst2)

# 출력 : [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
```

### itertools를 이용한 조합

```python
import itertools
lst = ['a','b','c']
lst2 = list(itertools.combinations(lst,2))

print(lst2)

# 출력 : [('a', 'b'), ('a', 'c'), ('b', 'c')]
```

