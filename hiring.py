import pandas as pd
from sklearn import linear_model
from word2number import w2n
import math

df=pd.read_csv('hiring.csv')
df.experience=df.experience.fillna('zero')
df.experience=df.experience.apply(w2n.word_to_num)
# print(df['experience'])
median_tscore=math.floor(df['test_score(out of 10)'].mean())
df['test_score(out of 10)']=df['test_score(out of 10)'].fillna(median_tscore)
# print(df['test_score(out of 10)'])
reg=linear_model.LinearRegression()
reg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df[['salary($)']])
print(reg.predict([[12,10,10]]))