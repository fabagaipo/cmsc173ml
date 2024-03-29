# -*- coding: utf-8 -*-
"""Bagaipo_Assignment3_MultiClassDataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cy_iihMFuEgHMZpfPqOtJnJdA4WRVeI0

# Imports
"""

import pandas as pd
import seaborn as sns

"""# Reading the Dataset"""

url = 'https://raw.githubusercontent.com/fabagaipo/cmsc173ml/main/datasets/glass.csv'
df = pd.read_csv(url, header=None)
df.columns = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5", "Feature6", "Feature7", "Feature8", "Feature9", "Target"]
df.head()

df.shape

sns.countplot(df['Target'])

df.corr()

sns.heatmap(df.corr())

"""# Cleaning the Dataset"""

df.isnull().sum()

len(df[df.duplicated()])

df.drop(df[df.duplicated()].index, axis=0, inplace=True)

df['Target'].value_counts()

"""# Splitting data"""

X = df.drop('Target',axis=1)
y=df['Target']
test_size = 0.2     # 80% training and 20% testing

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=888)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""# Model Evaluation with Imbalanced Dataset"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

model = KNeighborsClassifier()

y_train.value_counts()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy_original = accuracy_score(y_test, y_pred)
print("Accuracy: %.3f%%" % (accuracy_original))

report_original = classification_report(y_test, y_pred)
print(report_original)

confusionMatrix_original = confusion_matrix(y_test, model.predict(X_test))
sns.heatmap(confusionMatrix_original, annot=True, fmt=".0f")

"""# Handling Imbalanced Dataset"""

pip install -U imbalanced-learn

"""---
- Undersampling Method
"""

from imblearn.under_sampling import RandomUnderSampler
rus = RandomUnderSampler()
X_resampled_under, y_resampled_under = rus.fit_resample(X_train, y_train)

y_resampled_under.value_counts()

model.fit(X_resampled_under, y_resampled_under)
y_pred_under = model.predict(X_test)

accuracy_under = accuracy_score(y_test, y_pred_under)
print("Accuracy: %.3f%%" % (accuracy_under))

report_under = classification_report(y_test, y_pred_under)
print(report_under)

confusionMatrix_under = confusion_matrix(y_test, model.predict(X_test))
sns.heatmap(confusionMatrix_under, annot=True, fmt=".0f")

"""---
- Oversampling Method
"""

from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler()
X_resampled_over, y_resampled_over = ros.fit_resample(X_train, y_train)

y_resampled_over.value_counts()

model.fit(X_resampled_over, y_resampled_over)
y_pred_over = model.predict(X_test)

accuracy_over = accuracy_score(y_test, y_pred_over)
print("Accuracy: %.3f%%" % (accuracy_over))

report_over = classification_report(y_test, y_pred_over)
print(report_over)

confusionMatrix_over = confusion_matrix(y_test, model.predict(X_test))
sns.heatmap(confusionMatrix_over, annot=True, fmt=".0f")

"""# Evaluation

With the original dataset, we can see the accuracy results of 60% for predicting the glass targets. However, this accuracy is unreliable as we see how uneven each class is from each other. This is the definition of imbalanced datasets. Imbalanced datasets are those where there is a severe skew in the class distribution, such as 1:100 or 1:1000 examples in the minority class to the majority class. As can be seen in the report for the original dataset, the metrics of class=1, class=2 and class=3 are low. Although our model has a high accuracy, the accuracy only reflects that of class=5 and class=6.

After handling our imbalanced dataset with the methods of oversampling and undersampling, we see the accuracy drop down from the results of the original dataset (undersampling = 49% and oversampling = 56%). This is a significant decrease from that of the original report. According to the model, the prediction of the other high metric classes has decreased, but there is also an increase in the recall metric of the lower valued classes, which means that the rate of predicting those lower of the model increased.
"""