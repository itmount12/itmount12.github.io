## [파이썬] 데이터 시각화& 기초 통계

1. matplotlib 
- 파이썬에서 데이터 시각화를 위한 라이브러리로, 2d 그래픽 플로팅을 생성하는 데 사용됩니다. 주로 선 그래프, 산점도, 막대 그래프, 히스토그램 등 다양한 종류의 차트를 생성하는 데 활용됩니다. Numpy 배열을 기반으로 하며, 데이터 시각화에 필요한 다양한 기능과 옵션을 제공합니다.
- 주 모듈은 'pyplot' 입니다. matlab 스타일의 인터페이스를 제공하며, 간단하게 그래프를 생성하고 커스터 마이징 할수 있도록 도와주는 역할을 수행합니다.
2. seaborn
- 통계 데이터를 시각화하기 위한 파이썬 라이브러리로, 위의 'matplotlib' 기반으로 반들어진 고수준의 인터페이스를 제공합니다. 이는 간편한 사용법과 함께 세련된 차트 디자인을 제공합니다.


```python
import matplotlib.pyplot as plt  #그림그리기 도구
import pandas as pd
import seaborn as sns  
anscombe = sns.load_dataset("anscombe") 
print(anscombe)
print(type(anscombe))
```

       dataset     x      y
    0        I  10.0   8.04
    1        I   8.0   6.95
    2        I  13.0   7.58
    3        I   9.0   8.81
    4        I  11.0   8.33
    5        I  14.0   9.96
    6        I   6.0   7.24
    7        I   4.0   4.26
    8        I  12.0  10.84
    9        I   7.0   4.82
    10       I   5.0   5.68
    11      II  10.0   9.14
    12      II   8.0   8.14
    13      II  13.0   8.74
    14      II   9.0   8.77
    15      II  11.0   9.26
    16      II  14.0   8.10
    17      II   6.0   6.13
    18      II   4.0   3.10
    19      II  12.0   9.13
    20      II   7.0   7.26
    21      II   5.0   4.74
    22     III  10.0   7.46
    23     III   8.0   6.77
    24     III  13.0  12.74
    25     III   9.0   7.11
    26     III  11.0   7.81
    27     III  14.0   8.84
    28     III   6.0   6.08
    29     III   4.0   5.39
    30     III  12.0   8.15
    31     III   7.0   6.42
    32     III   5.0   5.73
    33      IV   8.0   6.58
    34      IV   8.0   5.76
    35      IV   8.0   7.71
    36      IV   8.0   8.84
    37      IV   8.0   8.47
    38      IV   8.0   7.04
    39      IV   8.0   5.25
    40      IV  19.0  12.50
    41      IV   8.0   5.56
    42      IV   8.0   7.91
    43      IV   8.0   6.89
    <class 'pandas.core.frame.DataFrame'>
    

seaborn 의 내장 데이터인 anscombe 를 불러왔습니다. 이는 데이터 프레임형태의 데이터 입니다. 


```python
anscombe.groupby('dataset').agg(['mean', 'std','var'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">x</th>
      <th colspan="3" halign="left">y</th>
    </tr>
    <tr>
      <th></th>
      <th>mean</th>
      <th>std</th>
      <th>var</th>
      <th>mean</th>
      <th>std</th>
      <th>var</th>
    </tr>
    <tr>
      <th>dataset</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>I</th>
      <td>9.0</td>
      <td>3.316625</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>2.031568</td>
      <td>4.127269</td>
    </tr>
    <tr>
      <th>II</th>
      <td>9.0</td>
      <td>3.316625</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>2.031657</td>
      <td>4.127629</td>
    </tr>
    <tr>
      <th>III</th>
      <td>9.0</td>
      <td>3.316625</td>
      <td>11.0</td>
      <td>7.500000</td>
      <td>2.030424</td>
      <td>4.122620</td>
    </tr>
    <tr>
      <th>IV</th>
      <td>9.0</td>
      <td>3.316625</td>
      <td>11.0</td>
      <td>7.500909</td>
      <td>2.030579</td>
      <td>4.123249</td>
    </tr>
  </tbody>
</table>
</div>



이 데이터는 4개의 유형으로 나누어 지는데, 평균, 표준편차, 분산이 모두 동일한 데이터입니다. 


```python
anscombe.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 44 entries, 0 to 43
    Data columns (total 3 columns):
     #   Column   Non-Null Count  Dtype  
    ---  ------   --------------  -----  
     0   dataset  44 non-null     object 
     1   x        44 non-null     float64
     2   y        44 non-null     float64
    dtypes: float64(2), object(1)
    memory usage: 1.2+ KB
    

시각화를 위해서 이 데이터를 유형별로 슬라이싱 해보겠습니다.


```python
dataset_1 = anscombe[anscombe['dataset']=='I']  
dataset_2 = anscombe[anscombe['dataset']=='II']
dataset_3 = anscombe[anscombe['dataset']=='II']
dataset_4 = anscombe[anscombe['dataset']=='IV']
```

그래프를 그리기 위해 각 데이터셋의 x 와 y 값을 별도의 시리즈 화 하도록 하겠습니다.


```python
x1 = dataset_1['x']
y1 = dataset_1['y']
x2 = dataset_2['x']
y2 = dataset_2['y']
x3 = dataset_3['x']
y3 = dataset_3['y']
x4 = dataset_4['x']
y4 = dataset_4['y']
```


```python
from scipy.stats import linregress 
```

