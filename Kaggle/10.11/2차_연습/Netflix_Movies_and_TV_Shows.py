import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import pandas as pd

# 데이터 불러오기
DATA_PATH = './data/'
df = pd.read_csv(DATA_PATH + 'netflix_titles.csv')

# 데이터 확인
print(df.head()) ## 데이터 로드 확인
msno.matrix(df) ## 데이터 null 유무 확인


# 데이터 전처리
## 0. cast에 있는 배우 리스트
df_actors = df[['cast']]
actors = df_actors['cast'].str.split(',')
titles = df['title', df['cast'].str.split(',')]

print(actors)
print(titles)
print('-------------------------')
# df[df['cast'].isnull()].get('title') ## cast가 null인 데이터 확인
# df[df['diractor'].isnull()].get('title') ## director가 null인 데이터 확인
print('-------------------------')

##
actor_check = dict()
for i in range(len(actors)):
	if type(actors[i]) != list:
		continue

	for j in range(len(actors[i])):
		actors[i][j] = actors[i][j].strip() ## 공백 제거

		if actors[i][j] not in actor_check: ## 배우가 이미 있는 경우
			actor_check[actors[i][j]] = 1
		elif actors[i][j] in actor_check:
			actor_check[actors[i][j]] += 1


## 1. cast에 존재하는 배우들의 영화와 드라마 출연 횟수


## 2. 배우들이 디렉터와 같이 일 한 횟수

#%%
