# 데이터 전처리

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats as spst

# COLLEGE
# 전처리 사항 : NULL값 없음, 가변수화 0, 1 전처리 필요x

telco = pd.read_csv("C:/Users/user/Documents/project1/The Telco Churn.csv")
telco.drop(['ID', 'REPORTED_USAGE_LEVEL', 'OSVER_15MINS_CALLS_PER_MONTH'], axis = 1, inplace = True)

telco.head()

print(telco['COLLEGE'].value_counts())
print('-'*50)
print(telco['COLLEGE'].value_counts()/len(telco['COLLEGE']))

cnt = telco['COLLEGE'].value_counts()

# nrows = 1, ncols = 2, index = 1

cnt = telco['COLLEGE'].value_counts()
colors = sns.color_palette('muted')

plt.subplot(1,2,1)
sns.set_theme(style="whitegrid")
sns.barplot(x = cnt.index, y = cnt.values, palette = colors)

plt.subplot(1,2,2)
plt.pie(cnt.values, labels = cnt.index, colors = colors, autopct = '%.2f%%')
plt.show()

# INCOME
# describe : 데이터 요약, 기초 통계량 표시
print(telco['INCOME'].describe())

# figure 복수 개의 그림을 동시에 그리고 싶을 때 사용, 그림의 크기, 해상도 배경색 등의 속성을 직접 지정하고 싶을 때
plt.figure(figsize  = (16,4))
plt.subplot(1,2,1)
# bins = 가로축 개수 지정
sns.histplot(data = telco, x= 'INCOME', bins = 30, palette = colors)

plt.subplot(1,2,2)
sns.kdeplot(data = telco, x = 'INCOME', palette = colors)

# tight_layout 촘촘하게 그래프 표시
plt.tight_layout()
plt.show()

# HANDSET_PRICE
print(telco['HANDSET_PRICE'].describe())

plt.figure(figsize  = (16,4))
plt.subplot(1,2,1)
sns.histplot(data = telco, x= 'HANDSET_PRICE', bins = 30, palette = colors)

plt.subplot(1,2,2)
sns.kdeplot(data = telco, x = 'HANDSET_PRICE', palette = colors)

plt.tight_layout()
plt.show()

# AVERAGE_CALL_DURATION
print(telco['AVERAGE_CALL_DURATION'].describe())

plt.figure(figsize  = (16,4))
plt.subplot(1,2,1)
sns.histplot(data = telco, x= 'AVERAGE_CALL_DURATION', bins = 30)

plt.subplot(1,2,2)
sns.kdeplot(data = telco, x = 'AVERAGE_CALL_DURATION')

plt.tight_layout()
plt.show()

# REPORTED_SATISFACTION
print(telco['REPORTED_SATISFACTION'].value_counts())
print('-'*50)
print(telco['REPORTED_SATISFACTION'].value_counts()/len(telco['REPORTED_SATISFACTION']))

cnt = telco['REPORTED_SATISFACTION'].value_counts()

plt.figure(figsize  = (16,4))
plt.subplot(1,2,1)
sns.barplot(x = cnt.index, y = cnt.values, palette = colors)

plt.subplot(1,2,2)
plt.pie(cnt.values, labels = cnt.index, autopct = '%.2f%%', colors = colors)

plt.tight_layout()
plt.show()

# CONSIDERING_CHANGE_OF_PLAN
print(telco['CONSIDERING_CHANGE_OF_PLAN'].value_counts())
print('-'*50)
print(telco['CONSIDERING_CHANGE_OF_PLAN'].value_counts()/len(telco['CONSIDERING_CHANGE_OF_PLAN']))

cnt = telco['CONSIDERING_CHANGE_OF_PLAN'].value_counts()

plt.figure(figsize  = (16,4))
plt.subplot(1,2,1)
sns.barplot(x = cnt.index, y = cnt.values, palette = colors)

plt.subplot(1,2,2)
plt.pie(cnt.values, labels = cnt.index, autopct = '%.2f%%', colors = colors)
plt.tight_layout()
plt.show()

# CHURN
print(telco['CHURN'].value_counts())
print('-'*50)
print(telco['CHURN'].value_counts()/len(telco['CHURN']))

cnt = telco['CHURN'].value_counts()

plt.subplot(1,2,1)
sns.barplot(x = cnt.index, y = cnt.values, palette= colors)

plt.subplot(1,2,2)
plt.pie(cnt.values, labels = cnt.index, autopct = '%.2f%%', colors = colors)
plt.tight_layout()
plt.show()