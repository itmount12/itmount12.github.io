```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
datas=pd.read_csv('시도별_1인_취업가구_20240221175115.csv',encoding='euc-kr')
```


```python
datas.columns
```




    Index(['시점', '시도별', '1인가구', '취업가구 (천가구)', '비율 (%)'], dtype='object')




```python
# 항목이 142 행으로 되어 있는데 2015~2022년 사이의 연도는 8개, 시도는 17개인데, 2017년부터 세종시가 추가되어서
(17*2)+(18*6)
```




    142




```python
sejong={'시점':[2015], '시도별': ['세종특별자치시'], '1인가구':[0], '취업가구 (천가구)': [0], '비율 (%)': [0.0]}
sejong1={'시점': [2016], '시도별': ['세종특별자치시'], '1인가구': [0], '취업가구 (천가구)': [0], '비율 (%)': [0.0]}
```


```python
sdf=pd.DataFrame(sejong)
sdf1=pd.DataFrame(sejong1)
dfs
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
      <th>시점</th>
      <th>시도별</th>
      <th>1인가구</th>
      <th>취업가구 (천가구)</th>
      <th>비율 (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>세종특별자치시</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>세종특별자치시</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data=pd.concat([datas,dfs])
```


```python
data=data.sort_values(['시점','시도별'],ascending=[True,True]).reset_index(drop=True)
```


```python
data.to_csv('test.csv')
```


```python
for x in range(2,4):
    data.iloc[:,x]=data.iloc[:,x]*1000
```


```python
data.rename(columns={'취업가구 (천가구)':'취업가구'},inplace=True)
```


```python
data['실업률']=100-data['비율 (%)']
```


```python
data.columns
```




    Index(['시점', '시도별', '1인가구', '취업가구', '비율 (%)', '실업률'], dtype='object')




```python
data=data.drop('비율 (%)',axis=1)
```


```python
emplom=data.iloc[:,[3,4]]
```


```python
data
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
      <th>시점</th>
      <th>시도별</th>
      <th>1인가구</th>
      <th>취업가구</th>
      <th>실업률</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>강원도</td>
      <td>190000</td>
      <td>110000</td>
      <td>41.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>경기도</td>
      <td>1024000</td>
      <td>654000</td>
      <td>36.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>경상남도</td>
      <td>346000</td>
      <td>210000</td>
      <td>39.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>경상북도</td>
      <td>324000</td>
      <td>191000</td>
      <td>40.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>광주광역시</td>
      <td>162000</td>
      <td>95000</td>
      <td>41.2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>139</th>
      <td>2022</td>
      <td>전라남도</td>
      <td>275000</td>
      <td>176000</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>140</th>
      <td>2022</td>
      <td>전라북도</td>
      <td>276000</td>
      <td>160000</td>
      <td>42.2</td>
    </tr>
    <tr>
      <th>141</th>
      <td>2022</td>
      <td>제주특별자치도</td>
      <td>90000</td>
      <td>63000</td>
      <td>30.1</td>
    </tr>
    <tr>
      <th>142</th>
      <td>2022</td>
      <td>충청남도</td>
      <td>333000</td>
      <td>217000</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>143</th>
      <td>2022</td>
      <td>충청북도</td>
      <td>256000</td>
      <td>164000</td>
      <td>36.1</td>
    </tr>
  </tbody>
</table>
<p>144 rows × 5 columns</p>
</div>



거주형태별


```python
house=pd.read_csv('성_및_거처의_종류별_1인가구__시군구_20240222112154.csv',encoding='euc-kr')
```


```python
house=house.iloc[1:,]
```


```python
house.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 144 entries, 1 to 144
    Data columns (total 10 columns):
     #   Column         Non-Null Count  Dtype 
    ---  ------         --------------  ----- 
     0   시점             144 non-null    object
     1   행정구역별(시군구)     144 non-null    object
     2   1인가구           144 non-null    object
     3   주택_계           144 non-null    object
     4   주택_단독주택        144 non-null    object
     5   주택_아파트         144 non-null    object
     6   주택_연립주택        144 non-null    object
     7   주택_다세대주택       144 non-null    object
     8   주택_비거주용건물내 주택  144 non-null    object
     9   주택이외의 거처_계     144 non-null    object
    dtypes: object(10)
    memory usage: 11.4+ KB
    


```python
house=house.sort_values(['시점','행정구역별(시군구)'])
```

결측치 방지


```python
house=house.reset_index(drop=True)
```


