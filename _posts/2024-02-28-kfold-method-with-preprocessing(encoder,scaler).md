```python
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, cross_validate
```

분포 데이터 생성


```python
korean=np.random.randint(30,100,size=1000)
math=np.random.randint(20,90,size=1000)
eng=np.random.randint(50,100,size=1000)
# 언어, 국어, 영어의 3개를 값을 임의 난수로 배열
data_lst=list(zip(korean,math,eng))
total_array=np.array(data_lst)
```


```python
grade=pd.DataFrame(total_array,columns=['언어','수리','영어'])
grade['평균']=np.mean(total_array, axis=1)
# 구간을 나누는 과정 pd.cut을 이용해 구간 분할
grade['성적 등급']=pd.cut(grade['평균'],bins=9,labels=[9,8,7,6,5,4,3,2,1])
```

# kfold 알고리즘
- 알고리즘의 핵심: 데이터를 훈련용, 검증용으로 나누는 것이 아니라 전체 데이터를 k 개의 알고리즘으로 분할 후, 그중에서 1개의 데이터를 테스트 데이터로, 나머지를 트레이닝 데이터로 사용하여 모델을 학습 시키는 방법
- from sklearn.model_selection import KFold : 일반적인 kfold 분포를 고려하지 않고 데이터를 분할
    - 전체 데이터를 임의로 고려하지 않고 자연스러운 배치의 분포에 조작을 가하지 않고 그대로 적용하기에 회귀 모델에 적용이 가능함
    - 일반화 성능의 평가: 무작위로 분할 된 데이터 이기에, 모델의 일반화 성능을 더 정확하게 고려 하는 것이 가능함.
    - 위의 항목들로 인해 통계적 유의성: 가설의 검증 결과가 임의적인 것이 아니기에 통계적 유의성을 높일 수 있음.
        - 통계적 유의성:가설의 결과가 우연히 발생할 확률이 얼마나 낮은지를 나타내는 개념.
- from sklearn.model_selection import StratifiedKFold : 전체 데이터의 범주를  고려한 데이터 분할 방법
    -  회귀 문제에서는 클래스가 없거나(범주형 변수가 존재하지 않음), 연속적인 값으로 이루어져 있어서 클래스 간의 비율을 유지할 필요가 없습니다. 즉 분포를 고려할 필요가 없으므로 분포를 고려한 kfold 가 유명무실 해짐.
- from sklearn.tree import DecisionTreeClassifier
- from sklearn.model_selection import cross_val_score, cross_validate

- 기본으로 kfold 이나 파라미터를 지정하면 skf 적용 가능

# kfold 메서드: 전체의 분포를 고려하지 않고 kfold 를 수행


```python
feature,label=grade[['언어','수리','영어']].values,grade['성적 등급'].values
kfold = KFold(n_splits=9)
model =DecisionTreeClassifier(random_state=25)
acc_lst=[]
n=0
for train_index, test_index in kfold.split(feature,label):
    n+=1  
    X_train, X_test = feature[train_index], feature[test_index]
    y_train, y_test = label[train_index], label[test_index]
    print('성적 분포:',np.unique(y_train, return_counts=True))
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    accuracy=accuracy_score(y_pred,y_test)
    acc_lst.append(accuracy)
    print(f'{n} 회차 시행')
    print('##정확도:',accuracy)
print('평균 정확도:',round(np.mean(acc_lst),2))
```

    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  58, 103, 188, 181, 172, 100,  56,  12], dtype=int64))
    1 회차 시행
    ##정확도: 0.6875
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  59, 109, 187, 171, 177, 101,  57,  10], dtype=int64))
    2 회차 시행
    ##정확도: 0.6486486486486487
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 17,  62, 105, 196, 175, 172,  95,  57,  10], dtype=int64))
    3 회차 시행
    ##정확도: 0.7027027027027027
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  63, 107, 190, 177, 168,  97,  56,  13], dtype=int64))
    4 회차 시행
    ##정확도: 0.6756756756756757
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 15,  56, 109, 193, 182, 174,  90,  58,  12], dtype=int64))
    5 회차 시행
    ##정확도: 0.7477477477477478
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 19,  62, 106, 192, 174, 170,  98,  56,  12], dtype=int64))
    6 회차 시행
    ##정확도: 0.7477477477477478
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  58, 108, 191, 171, 177,  96,  59,  11], dtype=int64))
    7 회차 시행
    ##정확도: 0.6306306306306306
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  59, 106, 185, 191, 173,  90,  55,  12], dtype=int64))
    8 회차 시행
    ##정확도: 0.6666666666666666
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 19,  59, 107, 182, 178, 177,  97,  58,  12], dtype=int64))
    9 회차 시행
    ##정확도: 0.6756756756756757
    평균 정확도: 0.69
    

