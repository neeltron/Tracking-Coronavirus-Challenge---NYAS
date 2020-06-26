# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:10:10 2020

@author: Neel
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import sklearn.metrics
from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
import os

os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"

data = pd.read_csv("COVID-19 Cases.csv", low_memory = False)

data = data[["Lat", "Long", "Population_Count", "Cases"]].dropna()
data_clean = data[["Lat", "Long", "Population_Count", "Cases"]]
data_clean = data_clean.astype("int")
data_clean = data_clean[(data_clean["Lat"] > 0)]
print(data_clean.head(170))
data_clean = data_clean.dropna()
print(data_clean.head(170))
print(data_clean["Lat"].dtypes)
data_clean = data_clean.head(300000)
# data_clean.fillna(data_clean.mean())
# data_clean = data_clean.replace([np.inf, -np.inf], np.nan).dropna(axis=0)

data_clean.dtypes
data_clean.describe()

predictors = data_clean[["Lat", "Long", "Population_Count"]]
targets = data_clean.Cases
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size = .4)

print(pred_train.shape)
print(pred_test.shape)
print(tar_train.shape)
print(tar_test.shape)

classifier = RandomForestClassifier(n_estimators = 25)
classifier = classifier.fit(pred_train, tar_train)

predictions = classifier.predict(pred_test)
print(predictions)

print(sklearn.metrics.confusion_matrix(tar_test, predictions))

accuracy = sklearn.metrics.accuracy_score(tar_test, predictions)
print(accuracy)

predict = classifier.predict([[72.76, 164.464, 69]])
print(predict)

model = ExtraTreesClassifier()
model.fit(pred_train, tar_train)

print(model.feature_importances_)

trees = range(25)
accuracy = np.zeros(25)

for idx in range(len(trees)):
    classifier = RandomForestClassifier(n_estimators = idx + 1)
    classifier = classifier.fit(pred_train, tar_train)
    predictions = classifier.predict(pred_test)
    accuracy[idx] = sklearn.metrics.accuracy_score(tar_test, predictions)
    


plt.cla()
plt.plot(trees, accuracy)

# from sklearn import tree
# from io import StringIO
# from IPython.display import Image

# out = StringIO()
# tree.export_graphviz(classifier, out_file = out)

# import pydotplus
# graph=pydotplus.graph_from_dot_data(out.getvalue())
# Image(graph.create_png())

# graph.write_pdf("decision_forest_.pdf")
# graph.write_png("decision_forest.png")
