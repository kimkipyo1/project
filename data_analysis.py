import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
from scipy import stats as spst
import seaborn as sns
import statsmodels.api as sm

telco = pd.read_csv("C:/Users/user/Documents/project1/The Telco Churn.csv")

# 범주형 데이터
# COLLEGE --> CHURN

feature = 'COLLEGE'
target = 'CHURN'

# 교차표 생성
table = pd.crosstab(telco[feature], telco[target], normalize = 'index')

# 1. 교차표 출력
print('교차표\n', table)
print('-' * 100)

# 2. 시각화(
plt.figure(figsize = (16, 4))
table.plot.bar(stacked=True)
plt.axhline(1 - telco[target].mean(), color = 'r')
plt.show()

mosaic(telco, [feature, target])
plt.axhline(1 - telco[target].mean(), color = 'r')
plt.show()

# 3. 가설검정(카이제곱검정)
# spst.chi2_contingency(교차표변수 이름) 카이제곱 검정 가능
result = spst.chi2_contingency(table)
print('카이제곱통계량', result[0])
print('p-value', result[1])
print('기대빈도\n',result[3])


# REPORTED_SATISFACTION --> CHURN
feature = 'REPORTED_SATISFACTION'

# 가변수화
# telco.loc = telco 행 뽑아오기
temp = telco.loc[telco[feature].notnull()]

temp['Satisfaction'] = 0
temp.loc[temp[feature] == 'very_sat', 'Satisfaction'] = 1
temp.loc[temp[feature] == 'sat', 'Satisfaction'] = 1
temp.loc[temp[feature] == 'avg', 'Satisfaction'] = 0
temp.loc[temp[feature] == 'unsat', 'Satisfaction'] = 0
temp.loc[temp[feature] == 'very_unsat', 'Satisfaction'] = 0

feature = 'Satisfaction'

# 교차표 생성
table = pd.crosstab(temp[feature], temp[target], normalize = 'index')

# 1. 교차표 출력
print('교차표\n', table)
print('-' * 100)

# 2. 시각화(
plt.figure(figsize = (16, 4))
table.plot.bar(stacked=True)
plt.axhline(1 - temp[feature].mean(), color = 'r')
plt.show()

mosaic(temp, [feature, target])
plt.axhline(1 - temp[target].mean(), color = 'r')
plt.show()

# 3. 가설검정(카이제곱검정)
result = spst.chi2_contingency(table)
print('카이제곱통계량', result[0])
print('p-value', result[1])
print('기대빈도\n',result[3])

# CONSIDERING_CHANGE_OF_PLAN --> CHURN

feature = 'CONSIDERING_CHANGE_OF_PLAN'

temp = telco.loc[telco[feature].notnull()]

temp['CONSIDERING'] = 0
temp.loc[temp[feature] == 'actively_looking_into_it', 'CONSIDERING'] = 1
temp.loc[temp[feature] == 'considering', 'CONSIDERING'] = 1
temp.loc[temp[feature] == 'perhaps', 'CONSIDERING'] = 0
temp.loc[temp[feature] == 'no', 'CONSIDERING'] = 0
temp.loc[temp[feature] == 'never_thought', 'CONSIDERING'] = 0

feature = 'CONSIDERING'

# 교차표 생성
table = pd.crosstab(temp[feature], temp[target], normalize = 'index')

# 1. 교차표 출력
print('교차표\n', table)
print('-' * 100)

# 2. 시각화(
plt.figure(figsize = (16, 4))
table.plot.bar(stacked=True)
plt.axhline(1 - temp[feature].mean(), color = 'r')
plt.show()

mosaic(temp, [feature, target])
plt.axhline(1 - temp[target].mean(), color = 'r')
plt.show()

# 3. 가설검정(카이제곱검정)
result = spst.chi2_contingency(table)
print('카이제곱통계량', result[0])
print('p-value', result[1])
print('기대빈도\n',result[3])

# 숫자형 데이터

# INCOME --> CHURN

feature = 'INCOME'

# 1. 시각화
plt.figure(figsize = (16, 4))

sns.histplot(x = feature, data = telco, hue = target)

sns.kdeplot(x = feature, data = telco, hue = target, common_norm = False)

plt.tight_layout()
plt.show()

# 2. 로지스틱 회귀

model = sm.Logit(telco[target], telco[feature])
result = model.fit()
print(result.pvalues)

# HANDSET_PRICE --> CHURN

feature = 'HANDSET_PRICE'

# 1. 시각화
plt.figure(figsize = (16, 4))

sns.histplot(x = feature, data = telco, hue = target)

sns.kdeplot(x = feature, data = telco, hue = target, common_norm = False)

plt.tight_layout()
plt.show()

# 2. 로지스틱 회귀

model = sm.Logit(telco[target], telco[feature])
result = model.fit()
print(result.pvalues)

# AVERAGE_CALL_DURATION --> CHURN

feature = 'AVERAGE_CALL_DURATION'

# 1. 시각화
plt.figure(figsize = (16, 4))

sns.histplot(x = feature, data = telco, hue = target)

sns.kdeplot(x = feature, data = telco, hue = target, common_norm = False)

plt.tight_layout()
plt.show()

# 2. 로지스틱 회귀

model = sm.Logit(telco[target], telco[feature])
result = model.fit()
print(result.pvalues)

