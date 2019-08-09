import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import PolynomialFeatures
from module_matplotlib import simple_plot

# Data import edilir.
path = '../Datasets/module_5_auto.csv'
df = pd.read_csv(path)

x_data = df.drop('price', axis=1)
y_data = df['price']

# Test ve train olarak iki parçaya ayrılır.
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.45, random_state=0)

lr = LinearRegression()

Rsqu_test = []
for n in range(1, 5):
    pr = PolynomialFeatures(degree=n)

    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])
    lr.fit(x_train_pr, y_train)
    Rsqu_test.append(lr.score(x_test_pr, y_test))


simple_plot(range(1, 5), Rsqu_test, 'order', 'R^2', 'R^2 Using Test Data')
