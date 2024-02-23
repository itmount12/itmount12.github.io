```python
import pandas as pd
import numpy as np
```


```python
ages=pd.read_csv('성_및_연령별_1인가구__시군구_20240222123109.csv',encoding='euc-kr')
```

보이는 바와같이 나이 대 구분이 5살 단위로 되어 있어 이를 10세 기준으로 통합하고자 한다.


```python
ages
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
      <th>합계</th>
      <th>20세 미만</th>
      <th>20~24</th>
      <th>25~29</th>
      <th>30~34</th>
      <th>35~39</th>
      <th>40~44</th>
      <th>45~49</th>
      <th>50~54</th>
      <th>55~59</th>
      <th>60~64</th>
      <th>65~69</th>
      <th>70~74</th>
      <th>75~79</th>
      <th>80~84</th>
      <th>85세 이상</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>시점</td>
      <td>행정구역별(시군구)</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
      <td>1인가구</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>전국</td>
      <td>5203440</td>
      <td>58020</td>
      <td>367152</td>
      <td>519871</td>
      <td>533193</td>
      <td>420129</td>
      <td>428605</td>
      <td>421153</td>
      <td>430941</td>
      <td>446608</td>
      <td>354599</td>
      <td>313584</td>
      <td>308780</td>
      <td>288138</td>
      <td>197240</td>
      <td>115427</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>서울특별시</td>
      <td>1115744</td>
      <td>13721</td>
      <td>93068</td>
      <td>165410</td>
      <td>157667</td>
      <td>105540</td>
      <td>94750</td>
      <td>82138</td>
      <td>77390</td>
      <td>77679</td>
      <td>62250</td>
      <td>56374</td>
      <td>50095</td>
      <td>39946</td>
      <td>24674</td>
      <td>15042</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>부산광역시</td>
      <td>361749</td>
      <td>4850</td>
      <td>29487</td>
      <td>29500</td>
      <td>27535</td>
      <td>22796</td>
      <td>25034</td>
      <td>26775</td>
      <td>29567</td>
      <td>36492</td>
      <td>32662</td>
      <td>28529</td>
      <td>25997</td>
      <td>22059</td>
      <td>13465</td>
      <td>7001</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>대구광역시</td>
      <td>239517</td>
      <td>3080</td>
      <td>18000</td>
      <td>20032</td>
      <td>20640</td>
      <td>17533</td>
      <td>19866</td>
      <td>20549</td>
      <td>21342</td>
      <td>22189</td>
      <td>18563</td>
      <td>15920</td>
      <td>15048</td>
      <td>13623</td>
      <td>8756</td>
      <td>4376</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>140</th>
      <td>2022</td>
      <td>전라북도</td>
      <td>284613</td>
      <td>2582</td>
      <td>20185</td>
      <td>24560</td>
      <td>19422</td>
      <td>14203</td>
      <td>14931</td>
      <td>17249</td>
      <td>21343</td>
      <td>23030</td>
      <td>27267</td>
      <td>23628</td>
      <td>20877</td>
      <td>18701</td>
      <td>20140</td>
      <td>16495</td>
    </tr>
    <tr>
      <th>141</th>
      <td>2022</td>
      <td>전라남도</td>
      <td>283429</td>
      <td>1242</td>
      <td>9920</td>
      <td>19095</td>
      <td>16104</td>
      <td>12792</td>
      <td>14330</td>
      <td>16507</td>
      <td>21984</td>
      <td>24936</td>
      <td>29188</td>
      <td>24882</td>
      <td>23156</td>
      <td>22904</td>
      <td>25935</td>
      <td>20454</td>
    </tr>
    <tr>
      <th>142</th>
      <td>2022</td>
      <td>경상북도</td>
      <td>430969</td>
      <td>3364</td>
      <td>26795</td>
      <td>34709</td>
      <td>29109</td>
      <td>22365</td>
      <td>23684</td>
      <td>25743</td>
      <td>32391</td>
      <td>36095</td>
      <td>44054</td>
      <td>38648</td>
      <td>32753</td>
      <td>26988</td>
      <td>30208</td>
      <td>24063</td>
    </tr>
    <tr>
      <th>143</th>
      <td>2022</td>
      <td>경상남도</td>
      <td>468772</td>
      <td>2219</td>
      <td>19214</td>
      <td>35458</td>
      <td>33319</td>
      <td>26532</td>
      <td>29924</td>
      <td>31846</td>
      <td>40628</td>
      <td>41958</td>
      <td>51453</td>
      <td>44261</td>
      <td>34365</td>
      <td>27971</td>
      <td>28044</td>
      <td>21580</td>
    </tr>
    <tr>
      <th>144</th>
      <td>2022</td>
      <td>제주특별자치도</td>
      <td>92172</td>
      <td>503</td>
      <td>3870</td>
      <td>8427</td>
      <td>7503</td>
      <td>6435</td>
      <td>7391</td>
      <td>7987</td>
      <td>9827</td>
      <td>9084</td>
      <td>8981</td>
      <td>7030</td>
      <td>4796</td>
      <td>3811</td>
      <td>3406</td>
      <td>3121</td>
    </tr>
  </tbody>
</table>
<p>145 rows × 18 columns</p>
</div>




```python
ages=ages.iloc[1:,] #불필요한 행제거
```


```python
ages=ages.sort_values(['시점','행정구역별(시군구)']).reset_index(drop=True)
```

ages 의 열을 확인해보면


```python
ages
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
      <th>합계</th>
      <th>20세 미만</th>
      <th>20~24</th>
      <th>25~29</th>
      <th>30~34</th>
      <th>35~39</th>
      <th>40~44</th>
      <th>45~49</th>
      <th>50~54</th>
      <th>55~59</th>
      <th>60~64</th>
      <th>65~69</th>
      <th>70~74</th>
      <th>75~79</th>
      <th>80~84</th>
      <th>85세 이상</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015</td>
      <td>강원도</td>
      <td>189379</td>
      <td>2293</td>
      <td>20467</td>
      <td>16088</td>
      <td>11473</td>
      <td>9986</td>
      <td>11833</td>
      <td>14080</td>
      <td>16724</td>
      <td>18944</td>
      <td>14821</td>
      <td>12591</td>
      <td>13894</td>
      <td>12795</td>
      <td>8109</td>
      <td>5281</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015</td>
      <td>경기도</td>
      <td>1026471</td>
      <td>7616</td>
      <td>50199</td>
      <td>99362</td>
      <td>118409</td>
      <td>100540</td>
      <td>103995</td>
      <td>98661</td>
      <td>95158</td>
      <td>90935</td>
      <td>66537</td>
      <td>55634</td>
      <td>51266</td>
      <td>44190</td>
      <td>27890</td>
      <td>16079</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015</td>
      <td>경상남도</td>
      <td>346754</td>
      <td>2463</td>
      <td>15076</td>
      <td>24195</td>
      <td>29008</td>
      <td>25385</td>
      <td>27116</td>
      <td>28584</td>
      <td>30764</td>
      <td>32836</td>
      <td>27086</td>
      <td>23688</td>
      <td>24818</td>
      <td>25862</td>
      <td>19050</td>
      <td>10823</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015</td>
      <td>경상북도</td>
      <td>322569</td>
      <td>3154</td>
      <td>21838</td>
      <td>24610</td>
      <td>24630</td>
      <td>19478</td>
      <td>21023</td>
      <td>22592</td>
      <td>25696</td>
      <td>28218</td>
      <td>24153</td>
      <td>22026</td>
      <td>25070</td>
      <td>27513</td>
      <td>20351</td>
      <td>12217</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015</td>
      <td>광주광역시</td>
      <td>163577</td>
      <td>2109</td>
      <td>14244</td>
      <td>18293</td>
      <td>19161</td>
      <td>14968</td>
      <td>14558</td>
      <td>13796</td>
      <td>12907</td>
      <td>12956</td>
      <td>9585</td>
      <td>8568</td>
      <td>8046</td>
      <td>7060</td>
      <td>4546</td>
      <td>2780</td>
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
      <td>1242</td>
      <td>9920</td>
      <td>19095</td>
      <td>16104</td>
      <td>12792</td>
      <td>14330</td>
      <td>16507</td>
      <td>21984</td>
      <td>24936</td>
      <td>29188</td>
      <td>24882</td>
      <td>23156</td>
      <td>22904</td>
      <td>25935</td>
      <td>20454</td>
    </tr>
    <tr>
      <th>140</th>
      <td>2022</td>
      <td>전라북도</td>
      <td>284613</td>
      <td>2582</td>
      <td>20185</td>
      <td>24560</td>
      <td>19422</td>
      <td>14203</td>
      <td>14931</td>
      <td>17249</td>
      <td>21343</td>
      <td>23030</td>
      <td>27267</td>
      <td>23628</td>
      <td>20877</td>
      <td>18701</td>
      <td>20140</td>
      <td>16495</td>
    </tr>
    <tr>
      <th>141</th>
      <td>2022</td>
      <td>제주특별자치도</td>
      <td>92172</td>
      <td>503</td>
      <td>3870</td>
      <td>8427</td>
      <td>7503</td>
      <td>6435</td>
      <td>7391</td>
      <td>7987</td>
      <td>9827</td>
      <td>9084</td>
      <td>8981</td>
      <td>7030</td>
      <td>4796</td>
      <td>3811</td>
      <td>3406</td>
      <td>3121</td>
    </tr>
    <tr>
      <th>142</th>
      <td>2022</td>
      <td>충청남도</td>
      <td>340741</td>
      <td>3409</td>
      <td>23999</td>
      <td>34523</td>
      <td>29871</td>
      <td>22277</td>
      <td>21353</td>
      <td>21465</td>
      <td>25668</td>
      <td>27101</td>
      <td>31877</td>
      <td>25653</td>
      <td>20590</td>
      <td>17599</td>
      <td>18880</td>
      <td>16476</td>
    </tr>
    <tr>
      <th>143</th>
      <td>2022</td>
      <td>충청북도</td>
      <td>260948</td>
      <td>1947</td>
      <td>17565</td>
      <td>29960</td>
      <td>23588</td>
      <td>15742</td>
      <td>15163</td>
      <td>15880</td>
      <td>20140</td>
      <td>21806</td>
      <td>25782</td>
      <td>20951</td>
      <td>14792</td>
      <td>13375</td>
      <td>13665</td>
      <td>10592</td>
    </tr>
  </tbody>