scipy.stats 모듈에서 선형 회귀 분석을 수행하는 함수를 호출하였습니다. 이 함수를 사용하면 주어진 두 변수 간의 선형 관계를 분석할 수 있습니다. 이 함수는 여러 통계치를 반환하여 선형 회귀의 결과를 제공합니다.

##  회귀 분석이란?

여러 자료들 간의 관계성을 수학적으로 추정하고, 설명하는 자료 분석의 기법입니다.  인과관계를 증명하는 메소드가 아닌, 인과 관계를 상정하고 그 모델을 구현하는 것입니다. 

회귀 분석은 생물학자 프랜시스 골턴이 '평균으로의 회귀'  현상을 증명하기 위해 만든 것으로 알려져 있습니다.  평균 회기라는 말은. 부모자식간 키를 측정한 결과가 예측 범위를 급격히 벗어난 값을 측정했으더, 다시 새로운 측정시에는 평균에 가까워지는 경향성을 일반화 하기 위해 만든 용어입니다. 

현대에 와서 회귀의 의미는 퇴색되고, 독립 변수와 종석 변수를 설정하고 이들의 관계를 통계적으로 살펴 보는 방법론을 회귀 분석이라고 명하고 있습니다. 

'선형성' 이란?
- 간단하게 설명하자면, 어떤 수(독립변수) 에 다른 수(편향) 을 더하거나, 곱했을때(가중치) , 어떤 특정 값(종속 변수) 가 나온다는 것을 의미합니다.


```python
#회귀선 계산
#두 변수간에 선형관계를 모델링 - 기울기, 절편, 상관계수, 가설검정, 표준오차
from scipy.stats import linregress 
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x1, y1)
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2, y2)
slope3, intercept3, r_value3, p_value3, std_err3 = linregress(x3, y3)
slope4, intercept4, r_value4, p_value4, std_err4 = linregress(x4, y4)

```

linregress(x1,y1) 객체는 두 값을 입력 받으면 이를 독립 변수와 종속 변수로 인식하고 그에 따른 회귀 직선 통계치를 제공합니다.

- slope: 회귀 선의 기울기
- intercept: 회귀선의 y 절편
- r-value: 상관 계수로, 두 변수 관의 관련성의 정도를 의미합니다. -1에 가까우면 음의 상관 관계, 1에 가까우면 양의 상관관계 0에 가까울수록 상관이 없습니다.
- p_value(유의 확률): 가설 검정에서 얻은 p_value 값 : 두 변수 간의 상관 관계가 우연히 발생한 것인지 를 검증합니다. 일반적인 유의 수준 0.05 보다 작은 값이 나오면 대립 가설이 채택 되어 유의미한 상관 관계로 간주됩니다.
- std_err: 기울기의 표준 오차: 기울기 추정치의 정확성을 나타냅니다. 보통 표준편차/표본크기의 제곱근 형식으로 나타내며, 이 값이 작을수록 직선이 높은 신뢰도를 가짐을 의미합니다.

유의 확률의 공식 ->
- [정규화 한 값: 값-평균/표준편차/루트 표본크기 ] 를 표준 정규분포 표에서 확인.


```python
fig=plt.figure() 
axis1 = fig.add_subplot(2,2,1) 
axis2 = fig.add_subplot(2,2,2)
axis3 = fig.add_subplot(2,2,3)
axis4 = fig.add_subplot(2,2,4)
axis1.plot(x1, intercept1+slope1*x1, color='red', label = "Regression Line")
axis2.plot(x2, intercept2 + slope2*x2, color='g', label='Regression Line')
axis3.plot(x3, intercept3 + slope3*x3, color='b', label='Regression Line')
axis4.plot(x4, intercept4 + slope4*x4, color='violet', label='Regression Line')
```


    
![png](output_22_0.png)
    


위의 코드를 살펴 보겠습니다.
1. fig 라는 객체 생성: 시각화를 그려낼 객체(도화지와 같은 역할을 수행.)
2. axis1=fig.add_subplot(2,2,1)
- subplot 함수는 여러 개의 그래프를 하나의 그림에 나타내도록 합니다. 즉 axis 1은 4등분 된 도화지의 왼쪽 위 부분입니다.
3. axis1.plot(x1, intercept1+slope1*x1, color='red', label = "Regression Line")
- 풀어서 설명하겠습니다. axis1 이라는 figure 의 가장왼쪽 부분에, x값은 =x1, y값은=intercept1+slope1*x1 인 그래프를 그리겠다는 의미입니다. 또 그 색상은 붉은 색, 그리고 파라미터 label은 그림들을 구분할 수 있도록 이름을 붙힌 것입니다.


```python
plt.show()
```

예시 연습


```python
x5= [x for x in range(-50,50)]
y5=[x**3+2*(x**2)-4 for x in range(-50,50)]
x6= [x for x in range(-50,50)]
y6=[3*(x**2)+4*x for x in range(-50,50)]
fig2= plt.figure()
axis1= fig2.add_subplot(2,1,1) #2행으로 나누고, 1열로 나눔. 
axis2= fig2.add_subplot(2,1,2)
axis1.plot(x5,y5,color='red',label='3차함수',linestyle='--')
axis2.plot(x6,y6,color='blue',label='도함수')
fig2.tight_layout()
plt.show()
```


    
![png](output_26_0.png)
    


회귀선을 보면 모든 그래프가 동일한 직선 관계를 보이고 있습니다. 그렇다면 실제 데이터도 그럴까요?
이를 확인 하기 위해 이번에는 x,y 를 순서쌍으로 나타내 표시해 보록 하겠습니다.