# stratified kfold : 전체의 분포를 고려해서 kfold 를 수행


```python
feature,label=grade[['언어','수리','영어']].values,grade['성적 등급'].values
skf = StratifiedKFold(n_splits=9)
model =DecisionTreeClassifier(random_state=25)
n=0
acc_lst=[]
for train_index, test_index in skf.split(feature,label):
    n+=1  
    X_train, X_test = feature[train_index], feature[test_index]
    y_train, y_test = label[train_index], label[test_index]
    print('성적 분포:',np.unique(y_train, return_counts=True))
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    accuracy=accuracy_score(y_pred,y_test)
    acc_lst.append(accuracy)
    print(f'{n} 회차 시행')
    print('정확도:',accuracy)
print('평균 정확도:',round(np.mean(acc_lst),2))

```

    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 17,  59, 106, 190, 178, 174,  96,  56,  12], dtype=int64))
    1 회차 시행
    정확도: 0.625
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  59, 106, 190, 178, 174,  96,  57,  11], dtype=int64))
    2 회차 시행
    정확도: 0.6576576576576577
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  60, 106, 190, 178, 173,  96,  57,  11], dtype=int64))
    3 회차 시행
    정확도: 0.6576576576576577
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  60, 107, 189, 178, 173,  96,  57,  11], dtype=int64))
    4 회차 시행
    정확도: 0.7117117117117117
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  60, 107, 189, 178, 173,  96,  57,  11], dtype=int64))
    5 회차 시행
    정확도: 0.8198198198198198
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  60, 107, 189, 177, 173,  96,  57,  12], dtype=int64))
    6 회차 시행
    정확도: 0.7567567567567568
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  60, 107, 189, 177, 173,  96,  57,  12], dtype=int64))
    7 회차 시행
    정확도: 0.7297297297297297
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 18,  59, 107, 189, 178, 173,  96,  57,  12], dtype=int64))
    8 회차 시행
    정확도: 0.7027027027027027
    성적 분포: (array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64), array([ 17,  59, 107, 189, 178, 174,  96,  57,  12], dtype=int64))
    9 회차 시행
    정확도: 0.7027027027027027
    평균 정확도: 0.71
    

# cross_validate:  for 문을 수행하지 않고  자동으로 cross_valid를 정해 바로 값을 딕셔너리 형태로 반환함


```python
from sklearn.model_selection import cross_val_score, cross_validate
cv_results = cross_validate(model, feature, label, cv=9, scoring='accuracy')
print(round(np.mean(cv_results['test_score']),2))
```

    0.71
    

# 라벨 인코더
- 목적: 머신 러닝에 있어서, 모델이 범주형 변수를 이해하고 모델 내부에 적용하기 위함임.
- method:
   - label 인코딩 메서드: 범주형 변수에  0에서부터 연속된 정수 값을 부여함
   - 이때 범주형 변수에 연속된 값을 포함시키므로 값의 크기에는 산술적인 의미가 부여됨.
    - from sklearn.preprocessing import LabelEncoder


```python
from sklearn.preprocessing import LabelEncoder as le
items=['TV','냉장고','컴퓨터','선풍기','냉장고','커피머신','선풍기','컴퓨터','냉장고']
encoder=le() #라벨 인코더 객체 생성
encoder.fit(items) #학습
label=encoder.transform(items) # 학습된 값을 토대로  인코딩 실시
print('인코딩 변환값:',label)
```

    인코딩 변환값: [0 1 4 2 1 3 2 4 1]
    