</table>
<p>144 rows × 18 columns</p>
</div>




```python
ages.shape
```




    (144, 18)



0열부터 2열은 지역 구분이므로, 3열부터 18열까지 두 열씩 합쳐 보도록한다.

여기서 20대 미만은 열이 하나이므로 제외한다.


```python
age_label=[f'{x*5}대' for x in range(4,18,2)]
```


```python
age_label
```




    ['20대', '30대', '40대', '50대', '60대', '70대', '80대']




```python
ages.iloc[:,2:]=ages.iloc[:,2:].astype(int)
```


```python
new_ages = pd.DataFrame()
for x, label in zip(range(4, 18,2), age_label):
    new_ages[f'{label}'] = ages.iloc[:, x].values + ages.iloc[:, x + 1].values
```

여기에 10대를 추가하고, 80대를 80세 이상으로 바꿔준다.


```python
new_ages['10대']=ages.iloc[:,3]
```


```python
new_ages.rename(columns={'80대':'80대 이상~'},inplace=True)
```


```python
new_ages=pd.concat([new_ages.iloc[:,-1],new_ages.iloc[:,:-1]],axis=1)
```


```python
new_ages
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
      <th>10대</th>
      <th>20대</th>
      <th>30대</th>
      <th>40대</th>
      <th>50대</th>
      <th>60대</th>
      <th>70대</th>
      <th>80대 이상~</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2293</td>
      <td>36555</td>
      <td>21459</td>
      <td>25913</td>
      <td>35668</td>
      <td>27412</td>
      <td>26689</td>
      <td>13390</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7616</td>
      <td>149561</td>
      <td>218949</td>
      <td>202656</td>
      <td>186093</td>
      <td>122171</td>
      <td>95456</td>
      <td>43969</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2463</td>
      <td>39271</td>
      <td>54393</td>
      <td>55700</td>
      <td>63600</td>
      <td>50774</td>
      <td>50680</td>
      <td>29873</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3154</td>
      <td>46448</td>
      <td>44108</td>
      <td>43615</td>
      <td>53914</td>
      <td>46179</td>
      <td>52583</td>
      <td>32568</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2109</td>
      <td>32537</td>
      <td>34129</td>
      <td>28354</td>
      <td>25863</td>
      <td>18153</td>
      <td>15106</td>
      <td>7326</td>
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
    </tr>
    <tr>
      <th>139</th>
      <td>1242</td>
      <td>29015</td>
      <td>28896</td>
      <td>30837</td>
      <td>46920</td>
      <td>54070</td>
      <td>46060</td>
      <td>46389</td>
    </tr>
    <tr>
      <th>140</th>
      <td>2582</td>
      <td>44745</td>
      <td>33625</td>
      <td>32180</td>
      <td>44373</td>
      <td>50895</td>
      <td>39578</td>
      <td>36635</td>
    </tr>
    <tr>
      <th>141</th>
      <td>503</td>
      <td>12297</td>
      <td>13938</td>
      <td>15378</td>
      <td>18911</td>
      <td>16011</td>
      <td>8607</td>
      <td>6527</td>
    </tr>
    <tr>
      <th>142</th>
      <td>3409</td>
      <td>58522</td>
      <td>52148</td>
      <td>42818</td>
      <td>52769</td>
      <td>57530</td>
      <td>38189</td>
      <td>35356</td>
    </tr>
    <tr>
      <th>143</th>
      <td>1947</td>
      <td>47525</td>
      <td>39330</td>
      <td>31043</td>
      <td>41946</td>
      <td>46733</td>
      <td>28167</td>
      <td>24257</td>
    </tr>
  </tbody>
</table>
<p>144 rows × 8 columns</p>
</div>




```python
old= pd.read_csv('1인가구 통계.csv')
```


```python
old=old.drop('Unnamed: 0',axis=1)
```


```python
total=pd.concat([old,new_ages],axis=1)
```


```python
total.to_excel('통합데이터.xlsx',index=False) #파일 생성시 불필요 인덱스 생성 방지
```

전체인구


```python
allp=pd.read_csv('성_및_연령별_추계인구_1세별__5세별__시도_20240222133036.csv',encoding='euc-kr')
```


```python
allp=allp.iloc[:,1:]
```


```python
allp=allp.sort_values(['시점','시도별(1)']).reset_index(drop=True)
```


```python
total['전체인구']=allp['데이터']
```


```python
concated=pd.concat([total.iloc[:,:3],total['전체인구'],total.iloc[:,3:]],axis=1)
```


```python
concated=concated.iloc[:,:-1]
```


```python
concated['1인가구']
```




    0       189379
    1      1026471
    2       346754
    3       322569
    4       163577
            ...   
    139     283429
    140     284613
    141      92172
    142     340741
    143     260948
    Name: 1인가구, Length: 144, dtype: int64




```python
concated.to_excel('1인가구 통합통계표.xlsx',index=False)
```

전국통계


```python
nationwide=concated[concated['시도']=='전국']
```


```python
xlabel=[x for x in range(2015,2023)]
```


```python
nationwide['1인가구']
```




    12     5203440
    30     5397615
    48     5618677
    66     5848594
    84     6147516
    102    6643354
    120    7165788
    138    7502350
    Name: 1인가구, dtype: int64




```python
import matplotlib.pyplot as plt
```


```python
nationwide.isna().sum()
```




    시점               0
    시도               0
    1인가구             0
    전체인구             0
    남자               0
    여자               0
    주택_계             0
    주택_단독주택          0
    주택_아파트           0
    주택_연립주택          0
    주택_다세대주택         0
    주택_비거주용건물내 주택    0
    주택이외의 거처_계       0
    취업가구             0
    실업률              0
    10대              0
    20대              0
    30대              0
    40대              0
    50대              0
    60대              0
    70대              0
    80대 이상~          0
    dtype: int64




```python
nationwide.reset_index(True)
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
      <th>시도</th>
      <th>1인가구</th>
      <th>전체인구</th>
      <th>남자</th>
      <th>여자</th>
      <th>주택_계</th>
      <th>주택_단독주택</th>
      <th>주택_아파트</th>
      <th>주택_연립주택</th>
      <th>...</th>
      <th>취업가구</th>
      <th>실업률</th>
      <th>10대</th>
      <th>20대</th>
      <th>30대</th>
      <th>40대</th>
      <th>50대</th>
      <th>60대</th>
      <th>70대</th>
      <th>80대 이상~</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td>2015</td>
      <td>전국</td>
      <td>5203440</td>
      <td>51014947</td>
      <td>2592963</td>
      <td>2610477</td>
      <td>4783231</td>
      <td>2710775</td>
      <td>1433666</td>
      <td>85109</td>
      <td>...</td>
      <td>3139000</td>
      <td>39.6</td>
      <td>58020</td>
      <td>887023</td>
      <td>953322</td>
      <td>849758</td>
      <td>877549</td>
      <td>668183</td>
      <td>596918</td>
      <td>312667</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>전국</td>
      <td>5397615</td>
      <td>51217803</td>
      <td>2675861</td>
      <td>2721754</td>
      <td>4921788</td>
      <td>2742516</td>
      <td>1504073</td>
      <td>90023</td>
      <td>...</td>
      <td>3238000</td>
      <td>40.0</td>
      <td>62639</td>
      <td>929408</td>
      <td>948637</td>
      <td>843044</td>
      <td>911859</td>
      <td>743553</td>
      <td>615056</td>
      <td>343419</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2017</td>
      <td>전국</td>
      <td>5618677</td>
      <td>51361911</td>
      <td>2791849</td>
      <td>2826828</td>
      <td>5088437</td>
      <td>2765198</td>
      <td>1605878</td>
      <td>93832</td>
      <td>...</td>
      <td>3408000</td>
      <td>39.2</td>
      <td>61058</td>
      <td>961791</td>
      <td>968461</td>
      <td>862810</td>
      <td>947726</td>
      <td>805432</td>
      <td>643547</td>
      <td>367852</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2018</td>
      <td>전국</td>
      <td>5848594</td>
      <td>51585058</td>
      <td>2906320</td>
      <td>2942274</td>
      <td>5269889</td>
      <td>2762080</td>
      <td>1750760</td>
      <td>98323</td>
      <td>...</td>
      <td>3552000</td>
      <td>39.3</td>
      <td>58154</td>
      <td>1019944</td>
      <td>992737</td>
      <td>864221</td>
      <td>974444</td>
      <td>869904</td>
      <td>670897</td>
      <td>398293</td>
    </tr>
    <tr>
      <th>84</th>
      <td>2019</td>
      <td>전국</td>
      <td>6147516</td>
      <td>51764822</td>
      <td>3053733</td>
      <td>3093783</td>
      <td>5521438</td>
      <td>2789981</td>
      <td>1926935</td>
      <td>104497</td>
      <td>...</td>
      <td>3747000</td>
      <td>39.3</td>
      <td>59415</td>
      <td>1117581</td>
      <td>1035616</td>
      <td>871653</td>
      <td>999047</td>
      <td>932613</td>
      <td>696101</td>
      <td>435490</td>
    </tr>
    <tr>
      <th>102</th>
      <td>2020</td>
      <td>전국</td>
      <td>6643354</td>
      <td>51836239</td>
      <td>3304398</td>
      <td>3338956</td>
      <td>5920184</td>
      <td>2921200</td>
      <td>2124418</td>
      <td>114584</td>
      <td>...</td>
      <td>3972000</td>
      <td>40.0</td>
      <td>76202</td>
      <td>1266911</td>
      <td>1115518</td>
      <td>903816</td>
      <td>1039495</td>
      <td>1038985</td>
      <td>732715</td>
      <td>469712</td>
    </tr>
    <tr>
      <th>120</th>
      <td>2021</td>
      <td>전국</td>
      <td>7165788</td>
      <td>51744876</td>
      <td>3583770</td>
      <td>3582018</td>
      <td>6356409</td>
      <td>3024891</td>
      <td>2373162</td>
      <td>126862</td>
      <td>...</td>
      <td>4352000</td>
      <td>38.2</td>
      <td>54052</td>
      <td>1363552</td>
      <td>1226034</td>
      <td>950236</td>
      <td>1100914</td>
      <td>1176108</td>
      <td>771145</td>
      <td>523747</td>
    </tr>
    <tr>
      <th>138</th>
      <td>2022</td>
      <td>전국</td>
      <td>7502350</td>
      <td>51628117</td>
      <td>3751071</td>
      <td>3751279</td>
      <td>6640775</td>
      <td>3075767</td>
      <td>2553695</td>
      <td>134435</td>
      <td>...</td>
      <td>4555000</td>
      <td>36.9</td>
      <td>53088</td>
      <td>1386552</td>
      <td>1298846</td>
      <td>977577</td>
      <td>1137505</td>
      <td>1252607</td>
      <td>808984</td>
      <td>587191</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 23 columns</p>
