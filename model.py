import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df=pd.read_csv('automobileEDA.csv',header=0)
# X=df['highway-mpg']
# Y=df['price']
lm=LinearRegression()
# # Yat=lm.fit(X,Y)
# # print(Yat[0:5])
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
yat=lm.fit(Z,df['price'])
# print(yat)
# width = 12
# height = 10
# plt.figure(figsize=(width, height))
# sns.regplot(x="highway-mpg", y="price", data=df)
# plt.ylim(0,)
# plt.show()

# width = 12
# height = 10
# plt.figure(figsize=(width, height))
# sns.residplot(x=df['highway-mpg'],y=df['price'])
# plt.show()

Y_hat = lm.predict(Z)
plt.figure(figsize=(10, 12))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()