```python
fig=plt.figure() #큰 도화지 생성
axis1 = fig.add_subplot(2,2,1) #2행 2열짜리의 1번째 따로 도화 
axis2 = fig.add_subplot(2,2,2)
axis3 = fig.add_subplot(2,2,3)
axis4 = fig.add_subplot(2,2,4)

axis1.plot(dataset_1['x'], dataset_1['y'],'o')  #'o' 점으로 표현하겠다는 뜻.
axis2.plot(dataset_2['x'], dataset_2['y'], 's') 
axis3.plot(dataset_3['x'], dataset_3['y'], '^',markersize=10) 
axis4.plot(dataset_4['x'], dataset_4['y'], 'x',markerfacecolor='r')

axis1.set_title('dataset_1')
axis2.set_title('dataset_2')
axis3.set_title('dataset_3')
axis4.set_title('dataset_4')

fig.tight_layout() #그래프 끼리 겹치지 않도록 하는 메서드
plt.show()  #지금까지 표시한 그래프를 한꺼번에 출력해라
```


    
![png](output_28_0.png)
    


실제로 순서 쌍 형태로 그래프를 확인해 보면, 전부 다른 데이터임을 알 수있습니다. 이는 데이터를 통계적 수치로만 판단할 것이 아닌 시각화를 통해 인사이트를 얻어야 함을 내포하고 있습니다.

## plot 의 주요 파라미터
- x 데이터, y 데이터 (그래프의 x와 y 축에 해당하는 데이터)
- 마커스타일 = 'x', '^', 's'  
- color: 선 또는 마커의 색상
- lableㅣ:그래프의 범례에 표시 될 항목의 레이블 지정
- linestyle: '-' 실선 , '--' 대시선
- markerfacecolor: 마커의 내부 색상
- markersize: 마커의 크기

## 2. 히스토그램 :plt.his()

히스토 그램은 도수 분포표를 그래프로 나타냇 것으로, 가로축은 계급, 세로축은 도수(회수나 개수) 를 나타냅니다.
- 도수 분포표: 특정 구간에 속하는 자료의 개수를 나태는 표.


```python
data = [1,2,2,3,3,3,4,4,5,5,5,5]
plt.figure()
plt.hist(data, bins=5, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('x축 레이블')
plt.ylabel('y축 레이블')
plt.title('히스토그램 제목')
plt.grid(True) #x,y 눈금선 표시
plt.show()
# data: 데이터
# bins: 구간(bin)의 개수
# color: 막대의 색상
# alpha: 투명도  - 낮으면 더 투명
# edgecolor: 막대의 테두리 색상
# density: 확률 밀도로 표시
```


    
![png](output_33_0.png)
    


plt.hist(data, bins=5, color='blue', alpha=0.7, edgecolor='black') 의 인자를 자세히 살펴 보겠습니다.

plt.hist -> 히스토그램을 만드는 메서드 입니다.
- data= 데이터의 분포를 나타내는데 쓸 배열 혹은 순차적인 자료형입니다.
- bins= 계급의 수: 총 5개의 계급을 나누어 그리겠다는 뜻입니다.
- alpha= 선명도로 값이 0에 가까워질수록 더 투명해 집니다.
- edgecolor: 막대의 태두리 색상을 의미합니다.
- density: 이 값을 True 로 하면, 히스토그램의 높이가 아닌 막대의 전체 면적이 1이 되도록 값들을 정규화 합니다. 이를 통해 히스토 그램이 확률 밀도 함수의 근사로 사용 될 수 있습니다.


```python
data = [1,2,2,3,3,3,4,4,5,5,5,5]
plt.figure()
plt.hist(data, bins=5, color='blue', alpha=0.7, edgecolor='black'
        ,density=True)
plt.xlabel('x축 레이블')
plt.ylabel('y축 레이블')
plt.title('히스토그램 제목')
plt.show()

```


    
![png](output_36_0.png)
    


위와같이 density를 True 로 설정하면, y값이  도수가 아닌 확률 밀도로써 표현 되어집니다. 

##  확률 밀도와 밀도 함수

1. 확률 밀도 : 확률 변수가 특정 구간에 속할 확률을 나타내는 함수로, 이를 통해 해당 구간에서의 상대적인 확률을 계산합니다. 즉 첫 번째 사각형(1.0~1.5와 2.0) 사이에 있을 확률이 10퍼센트라는 것으로 변경됩니다. (density=True) 일 경우
- 설명: 연속형 자료에서 특정 값에서의 확률은 0이 됩니다.(무수히 많은 실수들로 구성되어 있기에), 따라서 확률 밀도 함수는 특정 값 근처에 위치할 확률을 '길이' 혹은 '구간' 별로 나타내는 함수입니다.
2. 확률 밀도 함수 (PDF)
- 확률변수의 가능한 값들에 대한 확률 밀도를 나타내는 함수입니다. 확률 변수의 확률 분포를 정의하는 함수입니다.
- 수학적 정의로써 확률 밀도 함수는 누적 확률 함수를 적분한 함수입니다. 
- 설명: 확률 변수의 확률 분포를 수학적으로 정의하고, 어떤 값에 대한 확률 밀도를 제공하는 함수입니다. 확률 변수가 특정 값에 속할 확률은 해당 값에서의 PDF값(y값) 에 연결됩니다. pdf 의 면적은 항상 1이 되어야 합니다. (0<=확률<=100%) 
3. 확률 변수
- 확률 변수는 실험 또는 관찰 결과를 수치적으로 나타내는 변수입니다.  또 이 값이 특정한 분포를 따르는 변수를 의미합니다.
#### 확률 변수의 두가지 유형
1.  이산 확률 변수: 확률 변수가 취할 수 있는 값이 이산적인 경우를 나타냅니다. 예를 들어 주사위 던지기에서 나온 숫자 들이 이산 확률 변수의 예입니다. (1,2.4,5,6) (가위,바위,보) 이산 확률 변수의 확률 분포는 확률 질량함수를 사용하여 나타낼 수 잇습니다.
2. 연속 확률 변수: 확률 변수가 취할 수 있는 값들이 연속적인 경우를 나타냅니다. 예를 들어 온도나 시간 혹은 키와 같은 경우가 연속 확률 변수의 예입니다. 연속 확률 변수의 확률 분포는 확률 밀도 함수를 사용하여 나타낼 수 있습니다.
- 예시: 어떤 사람의 키가 170~ 171 일 확률 :
- 예시2: 시곗바늘이 12와 1사이에 있을 확률: 1/12