</div>




```python

```


```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
fig.gca().ticklabel_format( useOffset=False, style='plain')
axs[0,0].bar(xlabel,nationwide['1인가구'].values,label='1인가구')
axs[0,0].bar(xlabel,nationwide['전체인구'],alpha=0.5,label='전체 인구')
axs[0,0].legend()
axs[0, 0].set_xlabel('연도')
axs[0, 0].set_ylabel('단위/천만명')
axs[0,0].set_title('1인가구 vs 전체 인구')

axs[0,1].bar(xlabel,nationwide['1인가구'].values,label='1인가구')
axs[0, 1].set_xlabel('연도')
axs[0, 1].set_ylabel('단위/백만명')
axs[0,1].set_title('1인가구 증가현황')

axs[1,0].plot(xlabel[1:],singlr,label='1인가구')
axs[1,0].plot(xlabel[1:],alglr,label='전체인구')
axs[1,0].set_xlabel('연도')
axs[1,0].axhline(y=np.mean(singlr),color='k',linestyle='--',label=f'1인가구 평균선:{round(np.mean(singlr),1)}')
axs[1,0].axhline(y=np.mean(singlr)+2*np.std(singlr),color='b',linestyle='-')
axs[1,0].axhline(y=np.mean(singlr)-2*np.std(singlr),color='b',linestyle='-')
axs[1,0].set_ylabel('단위:퍼센트')
axs[1,0].legend()
axs[1,0].grid()
axs[1,0].set_title('증감률')


axs[1,1].plot(xlabel,nationwide['전체인구'].values,'r^-',label='전체인구')
axs[1, 1].set_xlabel('연도')
axs[1, 1].set_ylabel('단위/천만명')
axs[1,1].set_title('전체인구 증가현황')
axs[1,1].axvspan(xlabel[4], xlabel[7], color='red', alpha=0.3, label='코로나 발생시기')
axs[1,1].legend()
plt.show()

```


    
![png](output_41_0.png)
    


