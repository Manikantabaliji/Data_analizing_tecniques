import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#creating pandas data frame
df=pd.read_csv('titanic.csv')

#dropping all the unecassery coloumns
df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)

#creating dummy variables
dummies = pd.get_dummies(df.Sex)

#concatinating the dummies and main data frame
mergeddf=pd.concat([df,dummies],axis='columns')

#droping the Sex column and one dumy varible coloumn
final=mergeddf.drop(['Sex','male'],axis='columns')

#data preprocesing/data cleaning

final['Pclass'].fillna(final['Pclass'].mean(),inplace=True)#filling Pclass with avg value
final['Age'].fillna(final['Age'].mean(),inplace=True)#filling empty age cells with the avg age
final['Fare'].fillna(final['Fare'].mean(),inplace=True)#filling empty fare cells with avg Fare
final['female'].fillna(final['female'].mode()[0],inplace=True)#filling sex with mode of the column


# splittin the data set into 80:20 train:test 
X_train, X_test, y_train, y_test = train_test_split(final[['Pclass','Age','Fare','female']],final.Survived,test_size=0.2)
#creating logestic model

model=LogisticRegression()
model.fit(X_train,y_train)

# print(model.predict(X_test))
print(model.predict([[1,38,73,1]]))

# print(final.describe())


# print(y_train[0:6])