```python
print('디코딩 원본값:', encoder.inverse_transform)
print('디코딩 원본값:', encoder.classes_) # 디코딩 메서드 .inverse(역으로)  변환
```

    디코딩 원본값: <bound method LabelEncoder.inverse_transform of LabelEncoder()>
    디코딩 원본값: ['TV' '냉장고' '선풍기' '커피머신' '컴퓨터']
    

원 핫 인코더
- 목적: 라벨 인코딩을 통해 범주형 변수가 수치 데이터로 변환되었는데, 이 과정에서 연속적인 숫자를 넣었기에 의도하지 않는 산술적인 의미가 생성됨-> 상호 연관성이 없는 데이터이기에 산술적인 의미를 제거하고자 원 핫 인코딩을 수행함
- 알고리즘: 각각의 특성치를 이진 분류함.
    - 어떤 특성치에 해당하면 1로, 그게 아닌 것은  0으로 값을 부여하고, 1차원적인 값에 참, 부정 의 bool 형태의 차원을 입력하여 이를 구분함.


```python
from sklearn.preprocessing import LabelEncoder as le
from sklearn.preprocessing import OneHotEncoder as oh
items=['TV','냉장고','컴퓨터','선풍기','냉장고','커피머신','선풍기','컴퓨터','냉장고']
encoder=le()
encoder.fit(items)
label=encoder.transform(items)
# 라벨 인코딩 까지 마친 부분
label=label.reshape(-1,1)
ohe_enocoder=oh() #원 핫 인코더 생성
ohe_enocoder.fit(label)
labels=ohe_enocoder.transform(label)
print(labels)

print(labels.toarray())
```

      (0, 0)	1.0
      (1, 1)	1.0
      (2, 4)	1.0
      (3, 2)	1.0
      (4, 1)	1.0
      (5, 3)	1.0
      (6, 2)	1.0
      (7, 4)	1.0
      (8, 1)	1.0
    [[1. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0.]
     [0. 0. 0. 0. 1.]
     [0. 0. 1. 0. 0.]
     [0. 1. 0. 0. 0.]
     [0. 0. 0. 1. 0.]
     [0. 0. 1. 0. 0.]
     [0. 0. 0. 0. 1.]
     [0. 1. 0. 0. 0.]]
    

# 희소 행렬과 밀집 행렬
 ## print(labels) 희소 행렬
- 희소 행렬이란? 희소 행렬(Sparse Matrix)은 대부분의 요소가 0으로 이루어진 행렬을 말함. 희소 행렬은 데이터의 특성에 따라 자주 발생하며, 메모리와 연산 시간을 효율적으로 사용하기 위해 사용되어진다.

    - 희소 행렬의 특성과 장점: 
     - 0이 아닌 원소의 비율이 매우 낮음.
     - 메모리를 효율적으로 사용하기 위해 0이 아닌 원소만을 저장하고 나머지는 저장하지 않음. 이렇게 하면 메모리 공간의 절약에 있어서 획기적임.  - 집중되는 지점이 0이 아닌 점에 집중하므로 연산량이 빨라짐.
## print(labels.toarray()) 밀집 행렬
 - 밀집 행렬은 모든 원소가 메모리에 저장되어 있음. 메모리를 많이 차지함.
 - 소규모 데이터를 처리하는데 사용됨.
 - 다수의 값이 0이 아닌 경우에 희소 행렬보다 효율적, 선형 대수학적 연산에 사용되는 행렬.


## 피처 스케일링과 정규화
- 목적:서로 다른 변수의 값의 범위를 일정한 수준으로 맞추는 작업
- 특성치들의 특성을 조금 더 잘 드러나게  하거나 모델 자체의 성능을 향상시키기 위함임.
     - 표준화: 데이터 feature 각각의 |평균0 , 분산 1| 가우시안 정규 분포를 가진 값으로 변환.
    - 정규화: 개별 데이터의 크기를 모두 똑같은 단위로 변경


