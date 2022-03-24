import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
import numpy as np

df = pd.read_csv("heart.csv", delimiter=";")
#print(df)


"""Logistische Regression"""

X = df[["thalach", "chol"]]
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75)
model = LogisticRegression(class_weight={1:100, 0:100})
model.fit(X_train, y_train)

y_test_pred = model.predict(X_test)

print(np.mean(y_test_pred == y_test))

"""Classification report"""

from sklearn.metrics import classification_report



"""Precision und Recall Score"""

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

y_test_pred = model.predict(X_test)

recall = recall_score(y_test, y_test_pred)
precision = precision_score(y_test, y_test_pred)

plot_confusion_matrix(model, X_test, y_test, normalize="all")

print(recall)
print(precision)