```python
total=pd.concat([house,emplom],axis=1)
```


```python
total
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
      <th>시점</th>
      <th>행정구역별(시군구)</th>
      <th>1인가구</th>
      <th>주택_계</th>
      <th>주택_단독주택</th>
      <th>주택_아파트</th>
      <th>주택_연립주택</th>
      <th>주택_다세대주택</th>
      <th>주택_비거주용건물내 주택</th>
      <th>주택이외의 거처_계</th>
      <th>취업가구</th>
      <th>실업률</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>강원도</td>
      <td>189379</td>
      <td>180487</td>
      <td>114432</td>
      <td>55195</td>
      <td>4577</td>
      <td>2568</td>
      <td>3715</td>
      <td>8892</td>
      <td>110000</td>
      <td>41.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>경기도</td>
      <td>1026471</td>
      <td>924234</td>
      <td>458026</td>
      <td>315160</td>
      <td>19353</td>
      <td>110989</td>
      <td>20706</td>
      <td>102237</td>
      <td>654000</td>
      <td>36.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>경상남도</td>
      <td>346754</td>
      <td>324922</td>
      <td>219093</td>
      <td>87907</td>
      <td>4657</td>
      <td>7134</td>
      <td>6131</td>
      <td>21832</td>
      <td>210000</td>
      <td>39.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>경상북도</td>
      <td>322569</td>
      <td>307476</td>
      <td>218334</td>
      <td>69564</td>
      <td>5490</td>
      <td>8771</td>
      <td>5317</td>
      <td>15093</td>
      <td>191000</td>
      <td>40.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>광주광역시</td>
      <td>163577</td>
      <td>153847</td>
      <td>79638</td>
      <td>66304</td>
      <td>1906</td>
      <td>3634</td>
      <td>2365</td>
      <td>9730</td>
      <td>95000</td>
      <td>41.2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>139</th>
      <td>2022</td>
      <td>전라남도</td>
      <td>283429</td>
      <td>264474</td>
      <td>163557</td>
      <td>88818</td>
      <td>4603</td>
      <td>3226</td>
      <td>4270</td>
      <td>18955</td>
      <td>176000</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>140</th>
      <td>2022</td>
      <td>전라북도</td>
      <td>284613</td>
      <td>271896</td>
      <td>152778</td>
      <td>104661</td>
      <td>5298</td>
      <td>5670</td>
      <td>3489</td>
      <td>12717</td>
      <td>160000</td>
      <td>42.2</td>
    </tr>
    <tr>
      <th>141</th>
      <td>2022</td>
      <td>제주특별자치도</td>
      <td>92172</td>
      <td>79247</td>
      <td>42942</td>
      <td>18831</td>
      <td>6593</td>
      <td>8610</td>
      <td>2271</td>
      <td>12925</td>
      <td>63000</td>
      <td>30.1</td>
    </tr>
    <tr>
      <th>142</th>
      <td>2022</td>
      <td>충청남도</td>
      <td>340741</td>
      <td>316102</td>
      <td>176029</td>
      <td>116881</td>
      <td>6364</td>
      <td>12485</td>
      <td>4343</td>
      <td>24639</td>
      <td>217000</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>143</th>
      <td>2022</td>
      <td>충청북도</td>
      <td>260948</td>
      <td>246828</td>
      <td>134174</td>
      <td>98953</td>
      <td>4428</td>
      <td>5692</td>
      <td>3581</td>
      <td>14120</td>
      <td>164000</td>
      <td>36.1</td>
    </tr>
  </tbody>
</table>
<p>144 rows × 12 columns</p>
</div>




```python
total.iloc[:,2:10]=total.iloc[:,2:10].astype(int)
```

성별


```python
gender=pd.read_csv('gender.csv',encoding='euc-kr')
```


```python
gender=gender.sort_values(['시점','행정구역별(시군구)']).reset_index(drop=True)
```


```python
gender=gender.iloc[:-1,2:4]
```


```python
gender
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
      <th>남자</th>
      <th>여자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>96820</td>
      <td>92559</td>
    </tr>
    <tr>
      <th>1</th>
      <td>556495</td>
      <td>469976</td>
    </tr>
    <tr>
      <th>2</th>
      <td>167463</td>
      <td>179291</td>
    </tr>
    <tr>
      <th>3</th>
      <td>149660</td>
      <td>172909</td>
    </tr>
    <tr>
      <th>4</th>
      <td>83271</td>
      <td>80306</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>139</th>
      <td>134739</td>
      <td>148690</td>
    </tr>
    <tr>
      <th>140</th>
      <td>137085</td>
      <td>147528</td>
    </tr>
    <tr>
      <th>141</th>
      <td>46304</td>
      <td>45868</td>
    </tr>
    <tr>
      <th>142</th>
      <td>181544</td>
      <td>159197</td>
    </tr>
    <tr>
      <th>143</th>
      <td>136768</td>
      <td>124180</td>
    </tr>
  </tbody>
