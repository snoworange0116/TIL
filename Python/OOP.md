# OOP (객체지향 프로그래밍)



- 클래스 변수
  
  클래스의 속성
  모든 인스턴스가 공유
  Class.class_variable과 같이 접근 최상단에 위치
```python
class TestClass:
	class_variable = '클래스 변수'

tc = TestClass()

TestClass.class_variable # 이렇게 접근
tc.class_variable # 인스턴스 -> 클래스 -> 전역 순서로 이름공간 탐색하기 때문에, 접근 가능
```



- 인스턴스 변수
  
  각 인스턴스들의 고유한 변수
  self.instance_variable로 접근

```python
class TestClass:
    def __init__(self, arg1, arg2):
        self.instance_var1 = arg1
        self.instance_var2 = arg2
        
    def status(self):
        return self.instance_var1, self.instance_var2
    
tc = TestClass(1,2)
tc.instance_var1 # 이렇게 접근
tc.instance_var2 # 이렇게 접근
tc.status()
```



- 클래스 메서드

  클래스가 사용할 메서드이다.
  정의 위에 @classmethod 데코레이터를 사용한다.
  반드시 첫 인자로 cls를 받도록 정의한다.

```python
class MyClass:
    @classmethod
    def class_method_name(cls, arg1, arg2, ...):
```



- 인스턴스 메서드

  인스턴스가 사용할 메서드이다.
  메서드 정의 위에 데코레이터가 없으면, 자동으로 인스턴스 메서드가 된다.
  첫 번째 인자로 self를 받도록 정의한다. 이 때, 자동으로 인스턴스 객체가 self가 된다.

```python
class MyClass:
    def instance_method_name(self, arg1, arg2, ...):
        ...
my_instance = MyClass()
my_instance.instance_method(.., ..) 
# 인스턴스 생성 후 메서드를 호출하면 자동으로 첫 번째 인자로 인스턴스가 들어간다.
```

  

- 스태틱(정적) 메서드

  클래스가 사용할 메서드다.
  정의 위에 @staticmethod 데코레이터를 사용한다.
  묵시적인 첫 번째 인자를 받지 않는다.
  어떠한 인자도 자동으로 넘어가지 않는다.

```python
class Myclass:
    @staticmethod
    def static_method_name(arg1, arg2, ...):

MyClass.static_method_name(.., ..)
```

  

- 클래스, 인스턴스 메서드 예시

```python
class Doggy:
    num_of_dogs = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Doggy.num_of_dogs += 1
        
    def bark(self):
        print('멍멍')
        
    @classmethod
    def status(cls):
        print(f'현재 강아지는 {cls.num_of_dogs}마리 있습니다.')
        
    @classmethod
    def sell(cls):
        cls.num_of_dogs = 0

d1 = Doggy('초코', 3)
d2 = Doggy('만복이', 7)
d3 = Doggy('이널미', 4)
d1.bark() # 멍멍
```

  