# 증감률 계산


```python
def cgr(data): #반복가능한 객체
    grates = []
    for i in range(1, len(data)):
        rate = ((data[i] - data[i-1]) / data[i-1]) * 100
        grates.append(rate)
    return grates

```


```python
singlr=cgr(nationwide['1인가구'].values)
alglr=cgr(nationwide['전체인구'].values)
```


```python
np.mean(singlr)
```




    5.379528367482793




```python
singlr
```




    [3.73166597481666,
     4.095549608484488,
     4.092013119814504,
     5.1110061666102995,
     8.065664245526161,
     7.864009655363842,
     4.696789801763603]



연령별 인구


```python
pop=nationwide.iloc[:,-8:].reset_index(drop=True)
```


```python
year_title=[]
for x in range(2):
    for y in range(4):
        a=(x,y)
        year_title.append(a)
```


```python
year_title
```




    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]




```python
fig, axs = plt.subplots(nrows=2, ncols=4, figsize=(10, 10))
for i,(row,col) in enumerate(year_title):
    axs[row,col].pie(pop.iloc[i],autopct='%1.1f%%',labels=pop.columns)
    axs[row,col].set_title(f'{2015+i}년도')
fig.suptitle('연도별 1인가구 연령 분포 그래프') #fig= 도화지 전체 객체, suptitle-> 슈퍼타이틀: 대제목
# axs[0,1].pie(pop.iloc[1],autopct='%1.1f%%',labels=pop.columns)
# axs[0,1].set_title('2016년도')

# axs[0,2].pie(pop.iloc[2],autopct='%1.1f%%',labels=pop.columns)
# axs[0,2].set_title('2017년도')

# axs[0,3].pie(pop.iloc[3],autopct='%1.1f%%',labels=pop.columns)
# axs[0,3].set_title('2018년도')

# axs[1,0].pie(pop.iloc[4],autopct='%1.1f%%',labels=pop.columns)
# axs[1,0].set_title('2019년도')

# axs[1,1].pie(pop.iloc[5],autopct='%1.1f%%',labels=pop.columns)
# axs[1,1].set_title('2020년도')

# axs[(1,2)].pie(pop.iloc[6],autopct='%1.1f%%',labels=pop.columns)
# axs[1,2].set_title('2021년도')

# axs[1,3].pie(pop.iloc[7],autopct='%1.1f%%',labels=pop.columns)
# axs[1,3].set_title('2022년도')
```




    Text(0.5, 0.98, '연도별 1인가구 연령 분포 그래프')




    
