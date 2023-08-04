import pandas as pd
from sklearn import linear_model
from matplotlib import pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

df=load_digits()
# plt.gray()
# plt.matshow(df.images[2])
X_train, X_test, y_train, y_test = train_test_split(df.images,df.target,test_size=0.2)
# print(y_test[0:5])
model=linear_model.LogisticRegression()
model.fit(X_train,y_train)

# print(model.score(X_test,y_test))
print(model.predict(df.images[67]))

