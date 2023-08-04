import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from scipy.stats import f_oneway

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df=pd.read_csv("auto.csv")
df.columns=headers
df.replace("?",np.nan, inplace=True)
# missing_data = df.isnull()
# for columuns in missing_data.columns.values.tolist():
#     print(columuns)
#     print(missing_data[columuns].value_counts())
#     print(" ")
avg_stroke = df["stroke"].astype("float").mean(axis = 0)
df["stroke"].replace(np.nan, avg_stroke, inplace = True)
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)
df["num-of-doors"].replace(np.nan, "four", inplace=True)

normlossavg=df["normalized-losses"].astype(float).mean()
df["normalized-losses"].replace(np.nan,normlossavg,inplace=True)
# print(df.head(10))
avg_bore=df['bore'].astype('float').mean(axis=0)
df["bore"].replace(np.nan, avg_bore, inplace=True)
# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Data standardization
df['city-L/100km'] = 235/df["city-mpg"]
df.rename(columns={'highway-mpg':'highway-L/100km'},inplace=True)
#data normalization
# replace (original value) by (original value)/(maximum value)
# df[["length","width","height"]]=df[["length","width","height"]].astype(float)
# df["length"] = df["length"]/df["length"].max()
# df["width"] = df["width"]/df["width"].max()
# df["height"] = df["height"]/df["height"].max()

# print(df["length","width","height"].head(10))/
df["horsepower"]=df["horsepower"].astype(int, copy=True)


# plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
# plt.pyplot.xlabel("horsepower")
# plt.pyplot.ylabel("count")
# plt.pyplot.title("horsepower bins")
# draw historgram of attribute "horsepower" with bins = 3
# plt.pyplot.hist(df["horsepower"], bins = 3)

# # set x/y labels and plot title
# plt.pyplot.xlabel("horsepower")
# plt.pyplot.ylabel("count")
# plt.pyplot.title("horsepower bins")


dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
# merge data frame "df" and "dummy_variable_1" 
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
# df.drop("fuel-type", axis = 1, inplace=True)
# df.to_csv("C:\Users\balij\OneDrive\Desktop\Data Analysis")
# print(df.head())
# print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())
# Engine size as potential predictor variable of price
# sns.regplot(x="peak-rpm", y="price", data=df)
# sns.regplot(x="engine-size", y="price", data=df)
# sns.boxplot(x="body-style", y="price", data=df)
# plt.ylim(0,)

# sns.boxplot(x="engine-location", y="price", data=df)
# plt.show()


# print(df.describe(include="all"))
# drive_wheel_counts=df['drive-wheels'].value_counts().to_frame()
# drive_wheel_counts.rename(columns={'drive-wheels':'value_counts'},inplace=True)
# drive_wheel_counts.index.name="drive wheels"
# print(drive_wheel_counts)
# print(df['drive-wheels'].unique())
df_group_one = df[['drive-wheels','body-style','price']]
# df_group_one=df_group_one.groupby(['drive-wheels','body-style'],as_index=False).mean()
# grouped_pivot=df_group_one.pivot(index='drive-wheels',columns='body-style')
# # plt.pcolor(df,cmap='RdBu')
# # plt.colorbar()
# # plt.show()
# # print(df_group_one)
# fig, ax = plt.subplots()
# im = ax.pcolor(grouped_pivot, cmap='RdBu')

# #label names
# row_labels = grouped_pivot.columns.levels[1]
# col_labels = grouped_pivot.index

# #move ticks and labels to the center
# ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
# ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

# #insert labels
# ax.set_xticklabels(row_labels, minor=False)
# ax.set_yticklabels(col_labels, minor=False)

# #rotate label if too long
# plt.xticks(rotation=90)

# fig.colorbar(im)
# plt.show()
# person_corr,p_value=stats.pearsonr(df['highway-L/100km'],df['price'])
# print(person_corr,p_value)
# print(grouped_test2.head(2))
grouped_test2=df_group_one[['drive-wheels', 'price']].groupby(['drive-wheels'])
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])  
print( "ANOVA results: F=", f_val, ", P =", p_val)   