![png](output_51_1.png)
    



```python
year_title=[]
for x in range(2):
    for y in range(4):
        a=(x,y)
        year_title.append(a)
```


```python
year_title
```




    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]



지역별 동향 파악


```python
detailed=concated[concated['시도']!='전국']
```


```python
first=detailed[detailed['시점']==2015]
one=detailed[detailed['시점']==2016]
second=detailed[detailed['시점']==2017]
two=detailed[detailed['시점']==2018]
third=detailed[detailed['시점']==2019]
three=detailed[detailed['시점']==2020]
fouth=detailed[detailed['시점']==2021]
four=detailed[detailed['시점']==2022]
```


```python
fig,axs=plt.subplots(2,1,figsize=(8,8))
axs[0].barh(first['시도'],first['1인가구'])
axs[0].barh(first['시도'],-one['1인가구'])
axs[0].ticklabel_format(axis='x', useOffset=False, style='plain') #plain 과학 표기 금지!
axs[0].set_title('2015년과 2016년 1인 가구 지역비교')

axs[1].barh(first['시도'],second['1인가구'])
axs[1].barh(first['시도'],-two['1인가구'])
axs[1].ticklabel_format(axis='x', useOffset=False, style='plain')
axs[1].set_title('2017년과 2018년 1인 가구 지역비교')

fig.suptitle('연도별 1인 가구 비교:코로나 전 시점')
```




    Text(0.5, 0.98, '연도별 1인 가구 비교:코로나 전 시점')




    