```python
iris=load_iris()
iris_data=iris.data
iris_df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
```


```python
iris_df.head()
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
      <th>sepal length (cm)</th>
      <th>sepal width (cm)</th>
      <th>petal length (cm)</th>
      <th>petal width (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
  </tbody>
</table>
</div>



# from sklearn.preprocessing import StandadScaler : 정규화 스케일링 


```python
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
scaler.fit(iris_df) #학습
iris_scaled=scaler.transform(iris_df) #적용
```


```python
iris_scaled_df=pd.DataFrame(data=iris_scaled, columns=iris.feature_names)
iris_scaled_df
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
      <th>sepal length (cm)</th>
      <th>sepal width (cm)</th>
      <th>petal length (cm)</th>
      <th>petal width (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.900681</td>
      <td>1.019004</td>
      <td>-1.340227</td>
      <td>-1.315444</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.143017</td>
      <td>-0.131979</td>
      <td>-1.340227</td>
      <td>-1.315444</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.385353</td>
      <td>0.328414</td>
      <td>-1.397064</td>
      <td>-1.315444</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.506521</td>
      <td>0.098217</td>
      <td>-1.283389</td>
      <td>-1.315444</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.021849</td>
      <td>1.249201</td>
      <td>-1.340227</td>
      <td>-1.315444</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>1.038005</td>
      <td>-0.131979</td>
      <td>0.819596</td>
      <td>1.448832</td>
    </tr>
    <tr>
      <th>146</th>
      <td>0.553333</td>
      <td>-1.282963</td>
      <td>0.705921</td>
      <td>0.922303</td>
    </tr>
    <tr>
      <th>147</th>
      <td>0.795669</td>
      <td>-0.131979</td>
      <td>0.819596</td>
      <td>1.053935</td>
    </tr>
    <tr>
      <th>148</th>
      <td>0.432165</td>
      <td>0.788808</td>
      <td>0.933271</td>
      <td>1.448832</td>
    </tr>
    <tr>
      <th>149</th>
      <td>0.068662</td>
      <td>-0.131979</td>
      <td>0.762758</td>
      <td>0.790671</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 4 columns</p>
</div>



## from sklearn.preprocessing import MinMaxScaler: minmax 정규화 스케일링
- 0~양수값: 0~ 1번위 안으로 매핑
- 음수 양수 값: -1~1 사이의 값으로 매핑


```python
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(iris_df)
iris_mcaled=scaler.transform(iris_df)
iris_mcaled_df=pd.DataFrame(data=iris_mcaled, columns=iris.feature_names)
iris_mcaled_df
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
      <th>sepal length (cm)</th>
      <th>sepal width (cm)</th>
      <th>petal length (cm)</th>
      <th>petal width (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.222222</td>
      <td>0.625000</td>
      <td>0.067797</td>
      <td>0.041667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.166667</td>
      <td>0.416667</td>
      <td>0.067797</td>
      <td>0.041667</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.111111</td>
      <td>0.500000</td>
      <td>0.050847</td>
      <td>0.041667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.083333</td>
      <td>0.458333</td>
      <td>0.084746</td>
      <td>0.041667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.194444</td>
      <td>0.666667</td>
      <td>0.067797</td>
      <td>0.041667</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>0.666667</td>
      <td>0.416667</td>
      <td>0.711864</td>
      <td>0.916667</td>
    </tr>
    <tr>
      <th>146</th>
      <td>0.555556</td>
      <td>0.208333</td>
      <td>0.677966</td>
      <td>0.750000</td>
    </tr>
    <tr>
      <th>147</th>
      <td>0.611111</td>
      <td>0.416667</td>
      <td>0.711864</td>
      <td>0.791667</td>
    </tr>
    <tr>
      <th>148</th>
      <td>0.527778</td>
      <td>0.583333</td>
      <td>0.745763</td>
      <td>0.916667</td>
    </tr>
    <tr>
      <th>149</th>
      <td>0.444444</td>
      <td>0.416667</td>
      <td>0.694915</td>
      <td>0.708333</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 4 columns</p>
</div>



로그 스케일링: np.log


```python
log_scaled_data = np.log(iris_df)
```


```python
iris_log_scaled=pd.DataFrame(data=log_scaled_data, columns=iris.feature_names)
```


```python
iris_log_scaled
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
      <th>sepal length (cm)</th>
      <th>sepal width (cm)</th>
      <th>petal length (cm)</th>
      <th>petal width (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.629241</td>
      <td>1.252763</td>
      <td>0.336472</td>
      <td>-1.609438</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.589235</td>
      <td>1.098612</td>
      <td>0.336472</td>
      <td>-1.609438</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.547563</td>
      <td>1.163151</td>
      <td>0.262364</td>
      <td>-1.609438</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.526056</td>
      <td>1.131402</td>
      <td>0.405465</td>
      <td>-1.609438</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.609438</td>
      <td>1.280934</td>
      <td>0.336472</td>
      <td>-1.609438</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>1.902108</td>
      <td>1.098612</td>
      <td>1.648659</td>
      <td>0.832909</td>
    </tr>
    <tr>
      <th>146</th>
      <td>1.840550</td>
      <td>0.916291</td>
      <td>1.609438</td>
      <td>0.641854</td>
    </tr>
    <tr>
      <th>147</th>
      <td>1.871802</td>
      <td>1.098612</td>
      <td>1.648659</td>
      <td>0.693147</td>
    </tr>
    <tr>
      <th>148</th>
      <td>1.824549</td>
      <td>1.223775</td>
      <td>1.686399</td>
      <td>0.832909</td>
    </tr>
    <tr>
      <th>149</th>
      <td>1.774952</td>
      <td>1.098612</td>
      <td>1.629241</td>
      <td>0.587787</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 4 columns</p>
</div>



## 스케일러들의 장 단점
-  로그 스케일러 
    - 데이터의 값에 로그 함수를 적용하여 변환함. 양수에만 적용이 가능
    - 장점: 
        - 데이터의 분포를 정규분포에 가깝게 만들어 왜곡을 줄임
    - 단점:
        - 데이터에 0 또는 음수가 존재하면 로그 변환이 적용이 안됨
        - 데이터가 너무 작으면 로그 변환시에 무의미한 값이 나옴
        - 데이터의 왜곡 정도에 따라 성능 향상을 보장할 수 없음.
        - 큰 범위의 값들을 좁은 범위로 압축하여 모델 학습을 도움
    - 적용 대상: 데이터가 왜곡되어 있거나 큰 범위의 값이 존재할때 유용. 특히 특성 간 스케일이 차이가 나는 경우에 쓰임. 데이터의 분포가 급격하게 증가하는 경우에 유용
- min-max 스케일링
    - 데이터의 값을 최소갑과 최대값 사이의 범위로 변환함
    - 장점: 
        - 모든 특성을 동일 범위로 매핑하여 모델이 특성의 크기에 영향을 받지 않도록 함.
        - 이상치에 강건함
     - 단점:
         - 이상치가 있는 경우네느 전체 데이터의 범위가 넓어지므로, 스케일링이 제대로 이루어지지 않을수 있음
         - 데이터의 분포가 균일하지 않을 경우에는 스케일링이 올바르게 이루어지지 않음.
    - 적용 대상: 대부분의 데이터에 적용이 가능하나, 특히 이상치가 많은 경우에 유용. 특성의 크기가 중요하지 않는 경우에 사용됨. 이상치에 영향을 받을 가능성이 있는 경우
- 표준화 스케일링:
    - 특징: 데이터의 평균과 표준편차를 사용하여 변환
    - 장점:
        - 정규분포화를 하여 왜곡을 줄임
        - 이상치에 영향을 덜 받음.
     - 단점:
         - 이상치에 영향을 덜 받지만 여전히 영향 존재
         - 데이터 값의 범위 제한이 없기에 특정한 값에 데이터가 편중될 수 있음
         - 정규성이 보장되지 않으면 스케일링이 잘 이루어지지 않음.
     - 대부분의 데이터에 적용이 가능하며, 특히 데이터가 정규분포를 따르는 경우에 유용함. 


```python

```
