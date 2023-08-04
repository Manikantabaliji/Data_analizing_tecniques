import pandas as pd
import numpy as np
from sklearn import linear_model

df=pd.read_csv('carprices.csv')
dummies=pd.get_dummies(df['Car Model'])
merged=pd.concat([df,dummies],axis='columns')
final=merged.drop(['Car Model','BMW X5'],axis='columns')
model=linear_model.LinearRegression()
X=final.drop(['Sell Price($)'],axis='columns')
Y=final['Sell Price($)']
model.fit(X,Y)
print(model.predict([[57000,5,0,0]]))