![png](output_57_1.png)
    



```python
fig,axs=plt.subplots(2,1,figsize=(8,8))
axs[0].barh(first['시도'],third['1인가구'])
axs[0].barh(first['시도'],-three['1인가구'])
axs[0].ticklabel_format(axis='x', useOffset=False, style='plain') #plain 과학 표기 금지!
axs[0].set_title('2019년과 2020년 1인 가구 지역비교')

axs[1].barh(first['시도'],fouth['1인가구'])
axs[1].barh(first['시도'],-four['1인가구'])
axs[1].ticklabel_format(axis='x', useOffset=False, style='plain')
axs[1].set_title('2020년과 2021년 1인 가구 지역비교')

fig.suptitle('연도별 1인 가구 비교:코로나 시점')
fig.set_facecolor('red')
```


    
![png](output_58_0.png)
    


details


```python
import seaborn as sns
```


```python
for x in range(2,8):
    sns.kdeplot(detailed[f'{x}0대'],label=f'{x}0대')
plt.legend()
plt.gca().ticklabel_format(axis='x', useOffset=False, style='plain')
plt.gca().ticklabel_format(axis='y', useOffset=False, style='plain')
```


    
![png](output_61_0.png)
    



```python
fig,axis=plt.subplots(1,2,figsize=(8,10),constrained_layout=True) #간격 조정
sns.kdeplot(detailed.groupby('시도')[['60대','70대','80대 이상~']].mean(),ax=axis[0])
sns.kdeplot(old_m,ax=axis[0],label='노인전체',color='silver')
axis[0].ticklabel_format(axis='x', useOffset=False, style='plain')
axis[0].ticklabel_format(axis='y', useOffset=False, style='plain')
axis[0].set_title('시도별 노인 1인가구 연령별 평균 분포')

sns.kdeplot(detailed.groupby('시도')[[f'{x}0대' for x in range(2,6)]].mean(),ax=axis[1])
sns.kdeplot(awork_mean,ax=axis[1],label='고용 인구 전체',color='gold')
axis[1].ticklabel_format(axis='x', useOffset=False, style='plain')
axis[1].ticklabel_format(axis='y', useOffset=False, style='plain')
axis[1].set_title('시도별 생산 가능 인구 연령별 평균 분포')

fig.suptitle('시도별 1인가구 평균 연령 분포:시점(2015~2022)')
```




    Text(0.5, 0.98, '시도별 1인가구 평균 연령 분포:시점(2015~2022)')




    
