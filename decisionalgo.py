# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:19:19 2020

@author: Neel
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import classification_report
import sklearn.metrics
import os

os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"

data = pd.read_excel("dataset.xlsx")
data = data[["age", "result", "Hematocrit", "Hemoglobin", "Platelets", "rbc", "Lympho", "Leuko", "Baso", "Eosino"]]
# data["result"].replace("negative", 0)
data["result"].replace("negative", 0, inplace=True)
data["result"].replace("positive", 1, inplace=True)
data_clean = data.dropna()

print(data_clean)

predictors = data_clean[["age", "Hematocrit", "Hemoglobin", "Platelets", "rbc", "Leuko"]]
targets = data_clean.result
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size = 0.4)

classifier = DecisionTreeClassifier()
classifier = classifier.fit(pred_train, tar_train)

predictions = classifier.predict(pred_test)

sklearn.metrics.confusion_matrix(tar_test, predictions)

accuracy = sklearn.metrics.accuracy_score(tar_test, predictions)
print(accuracy)

from sklearn import tree
from io import StringIO
from IPython.display import Image

out = StringIO()
tree.export_graphviz(classifier, out_file = out)

import pydotplus
graph=pydotplus.graph_from_dot_data(out.getvalue())
Image(graph.create_png())

graph.write_pdf("decision_tree.pdf")
graph.write_png("decision_tree.png")
