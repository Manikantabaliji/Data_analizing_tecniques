import pandas as pd
from sklearn import linear_model
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

df=load_iris()
print(dir(df.target_names[0:2]))