![png](output_62_1.png)
    



```python
old_guys=detailed.groupby('시도')[['60대','70대','80대 이상~']].mean()
```


```python
old_guys
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
      <th>60대</th>
      <th>70대</th>
      <th>80대 이상~</th>
    </tr>
    <tr>
      <th>시도</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강원도</th>
      <td>38601.875</td>
      <td>29599.375</td>
      <td>18987.5</td>
    </tr>
    <tr>
      <th>경기도</th>
      <td>185812.5</td>
      <td>120757.0</td>
      <td>66844.0</td>
    </tr>
    <tr>
      <th>경상남도</th>
      <td>71642.875</td>
      <td>55188.875</td>
      <td>38058.375</td>
    </tr>
    <tr>
      <th>경상북도</th>
      <td>63229.375</td>
      <td>54763.375</td>
      <td>42155.625</td>
    </tr>
    <tr>
      <th>광주광역시</th>
      <td>25096.25</td>
      <td>18114.25</td>
      <td>10202.125</td>
    </tr>
    <tr>
      <th>대구광역시</th>
      <td>48496.5</td>
      <td>34419.0</td>
      <td>19514.875</td>
    </tr>
    <tr>
      <th>대전광역시</th>
      <td>26171.375</td>
      <td>16817.125</td>
      <td>9672.375</td>
    </tr>
    <tr>
      <th>부산광역시</th>
      <td>80397.875</td>
      <td>58102.875</td>
      <td>28808.125</td>
    </tr>
    <tr>
      <th>서울특별시</th>
      <td>156244.875</td>
      <td>110359.25</td>
      <td>56694.125</td>
    </tr>
    <tr>
      <th>세종특별자치시</th>
      <td>3397.25</td>
      <td>2124.875</td>
      <td>1402.5</td>
    </tr>
    <tr>
      <th>울산광역시</th>
      <td>19649.75</td>
      <td>11101.25</td>
      <td>5256.0</td>
    </tr>
    <tr>
      <th>인천광역시</th>
      <td>48141.75</td>
      <td>30866.5</td>
      <td>17283.375</td>
    </tr>
    <tr>
      <th>전라남도</th>
      <td>42361.875</td>
      <td>45931.25</td>
      <td>36677.125</td>
    </tr>
    <tr>
      <th>전라북도</th>
      <td>39789.125</td>
      <td>37024.625</td>
      <td>28213.375</td>
    </tr>
    <tr>
      <th>제주특별자치도</th>
      <td>11530.875</td>
      <td>7168.625</td>
      <td>5162.375</td>
    </tr>
    <tr>
      <th>충청남도</th>
      <td>41779.625</td>
      <td>34142.125</td>
      <td>26865.75</td>
    </tr>
    <tr>
      <th>충청북도</th>
      <td>33579.375</td>
      <td>25440.0</td>
      <td>17998.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
awork=detailed.groupby('시도')[[f'{x}0대' for x in range(2,6)]].mean()
```


```python
awork_mean=(awork['20대']+awork['30대']+awork['40대']+awork['50대'])/4
```

8년 평균 10대  1인가구 분포


```python
idx=np.arange(8)
```


```python
xlabel
```




    [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]




```python
fig, ax = plt.subplots(figsize=(12,6))
bar_width = 0.1
plt.plot(idx,nationwide['실업률'],label='전국 실업률',marker='*',color='black',linestyle="--")
plt.bar(idx,detailed[detailed['시도']=='서울특별시']['실업률'],bar_width,label='서울')
plt.bar(idx+bar_width,detailed[detailed['시도']=='광주광역시']['실업률'],bar_width,label='광주')
plt.bar(idx+bar_width*2,detailed[detailed['시도']=='인천광역시']['실업률'],bar_width,label='인천')
plt.bar(idx+bar_width*3,detailed[detailed['시도']=='부산광역시']['실업률'],bar_width,label='부산')
plt.bar(idx+bar_width*4,detailed[detailed['시도']=='대전광역시']['실업률'],bar_width,label='대전')
plt.bar(idx+bar_width*5,detailed[detailed['시도']=='울산광역시']['실업률'],bar_width,label='울산')
plt.bar(idx+bar_width*6,detailed[detailed['시도']=='대구광역시']['실업률'],bar_width,label='대구')
plt.xticks(np.arange(bar_width, 8 + bar_width, 1), xlabel)

plt.legend()
```




    <matplotlib.legend.Legend at 0x17536589110>




    
![png](output_70_1.png)
    