이번에는 seaborn 으로 히스토 그램을 그려보도록 하겠습니다.


```python
sns.histplot(data, bins=5, color='blue', kde=True)
plt.show()
```


    
![png](output_41_0.png)
    


## kde=True?

Kernel Density Estimation :커널 밀도 추정 을 통해 주어진 데이터 셋의 확률 밀도 함수를 근사적으로 나타내는 부드러운 곡선입니다. 
이는 히스토그램의 불연속적인 특정을 극복하고, 데이터 분포를 더 부드럽게 시각화 할 수 있게 해 줍니다. 
1. 커널 선택-> 이 경우 가우시안 커널 선택
2. 대역폭 선택.> 커널 함수의 산포를 결정하는데, 값이 클수록 완만하고, 작을수록 부드러운 밀도추정 곡선이 생성됨.
3. 커널 함수 적용, 각각의 이산적인 데이터 포인트를 중심으로 선택된 커널 함수를 적용합니다.
4. 모든 커널 합산: 각 데이터 포인트에서 얻은 값을 합하여 전체 데이터의 확률 밀도함수: 확률 분포를 얻습니다.
5. 이렇게 얻어진 확률 분포는 실제 확률이 아니라 엄밀히 말하면 밀도를 추정한 곡선입니다.

커널이란?
- 주어진 데이터 포인트 주변에 특정 형태의 함수를 배치하는 데 쓰이는 소규모 함수입니다. 커널 함수는 데이터 포인트를 중심으로 작용하며, 데이터의 확률 밀도 함수를 근사화 하는데에 도움이 됩니다.
- 쉽게 설명하면, 데이터 포인트를 부드럽게 만들어 주는 역할을 합니다. 어떤 지점에서의 데이터가 하나의 데이터가 아닌 그 주변에 퍼져 있는 것으로(연속형의 느낌을 가질수 있도록) 
- 가우시안 커널이 주로 사용 되며, 데이터 포인트 주변에 가중치를 둡니다. 
- 대역폭: 각 포인트 주변에 얼마나 넓게 커널을 펼칠지를 결정하는 매개 변수입니다.


```python
import random
import numpy as np
```


```python
data = [1,2,2,3,3,3,4,4,5,5,5,5]
h= 5
def gausian(u):
    return np.exp(-(np.abs(u)**2/2)/(h*np.sqrt(2*np.pi)))
```


```python
len_array= 1000
p_x= np.zeros(len_array)
x=np.array(sorted(np.random.uniform(-10,10,len_array)))
for x_i in data:
    u=(x-x_i)/h
    p_x_i=np.array(gausian(u)/len(data))
    p_x+=p_x_i
    sns.lineplot(x=x,y=p_x_i,color='black', linestyle='--')
    
sns.lineplot(x=x, y=p_x, color='blue').set(title='gausian kde', xlabel='x', ylabel='Density Function')
sns.rugplot(data, height=0.02, color='red')
```




    <Axes: title={'center': 'gausian kde'}, xlabel='x', ylabel='Density Function'>




    
![png](output_47_1.png)
    


- u: 커널 함수의 맥락에서 사용되는 변수입니다. 주어진 데이터의 각 데이터 포인트와 일정한 간격으로 정의된 배열 x 간의 정규화된 차이입니다.
- p_x_i: 각 개별 데이터 포인트의 확률 밀도 함수입니다. 이 주변에 대해 가우시안 밀도 함수가 적용되어서 계산됩니다.
- p_x 는 각 개별 데이터 포인트의 기여를 모두 합한 전체적인 확률 밀도 함수입니다. 각 데이터 포인트의 기여를 누적합니다.

표준 정규 분포

표준 정규 분포는 평균이 0이고 표준 편차가 1인 정규 분포를 의미합니다. 이 분포는 종 모양의 곡선으로, 평균을 중심으로 좌우 대칭이며, 표준 편차가 1이므로 분포의 폭이 정규화 되어 있습니다. 

정규 분포란?
통계학의 주 확률 분포로, 연속형 확률 분포로 종 모양의 곡선으로 나타내여 집니다. 정규 분포는 자연계의 많은 현상에 적용될수 있는 함수입니다. (이게 가능한 이유는 큰수의 법칙, 중심 극한 정리에 의해 표본 수가 커지면 커질수록 모수의 분포가 정규 분포에 가까워지는 경향을 보이는 것으로 알고 있습니다.)


```python
from scipy.stats import norm
data=np.random.randn(1000)
```

np.random.randn(1000) 는 표준정규분포에서 1000개의 난수를 생성하는 코드입니다. 확률 분포= 확률 밀도 함수라고 생각하면 됩니다.


