import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pylab import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv("happiness.csv")


"""Polynominal Regressoin"""

X = df[["GDP per capita", "Generosity"]].values
y = df[["Score"]].values
X_train, X_test, y_train, y_test = train_test_split(X, y)

poly = PolynomialFeatures(include_bias=False)
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly,y_train)
PR = (model.score(X_test_poly, y_test))
print(PR)