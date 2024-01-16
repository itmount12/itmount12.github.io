# [파이썬] 오라

1. 오라클에 맞는 버전을 위 사이트에서 찾기
2. 다운로드
3. 압축풀기
4. 경로 복사
5. 환경설정에서 추가


```python
!pip install cx_Oracle
```

    Collecting cx_Oracle
      Downloading cx_Oracle-8.3.0.tar.gz (363 kB)
         ---------------------------------------- 0.0/363.9 kB ? eta -:--:--
         - -------------------------------------- 10.2/363.9 kB ? eta -:--:--
         -------------------------- ----------- 256.0/363.9 kB 2.6 MB/s eta 0:00:01
         -------------------------------------- 363.9/363.9 kB 2.8 MB/s eta 0:00:00
      Installing build dependencies: started
      Installing build dependencies: finished with status 'done'
      Getting requirements to build wheel: started
      Getting requirements to build wheel: finished with status 'done'
      Preparing metadata (pyproject.toml): started
      Preparing metadata (pyproject.toml): finished with status 'done'
    Building wheels for collected packages: cx_Oracle
      Building wheel for cx_Oracle (pyproject.toml): started
      Building wheel for cx_Oracle (pyproject.toml): finished with status 'error'
    Failed to build cx_Oracle
    

      error: subprocess-exited-with-error
      
      Building wheel for cx_Oracle (pyproject.toml) did not run successfully.
      exit code: 1
      
      [8 lines of output]
      <string>:6: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
      C:\Users\user\AppData\Local\Temp\pip-build-env-2nwb7u6f\overlay\Lib\site-packages\setuptools\config\expand.py:133: SetuptoolsWarning: File 'C:\\Users\\user\\AppData\\Local\\Temp\\pip-install-whrblhu3\\cx-oracle_3419c6254cb644469428cc4778720f32\\README.md' cannot be found
        return '\n'.join(
      running bdist_wheel
      running build
      running build_ext
      building 'cx_Oracle' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]
      
      note: This error originates from a subprocess, and is likely not a problem with pip.
      ERROR: Failed building wheel for cx_Oracle
    ERROR: Could not build wheels for cx_Oracle, which is required to install pyproject.toml-based projects
    


```python
import cx_Oracle as oci
```


```python
conn_info = {'user':'scott','password':'tiger','dsn': 'localhost:1521/xe'}
conn=oci.connect(**conn_info) #함수원형, 함수 프로토타입, 함수 시그니쳐

conn.version
```




    '11.2.0.2.0'




```python
cursor = conn.cursor() #커서 객체
```




```python
cursor.execute("select empno, ename, deptno from emp where ename='JAMES'")

```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[27], line 5
          2 #rlt= cursor.fetchall()
          3 #lt
          4 for rs in cursor:
    ----> 5     print(rs[0],rs[1],rs[7])
    

    IndexError: tuple index out of range



```python
name = "'JAMES'"
sql = f"select * from emp where ename ={name}"
print(sql)
cursor.execute(sql)
for rs in cursor:
    print(rs)
```

    select * from emp where ename ='JAMES'
    (7900, 'JAMES', 'CLERK', 7698, datetime.datetime(1981, 12, 3, 0, 0), 950.0, None, 30)
    

오라클 요구 방법


```python
sql3 ='select * from emp where ename=:enm and deptno=:dpn' 
```

바인딩 파라미터

바인딩 파라미터는 SQL 쿼리에서 사용되는 파라미터를 나타냅니다. SQL 쿼리에서 바인딩 파라미터를 사용하면 동적인 값(변하는 값)들을 안전하게 쿼리에 포함시킬 수 있습니다. 이는 주로 데이터베이스와 상호작용하는 애플리케이션에서 사용됩니다.

바인딩 파라미터의 주요 이점은 SQL 인젝션 공격을 방지하는 데 있습니다. SQL 인젝션은 사용자 입력을 통해 악의적인 SQL 코드가 주입되어 데이터베이스에 영향을 미치는 공격입니다. 바인딩 파라미터를 사용하면 사용자 입력이 안전하게 처리되며, 쿼리 문자열에 사용자 입력을 직접 삽입하는 것을 방지할 수 있습니다.

다양한 데이터베이스 시스템에서는 바인딩 파라미터를 사용하는 방법이 조금씩 다를 수 있습니다. 


```python
name = input("이름 입력:")
deptno = input('부서번호 입력:')
cursor.execute(sql3,{'enm':name,'dpn':deptno})
for rs in cursor:
    print(rs)
```

    이름 입력:
    부서번호 입력:
    


```python
cursor.execute('select*from emp')
rows=cursor.fetchmany(2) #2줄만 
for rs in rows:
    print(rs)
```

    (7369, 'SMITH', 'CLERK', 7902, datetime.datetime(1980, 12, 17, 0, 0), 800.0, None, 20)
    (7499, 'ALLEN', 'SALESMAN', 7698, datetime.datetime(1981, 2, 20, 0, 0), 1600.0, 300.0, 30)
    


```python

```


```python

```