</table>
<p>144 rows × 2 columns</p>
</div>




```python
total
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
      <th>시점</th>
      <th>행정구역별(시군구)</th>
      <th>1인가구</th>
      <th>주택_계</th>
      <th>주택_단독주택</th>
      <th>주택_아파트</th>
      <th>주택_연립주택</th>
      <th>주택_다세대주택</th>
      <th>주택_비거주용건물내 주택</th>
      <th>주택이외의 거처_계</th>
      <th>취업가구</th>
      <th>실업률</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>강원도</td>
      <td>189379</td>
      <td>180487</td>
      <td>114432</td>
      <td>55195</td>
      <td>4577</td>
      <td>2568</td>
      <td>3715</td>
      <td>8892</td>
      <td>110000</td>
      <td>41.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>경기도</td>
      <td>1026471</td>
      <td>924234</td>
      <td>458026</td>
      <td>315160</td>
      <td>19353</td>
      <td>110989</td>
      <td>20706</td>
      <td>102237</td>
      <td>654000</td>
      <td>36.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>경상남도</td>
      <td>346754</td>
      <td>324922</td>
      <td>219093</td>
      <td>87907</td>
      <td>4657</td>
      <td>7134</td>
      <td>6131</td>
      <td>21832</td>
      <td>210000</td>
      <td>39.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>경상북도</td>
      <td>322569</td>
      <td>307476</td>
      <td>218334</td>
      <td>69564</td>
      <td>5490</td>
      <td>8771</td>
      <td>5317</td>
      <td>15093</td>
      <td>191000</td>
      <td>40.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>광주광역시</td>
      <td>163577</td>
      <td>153847</td>
      <td>79638</td>
      <td>66304</td>
      <td>1906</td>
      <td>3634</td>
      <td>2365</td>
      <td>9730</td>
      <td>95000</td>
      <td>41.2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>139</th>
      <td>2022</td>
      <td>전라남도</td>
      <td>283429</td>
      <td>264474</td>
      <td>163557</td>
      <td>88818</td>
      <td>4603</td>
      <td>3226</td>
      <td>4270</td>
      <td>18955</td>
      <td>176000</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>140</th>
      <td>2022</td>
      <td>전라북도</td>
      <td>284613</td>
      <td>271896</td>
      <td>152778</td>
      <td>104661</td>
      <td>5298</td>
      <td>5670</td>
      <td>3489</td>
      <td>12717</td>
      <td>160000</td>
      <td>42.2</td>
    </tr>
    <tr>
      <th>141</th>
      <td>2022</td>
      <td>제주특별자치도</td>
      <td>92172</td>
      <td>79247</td>
      <td>42942</td>
      <td>18831</td>
      <td>6593</td>
      <td>8610</td>
      <td>2271</td>
      <td>12925</td>
      <td>63000</td>
      <td>30.1</td>
    </tr>
    <tr>
      <th>142</th>
      <td>2022</td>
      <td>충청남도</td>
      <td>340741</td>
      <td>316102</td>
      <td>176029</td>
      <td>116881</td>
      <td>6364</td>
      <td>12485</td>
      <td>4343</td>
      <td>24639</td>
      <td>217000</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>143</th>
      <td>2022</td>
      <td>충청북도</td>
      <td>260948</td>
      <td>246828</td>
      <td>134174</td>
      <td>98953</td>
      <td>4428</td>
      <td>5692</td>
      <td>3581</td>
      <td>14120</td>
      <td>164000</td>
      <td>36.1</td>
    </tr>
  </tbody>
</table>
<p>144 rows × 12 columns</p>
</div>




```python
result = pd.concat([total, gender],axis=1)
```


```python
result=pd.concat([total.iloc[:,:3],gender,total.iloc[:,3:]],axis=1)
```


```python
result.rename(columns={'행정구역별(시군구)':'시도'},inplace=True)
```


```python
result.to_csv('1인가구 통계량: 성별,취업률,주거형태.csv')
```


```python

```