```python
nationwide['실업률']
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
      <th>시도</th>
      <th>1인가구</th>
      <th>전체인구</th>
      <th>남자</th>
      <th>여자</th>
      <th>주택_계</th>
      <th>주택_단독주택</th>
      <th>주택_아파트</th>
      <th>주택_연립주택</th>
      <th>...</th>
      <th>취업가구</th>
      <th>실업률</th>
      <th>10대</th>
      <th>20대</th>
      <th>30대</th>
      <th>40대</th>
      <th>50대</th>
      <th>60대</th>
      <th>70대</th>
      <th>80대 이상~</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td>2015</td>
      <td>전국</td>
      <td>5203440</td>
      <td>51014947</td>
      <td>2592963</td>
      <td>2610477</td>
      <td>4783231</td>
      <td>2710775</td>
      <td>1433666</td>
      <td>85109</td>
      <td>...</td>
      <td>3139000</td>
      <td>39.6</td>
      <td>58020</td>
      <td>887023</td>
      <td>953322</td>
      <td>849758</td>
      <td>877549</td>
      <td>668183</td>
      <td>596918</td>
      <td>312667</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>전국</td>
      <td>5397615</td>
      <td>51217803</td>
      <td>2675861</td>
      <td>2721754</td>
      <td>4921788</td>
      <td>2742516</td>
      <td>1504073</td>
      <td>90023</td>
      <td>...</td>
      <td>3238000</td>
      <td>40.0</td>
      <td>62639</td>
      <td>929408</td>
      <td>948637</td>
      <td>843044</td>
      <td>911859</td>
      <td>743553</td>
      <td>615056</td>
      <td>343419</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2017</td>
      <td>전국</td>
      <td>5618677</td>
      <td>51361911</td>
      <td>2791849</td>
      <td>2826828</td>
      <td>5088437</td>
      <td>2765198</td>
      <td>1605878</td>
      <td>93832</td>
      <td>...</td>
      <td>3408000</td>
      <td>39.2</td>
      <td>61058</td>
      <td>961791</td>
      <td>968461</td>
      <td>862810</td>
      <td>947726</td>
      <td>805432</td>
      <td>643547</td>
      <td>367852</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2018</td>
      <td>전국</td>
      <td>5848594</td>
      <td>51585058</td>
      <td>2906320</td>
      <td>2942274</td>
      <td>5269889</td>
      <td>2762080</td>
      <td>1750760</td>
      <td>98323</td>
      <td>...</td>
      <td>3552000</td>
      <td>39.3</td>
      <td>58154</td>
      <td>1019944</td>
      <td>992737</td>
      <td>864221</td>
      <td>974444</td>
      <td>869904</td>
      <td>670897</td>
      <td>398293</td>
    </tr>
    <tr>
      <th>84</th>
      <td>2019</td>
      <td>전국</td>
      <td>6147516</td>
      <td>51764822</td>
      <td>3053733</td>
      <td>3093783</td>
      <td>5521438</td>
      <td>2789981</td>
      <td>1926935</td>
      <td>104497</td>
      <td>...</td>
      <td>3747000</td>
      <td>39.3</td>
      <td>59415</td>
      <td>1117581</td>
      <td>1035616</td>
      <td>871653</td>
      <td>999047</td>
      <td>932613</td>
      <td>696101</td>
      <td>435490</td>
    </tr>
    <tr>
      <th>102</th>
      <td>2020</td>
      <td>전국</td>
      <td>6643354</td>
      <td>51836239</td>
      <td>3304398</td>
      <td>3338956</td>
      <td>5920184</td>
      <td>2921200</td>
      <td>2124418</td>
      <td>114584</td>
      <td>...</td>
      <td>3972000</td>
      <td>40.0</td>
      <td>76202</td>
      <td>1266911</td>
      <td>1115518</td>
      <td>903816</td>
      <td>1039495</td>
      <td>1038985</td>
      <td>732715</td>
      <td>469712</td>
    </tr>
    <tr>
      <th>120</th>
      <td>2021</td>
      <td>전국</td>
      <td>7165788</td>
      <td>51744876</td>
      <td>3583770</td>
      <td>3582018</td>
      <td>6356409</td>
      <td>3024891</td>
      <td>2373162</td>
      <td>126862</td>
      <td>...</td>
      <td>4352000</td>
      <td>38.2</td>
      <td>54052</td>
      <td>1363552</td>
      <td>1226034</td>
      <td>950236</td>
      <td>1100914</td>
      <td>1176108</td>
      <td>771145</td>
      <td>523747</td>
    </tr>
    <tr>
      <th>138</th>
      <td>2022</td>
      <td>전국</td>
      <td>7502350</td>
      <td>51628117</td>
      <td>3751071</td>
      <td>3751279</td>
      <td>6640775</td>
      <td>3075767</td>
      <td>2553695</td>
      <td>134435</td>
      <td>...</td>
      <td>4555000</td>
      <td>36.9</td>
      <td>53088</td>
      <td>1386552</td>
      <td>1298846</td>
      <td>977577</td>
      <td>1137505</td>
      <td>1252607</td>
      <td>808984</td>
      <td>587191</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 23 columns</p>
</div>




```python

```
