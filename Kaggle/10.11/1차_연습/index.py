## 1. csv 선정
## 2. csv 데이터 분석
## 3. 시각화 할 데이터 개념 정리
## 4. csv 데이터 시각화


## 0. 라이브러리 불러오기
import pandas as pd
import missingno as msno # 입력된 데이터의 결함(결측치)를 그래프로 시각화
import numpy as np
import matplotlib.pyplot as plt


## 1. csv 로드
DATA_PATH = './data/'
df = pd.read_csv(DATA_PATH + 'accessories.csv')
print(df.head())

## 데이터 null 빈칸 확인
msno.matrix(df)
fig = plt.figure(figsize = (10, 10))
fig.show()

## 2. csv 데이터 분석
## 2-1. 필요한 컬럼 분석

## - 이름    Name
## - 카테고리 Type
## - 컬러    Variation
## - 가격    Sell
## 2-2. 불러온 데이터로 그래프 데이터 생성
## 컬러별 상품의 가격의 편차 분석
## 상품 카테고리 별 컬러 종류
df = df[['Type', 'Variation', 'Sell']]
group_df = df.groupby(['Type', 'Variation']).count()
print(group_df)

## 상품 카테고리 별 컬러 종류
### 그래프 생성
plt.figure(figsize = (10, 10))
plt.title('Type - Variation', fontdict = {'fontsize': 20})
# plt.subplot(111, projection = '3d')
# plt.xlabel('Type')
# plt.ylabel('Variation')
# plt.zlabel('Sell')

# xs = np.array(group_df.index.get_level_values(0))
# ys = np.array(group_df.index.get_level_values(1))
# zs = np.array(group_df['Sell'])

plt.plot(
	group_df.values,
	scalex = True,
	scaley = True,
	linestyle = '-',
	marker = 'o',
)
plt.legend()
# ax = plt.gca()
# ax.scatter(xs, ys, zs, c = 'r', marker = 'o')
# ax.set_xlabel('Type')
# ax.set_ylabel('Variation')
# ax.set_zlabel('Sell')
plt.show()

## -- 시간초과로 인해 3D 작업 중단