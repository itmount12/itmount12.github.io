# [파이썬] 예외 처리

파이썬으로 코딩을 하다 보면 여러 오류들과 마주하게 됩니다.


```python
a,b,c ="강아지",'강','송'
a-b+c
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[1], line 2
          1 a,b,c ="강아지",'강','송'
    ----> 2 a-b+c
    

    TypeError: unsupported operand type(s) for -: 'str' and 'str'


이와 같이 문법과 맞지 않는 코딩을 하였을 경우 이를 고지하는 역할을 합니다. 또한 오류가 발생한 부분에서 프로그램도 비정상 종료됩니다.

하지만 정말 프로그램이 비정상 종료를 방치해서 큰 문제를 야기하는 경우가 존재합니다. 이러한 이유에서 프로그램에게 미리 이런 상황이 발생하였을 경우에는 이렇게 대처해라.즉 재난대책을 세워두는 것을 예외처리라고 합니다.

에러가 발생하였을때에 코드를 다음과 같이 수정해 보겠습니다.


```python
try:
    a-b+c
except:
    print("데이터 타입을 확인해 보세요?")
```

    데이터 타입을 확인해 보세요?
    

파이썬은 여러 자료 형태를 전부 다루기 때문에, 다양한 에러를 발생합니다. 그중에서 특정한 에러만 처리를 하고 싶다면 except 뒤에 에러명을 적으면 됩니다.


```python
try:
    a-b+c
except TypeError:
    print("데이터 타입을 확인해 보세요?")
```

    데이터 타입을 확인해 보세요?
    

예외를 발생시킨 변수가 무엇인지 확인할 수도 있습니다.


```python
try:
    a-b+c
except TypeError as e:
    print(f"데이터 타입을 확인해 보세요?,{e}")
```

    데이터 타입을 확인해 보세요?,unsupported operand type(s) for -: 'str' and 'str'
    

주로 발생하는 예외들을 정리해 보겠습니다.
- Exception: 모든 예외의 상위 클래스: 모든 예외를 출력하는 예외의 왕
- ValueError: 값의 형식이 잘못 되었을때 발생하는 에러
- IndexError: 범위를 벗어났을 때 발생하는 에러
- ZeroDivisionError: 0으로 나눴을 때의 에러
- TypeError: 연산 중 자료가 다를 때의 에러
- KeyError: 사전에 없는 키를 입력했을 때 에러
- FileNotFoundError: 존재하지 않는 파일이 에러

여러 가지의 예외를 처리할 수도 있습니다.


```python
try:
    file= open('example.txt','r')
    content=file.read()
    file.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except PermissionError:
    print("권한이 없습니다")
```

    파일을 찾을 수 없습니다.
    

모든 예외를 처리하고 싶다면 Exception 을 사용하면 됩니다.


```python
try:
    file= open('example.txt','r')
    content=file.read()
    file.close()
except Exception as e:
    print("예외 발생",e)
```

    예외 발생 [Errno 2] No such file or directory: 'example.txt'
    

**사용자 정의 예외 발생**

예외를 강제적으로 발생시켜야 할 경우도 존재합니다. 파이썬의 연산상으로는 문제가 없지만,

실제로 결과가 나왔을때 문제가 되는 경우도 존재하기 때문입니다.

이런 경우 raise를 통해 예외를 발생시킵니다.


```python
def divid(x):
    if x == 0:
        raise ZeroDivisionError("0으로는 나눌수 없습니다.")
    return 4/x
```


```python
divid(0)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    Cell In[10], line 1
    ----> 1 divid(0)
    

    Cell In[9], line 3, in divid(x)
          1 def divid(x):
          2     if x == 0:
    ----> 3         raise ZeroDivisionError("0으로는 나눌수 없습니다.")
          4     return 4/x
    

    ZeroDivisionError: 0으로는 나눌수 없습니다.


사용자가 아예 새로운 종류의 예외를 만들고 싶을 때에는? 클래스 상속!

파이썬에 기본으로 내장된 예외들 말고 새로운 종류의 예외를 만들고 싶을 때, Exception 클래스를 상속받아 예외를 만들면 됩니다.


```python
class OverflowError(Exception):
    def __init__(self):
        super().__init__('100점을 초과할 수 없습니다.')

def get_points():
    try:
        x=int(input())
        if x>100:
            raise OverflowError
        print(f"{x}점")
    except Exception as e:
        print('예외발생',e)

get_points()
```

    106
    예외발생 100점을 초과할 수 없습니다.
    

이 방식으로도 상속 받을 수 있습니다.


```python
class BelowZeroError(Exception):
    def __init__(self, num):
        self.num = num
        self.message = "음수값은 점수가 될 수 없습니다."

    def __str__(self):
        return f"{self.num}은 {self.message}"

def get_points2():
    try:
        x = int(input())
        if x < 0:
            raise BelowZeroError(x)
        else:
            print(f"{x}점")
    except BelowZeroError as e:
        print(e)

get_points2()

```

    -97
    -97은 음수값은 점수가 될 수 없습니다.
    

이 부분은 클래스를 더 공부한 후 다시 수정, 보완하겠습니다.


```python

```