```python
plt.hist(data, bins=30, density=True, alpha=0.8, color='black',edgecolor='r')
xmin, xmax=plt.xlim()
```


    
![png](output_54_0.png)
    


xmin, xmax :plt.xlim() 는 data 의 극대, 극소값을 튜플로 반환하는데, 이 값을 xmin.xmax 가 할당 받았습니다.
-plt.lim () 함수는 현재 그림의 x축 범위를 결정할 때 주어진 데이터의 최소값과 최대값을 고려합니다. 주어진 데이터에 따라서 x축 범위가 자동으로 조절되며, xmin 과 xmax 변수에 할당합니다.


```python
x = np.linspace(xmin, xmax, 100) #xmin , xmax 100의 균등한 데이터 출력
p= norm.pdf(x,0,1)#x데이터, 0평균, 1표편 , x값에서 확률 밀도 값을 반환(kde)
plt.plot(x,p, 'k', linewidth=2)
plt.title('표준 정규분포와 히스토그램')
plt.xlabel('값')
plt.ylabel('밀도')
plt.show()

```

    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 48128 (\N{HANGUL SYLLABLE MIL}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 46020 (\N{HANGUL SYLLABLE DO}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 54364 (\N{HANGUL SYLLABLE PYO}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 51456 (\N{HANGUL SYLLABLE JUN}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 51221 (\N{HANGUL SYLLABLE JEONG}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 44508 (\N{HANGUL SYLLABLE GYU}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 48516 (\N{HANGUL SYLLABLE BUN}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 54252 (\N{HANGUL SYLLABLE PO}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 50752 (\N{HANGUL SYLLABLE WA}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 55176 (\N{HANGUL SYLLABLE HI}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 49828 (\N{HANGUL SYLLABLE SEU}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 53664 (\N{HANGUL SYLLABLE TO}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 44536 (\N{HANGUL SYLLABLE GEU}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 47016 (\N{HANGUL SYLLABLE RAEM}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    C:\Users\zuise\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:152: UserWarning: Glyph 44050 (\N{HANGUL SYLLABLE GABS}) missing from current font.
      fig.canvas.print_figure(bytes_io, **kw)
    


    
![png](output_56_1.png)
    


x = np.linspace(xmin, xmax, 100)
- 넘파이의 메서드로, 주어진 범위에서 균일한 간격으로 일정 개수의 실수 값을 생성하는 함수입니다.
- 즉 여기서는 극대, 극소의 값 사이에 100개의 값을 생성하여 배열에 할당한 것입니다.


```python
plt.hist(data, bins=30, density=True, alpha=0.8, color='black',edgecolor='r')
xmin, xmax=plt.xlim()
x = np.linspace(xmin, xmax, 100) #xmin , xmax 100의 균등한 데이터 출력
p= norm.pdf(x,0,1)#x데이터, 0평균, 1표편 , x값에서 확률 밀도 값을 반환(kde)
plt.plot(x,p, 'k', linewidth=2) # 선의 굵기를 나타냅니다.
plt.title('표준 정규분포와 히스토그램')
plt.xlabel('값')
plt.ylabel('밀도')
plt.show()

```


    
![png](output_58_0.png)
    


산점도 그래프  plt.scatter(x,y)


```python
tips = sns.load_dataset("tips").sort_values(by='total_bill')
```


```python
tips.head()
# type(tips)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>67</th>
      <td>3.07</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
    </tr>
    <tr>
      <th>92</th>
      <td>5.75</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>111</th>
      <td>7.25</td>
      <td>1.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
    </tr>
    <tr>
      <th>172</th>
      <td>7.25</td>
      <td>5.15</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>149</th>
      <td>7.51</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



산점도란?
산점도는 두 변수 간의 관계를 시각화 하기 위해 사용되는 그래프 입니다. 각각의 데이터 포인트는 좌표 평면 상의 한 점으로 나타내어지며, x출은 하나의 변수를, y 축은 다른 변수를 나타냅니다.
- 주로 변수 간의 상관 관계나, 분포, 군집을 볼떄 사용됩니다. 


```python
plt.scatter(tips['total_bill'], tips['tip'])
plt.title('Scatterplot of Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
```




    Text(0, 0.5, 'Tip')




    
![png](output_63_1.png)
    


산점도를 통해 총 식사비와 팁의 상관 관계를 추정할수 있습니다. 

### 박스 플롯 plt.boxplot()
박스 플롯은 데이터의 분포와 이상치를 시각적으로 나타내는 그래프 입니다. 주로 데이터의 중앙값, 사분위수, 이상치 등을 확인하는데 사용됩니다.


```python
paper = plt.figure() 
axes1 = paper.add_subplot(1, 1, 1)
axes1.boxplot( [tips[tips['sex'] == 'Female']['tip'],   tips[tips['sex'] == 'Male']['tip']], 
            labels=['Female', 'Male'],showfliers=True) #이상치(outliers)안보여주기
axes1.set_title('Boxplot of Tips by Sex')

```




    Text(0.5, 1.0, 'Boxplot of Tips by Sex')




    
![png](output_66_1.png)
    


박스 플롯의 주요 요소
1. 상자: 데이터의 사분위수를 나타내며, 데이터의 중앙값이 상자 내부의 노란 선으로 표시되었습니다.
2. 수염: 상자에서 벗어난 데이터의 범위를 나타냅니다. 일반적으로 1.5*iqr(사분위 범위) 를 벗어난 데이터는 이상치로 표시됩니다.
3. 이상치: 상자 밖의 개별 데이터 포인트로, 주로 수염을 벋어난 값 중에서 특이 값을 나타냅니다.
4. 사분위수: 3사분위수에서 1사분위수를 뺀 범위를 사분위 범위로, 상자의 세로 길이가 이 범위 입니다.(iqr)

axes1.boxplot( [tips[tips['sex'] == 'Female']['tip'],   

tips[tips['sex'] == 'Male']['tip']], 

            labels=['Female', 'Male'],showfliers=True) 

boxplot 의 파라미터
- x or y: 데이터를 입력합니다.하나만 사용해야 합니다.
- data: 데이터 프레임 형태로 데이터를 입력 할때 사용합니다.
- hue: 범주형 변수를 기준으로 여러 그룹을 비교할때 사용합니다.
- orient:박스 플롯의 방향을 설정합니다. 'v','h' :수직, 수평
- width: 상자의 폭을 설정합니다.
- showfliers: 이상치를 표시할지 여부를 결정하는데  FALSE 값은 이상치를 드러내지 않습니다.
- whis: 수염의 길이로, 기본 값은 1,5입니다.
- notch: 상자의 중앙 부분을 확대하여 신뢰 구간을 나타낼지 여부를 결정합니다.
- color: 상자와 수염의 색상을 설정합니다.
- sym: 이상치를 표시하는데 사용되는 기호를 설정합니다.
- linewidth: 상자의 테두리 두께를 설정합니다.


```python
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")  # 예제 데이터 로드

# 박스 플롯 그리기
sns.boxplot(x="day", y="total_bill", data=data, hue="sex", width=0.7, linewidth=2)
            #범주     # 이산                       #성별
# 제목 설정
plt.title('Box Plot')

# 그래프 표시
plt.show()

```


    
![png](output_72_0.png)
    


다변량 데이터


```python
def recode_sex(sex):
    if sex == 'Female':
        return 0 
    else:
        return 1

tips['sex_num'] = tips['sex'].apply(recode_sex)
```

성별을 가변수화하는 함수로, 성별을 0,1로 나누어 새로운 열에 할당하였습니다.


```python
import matplotlib.pyplot as plt

scatter_plot = plt.figure() 
axes1 = scatter_plot.add_subplot(1, 1, 1) 

#x, y, c   다변량 데이타 그래프 그리기
scatter = axes1.scatter(  x=tips['total_bill'],  y=tips['tip'],    
    s=tips['size'] * 20,  #데이터프레임의 'size' 열 값을 20배로 확장하여 마커 크기를 설정
    c=tips['sex_num'],  # 'sex_num'에 따라 다른 색상 지정
    alpha=0.5, cmap='cividis')
# cmap = 'viridis'
# 'plasma', 'inferno', 'magma', 'cividis'
plt.colorbar(scatter, label='Sex')
axes1.set_title('Total Bill vs Tip Colored by Sex and Sized by Size') 
axes1.set_xlabel('Total Bill') 
axes1.set_ylabel('Tip') 
```




    Text(0, 0.5, 'Tip')




    
![png](output_76_1.png)
    



```python
tips.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>sex_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>67</th>
      <td>3.07</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>5.75</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>111</th>
      <td>7.25</td>
      <td>1.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>172</th>
      <td>7.25</td>
      <td>5.15</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>149</th>
      <td>7.51</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



0. 데이터 프레임과 함께 데이터를 해석해 보겠습니다.
1. size 의 경우 식사를 한 인원수입니다.
  - s=tips['size'] * 20 
  - 파리미터 x 는 마커의 크기를 설정하는 함수인데, 이 값이 size 에 비례해서 크고 작도록 시각화 하였습니다.
2. c=tips['sex_num'] 
  - 파라미터 c 는 마커의 색상을 나타내는 함수인데, 남녀에 따라 색상이 다르도록 지정하였습니다.
3. plt.colorbar(scatter, label='Sex') 는 색상 바를 그리는 코드입니다.
- scatter 객체에 대한 컬러바를 생성하기 위해 scatter를 입력하였습니다.
- label='sex' 성별에 따라 색상이 지정되었다는 것을 의미하기 위해 레이블을 지정한 것입니다.

다변량 산점도 플롯


```python
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species', markers=['o','s','d'])
plt.show()
```

    C:\Users\zuise\anaconda3\Lib\site-packages\seaborn\axisgrid.py:118: UserWarning: The figure layout has changed to tight
      self._figure.tight_layout(*args, **kwargs)
    


    
![png](output_80_1.png)
    


## sns.pairplot 의 인자들에 대해 설명하겠습니다.
1. data: 페어플롯의 기반이 되는 데이터 셋입니다.
2. hue: 분류하고자 하는 범주열의 이름입니다. 종속변수인 'species' 를 사용하여 종에 따른 색상을 구분하였습니다.
3. markers: 각각의  범주에 따라 사용할 마커의 종류를 리스트로 지정하는데, 범주에 수에 따라 지정해야 합니다.
4. diag_kind : 주대각 선에 그려진 그래프의 종류입니다. hist 와 kde 두개의 인자를 가지며, 각각 히스토그램과 kde 를 그려냅니다.
5. plot_kws: 주대각선에 그려질 그래프의 추가 인자를 설정하는 딕셔너리입니다. 

### sns.distplot(단일 변수, kde,hist, rug)
디스트 플롯은 단일 변수의 분포를 확인하기 유용한 그래프를 생성하는데 사용됩니다. 주로 히스토 그램과 커널 밀도 추정 곡선을 동시 표기화 하여 시각화하는데 활용됩니다.

histogram + kde
- data: 시각화하려는 데이터를 지정합니다.
- bins: 히스토그램의 구간(bin) 수를 조절합니다.
- kde: 커널 밀도 추정 그래프를 표시할지 여부를 결정합니다. 기본값은 True
- color: 그래프의 색상을 설정합니다.
- rug: 데이터 포인트(실제 관측치)의 위치를 간단한 선분으로 나타내는 역할을 수행합니다. 이는 주어진 데이터의 위치를 시각적으로 표현하여 밀도 추정 곡선과 히스토그램과 함께 데이터의 분포를 더 잘 이해할 수 있게 합니다.


```python
sns.distplot(tips['total_bill'], kde=True, hist=True , rug=True) #default kde=True
```

    C:\Users\zuise\AppData\Local\Temp\ipykernel_13564\3864347321.py:6: UserWarning: 
    
    `distplot` is a deprecated function and will be removed in seaborn v0.14.0.
    
    Please adapt your code to use either `displot` (a figure-level function with
    similar flexibility) or `histplot` (an axes-level function for histograms).
    
    For a guide to updating your code to use the new functions, please see
    https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
    
      sns.distplot(tips['total_bill'], kde=True, hist=True , rug=True) #default kde=True
    




    <Axes: xlabel='total_bill', ylabel='Density'>




    
![png](output_84_2.png)
    


sns.coutplot
- 범주형 변수의 카테고리 별로 데이터 포인트의 개수를 세어 막대 그래프로 나타내는 seaborn 함수입니다. 주로 범주형 변수의 분포를 확인 할때 사용됩니다.


```python
sns.countplot(data=tips, x='day')
```




    <Axes: xlabel='day', ylabel='count'>




    
![png](output_86_1.png)
    



```python
sns.countplot(data=tips, x='sex')
```




    <Axes: xlabel='sex', ylabel='count'>




    
![png](output_87_1.png)
    


## sns.regplot(x,y, 데이터)

산점도와 회귀 선을 같이 표시하는 데이터로, 두 변수 간의 선형성을 시각적으로 확인할 수 있습니다.


```python
sns.regplot(x='total_bill', y='tip', data=tips)
```




    <Axes: xlabel='total_bill', ylabel='tip'>




    
![png](output_90_1.png)
    



```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
sns.regplot(x=x1, y=y1, data=dataset_1, ax=axes[0, 0])
sns.regplot(x=x2, y=y2, data=dataset_2, ax=axes[0, 1])
sns.regplot(x=x3, y=y3, data=dataset_3, ax=axes[1, 0])
sns.regplot(x=x4, y=y4, data=dataset_4, ax=axes[1, 1])
```




    <Axes: xlabel='x', ylabel='y'>




    
![png](output_91_1.png)
    


1. **fig, axes = plt.subplots(2, 2, figsize=(10, 8))**
- plt.subplots 를 사용해 2*2 형태의 서브 플롯이 있는 그림을 생성합니다.
- fig 는 전체 그림을 나타내는 figure객체 입니다.plt.figure() 
- axes 는 각 서브 플롯에 대한 axes 객체를 가진 2차원 배열입니다.
2. sns.regplot(x=x1, y=y1, data=dataset_1, ax=axes[0, 0])
- **ax= axes[0,0]: 그래프를 그릴 서브 플롯을 지정합니다. 여기서는 0행 0열 부분에 해당 그래프를 그립니다.**
- ax 인자를 활용해, matplotlib 의 서브 플롯에 seaborn 그래프를 그릴 수 있습니다. 이를 통해 seaborn 의 높은 수준의 통계 그래픽 함수와 matplotlib 의 서브 플롯을 함께 사용 할 수 있습니다.
- matplotlib 의 서브 플롯에 seaborn 그래플르 그리는 것은 seborn 의 고유 기능이 아니므로 matplotlib을 사용하여 서브플롯을 그리고, ax 인자를 사용해 seaborn 을 나눠 그리면 됩니다.

## 산점도+ 히스토그램 . jointplot

jointplot 은 두 변수 간의 이변량 관계를 시각화 하는데 사용되는 함수로, 각 변수의 산점도와 히스토그램을 함께 보여주는 편리한 그래프를 생성합니다.
- 이변량 관계의 시각화
- 단변량 분포의 확인
- 추세의 확인 (회귀선을 통한)
- 커널 밀도의 추정


```python
sns.jointplot(x='total_bill', y='tip', data=tips)
```




    <seaborn.axisgrid.JointGrid at 0x258fa767590>




    
![png](output_95_1.png)
    



```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
sns.jointplot(x=x1, y=y1, data=dataset_1, ax=axes[0, 0],kind='kde')
sns.jointplot(x=x2, y=y2, data=dataset_2, ax=axes[0, 1],kind='kde')
sns.jointplot(x=x3, y=y3, data=dataset_3, ax=axes[1, 0])
sns.jointplot(x=x4, y=y4, data=dataset_4, ax=axes[1, 1])
```

    C:\Users\zuise\AppData\Local\Temp\ipykernel_13564\2237893360.py:2: UserWarning: Ignoring `ax`; jointplot is a figure-level function.
      sns.jointplot(x=x1, y=y1, data=dataset_1, ax=axes[0, 0],kind='kde')
    C:\Users\zuise\AppData\Local\Temp\ipykernel_13564\2237893360.py:3: UserWarning: Ignoring `ax`; jointplot is a figure-level function.
      sns.jointplot(x=x2, y=y2, data=dataset_2, ax=axes[0, 1],kind='kde')
    C:\Users\zuise\AppData\Local\Temp\ipykernel_13564\2237893360.py:4: UserWarning: Ignoring `ax`; jointplot is a figure-level function.
      sns.jointplot(x=x3, y=y3, data=dataset_3, ax=axes[1, 0])
    C:\Users\zuise\AppData\Local\Temp\ipykernel_13564\2237893360.py:5: UserWarning: Ignoring `ax`; jointplot is a figure-level function.
      sns.jointplot(x=x4, y=y4, data=dataset_4, ax=axes[1, 1])
    




    <seaborn.axisgrid.JointGrid at 0x258fb664890>




    
![png](output_96_2.png)
    



    
![png](output_96_3.png)
    



    
![png](output_96_4.png)
    



    
![png](output_96_5.png)
    



    
![png](output_96_6.png)
    


#커널 밀도 추정 그래프 sns.kdeplot
- 단일 변수 혹은 이변량 데이터의 커널 밀도 추정을 시각화 하는데 사용됩니다. 커널 밀도 추정은 데이터의 분포를 부드럽게 나타내어 주는데 도움이 되며, 히스토 그램 대신 사용됩니다.


```python
sns.kdeplot(x=tips['total_bill'], y=tips['tip'], shade=True)
```

    C:\Users\zuise\AppData\Local\Temp\ipykernel_13564\2296107636.py:1: FutureWarning: 
    
    `shade` is now deprecated in favor of `fill`; setting `fill=True`.
    This will become an error in seaborn v0.14.0; please update your code.
    
      sns.kdeplot(x=tips['total_bill'], y=tips['tip'], shade=True)
    




    <Axes: xlabel='total_bill', ylabel='tip'>




    
![png](output_98_2.png)
    


등고선의 해석
- shade=True 로 지장하면 등고선과 함께 데이터의 밀ㄷ를 나타내는 색상으로 채워진 그래프가 등장합니다.
- 등고선 자체는 밀도의 높 낮이를 의미하며, 색상이 진할수록 높은 밀도를 나타냅니다. 
- 등고선이 더 진한 부분은, total_bill 과 tip 변수가 공통으로 존재하는 곳으로, 해당 지역에서는 두 변수간의 상관 관계가 높다고 볼수 있습니다.
- 등고선이 의미한 지역은 데이터가 희소하거나, 두 변수간의 관계성이 낮은 지역입니다.
- 등고선의 간격은 밀도의 레벨을 나타내며, 등고선의 간격이 좁으면 좁을수록, 해당 지역에 데이터가 많이 있다는 것을 의미합니다.


```python
sns.kdeplot(x=tips['total_bill'], y=tips['tip'], shade=False)
```

    C:\Users\zuise\AppData\Local\Temp\ipykernel_13564\587601426.py:1: FutureWarning: 
    
    `shade` is now deprecated in favor of `fill`; setting `fill=False`.
    This will become an error in seaborn v0.14.0; please update your code.
    
      sns.kdeplot(x=tips['total_bill'], y=tips['tip'], shade=False)
    




    <Axes: xlabel='total_bill', ylabel='tip'>




    
![png](output_100_2.png)
    



```python
sns.kdeplot(x='sepal_length', hue='species', data=iris)
# sns.pairplot(iris, hue='species', markers=['o','s','d'])
```




    <Axes: xlabel='sepal_length', ylabel='Density'>




    
![png](output_101_1.png)
    


일변량 데이터에 대해서는 이와같이 kde 커널 함수를 시각화합니다.

## barplot 
- x에는 범주형 자료, y 에는 해당 범주별 통계값 배열이 들어가게 됩니다.
- 중앙의 검은 막대는 오차 막대로, 해당 범주에서의 값의 신뢰구간을 나타냅니다.
- 범주의 항목별 평균을 막대 그래프로 나타내고, 오차 막대로 신뢰 구간을 나타냅니다.


```python
tips.head(4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>sex_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>67</th>
      <td>3.07</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>5.75</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>111</th>
      <td>7.25</td>
      <td>1.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>172</th>
      <td>7.25</td>
      <td>5.15</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.barplot(x='time', y='total_bill', data=tips)
```




    <Axes: xlabel='time', ylabel='total_bill'>




    
![png](output_105_1.png)
    



```python
sns.barplot(x='day', y='tips', data=tips)
```




    <Axes: xlabel='day', ylabel='tip'>




    
![png](output_106_1.png)
    



```python
sns.barplot(x='day', y='total_bill', data=tips)
```




    <Axes: xlabel='day', ylabel='total_bill'>




    
![png](output_107_1.png)
    


바이올린 플롯

주어진 데이터 셋에서 범주형 변수에 따른 연속형 변수의 분포를 바이올린 플롯을 나타냅니다. 바이올린 플롯은 매트랩과 kde 를 결합하여 각 범주에서의 값의 분포를 나타냅니다.
- 바이올린 플롯을 수직으로 절반으로 나누면 각 범주에서 값의 분포를 나타내는 kde 그래프가 됩니다.
- 바이올린 플롯의 직선은 플롯의 중앙값을 나타냅니다. 이 직선은 분포에서 중앙값에 해당하는 위치를 표시합니다. 
- 즉 바이올린 플롯은 kde 그래프와 박스 플롯을 동시에 구현해 데이터의분포를 파악하는 그래프 입니다.


```python
sns.violinplot(x='time', y='total_bill', data=tips)
```




    <Axes: xlabel='time', ylabel='total_bill'>




    
![png](output_110_1.png)
    



```python

```
