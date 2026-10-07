
Load and explore the data


Read the dataset

Program:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("binary.csv")
print(type(dataset))
print(dataset.head())
print(dataset.shape)
print(dataset.info())
print(dataset.count())
print(dataset.columns)

Output:
<class 'pandas.DataFrame'>
   admit  gre   gpa  rank
0      0  600  3.33     3
1      0  400  2.95     2
2      0  500  3.82     2
3      0  720  3.29     4
4      0  440  3.26     3
(400, 4)
<class 'pandas.DataFrame'>
RangeIndex: 400 entries, 0 to 399
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   admit   400 non-null    int64  
 1   gre     400 non-null    int64  
 2   gpa     400 non-null    float64
 3   rank    400 non-null    int64  
dtypes: float64(1), int64(3)
memory usage: 12.6 KB
None
admit    400
gre      400
gpa      400
rank     400
dtype: int64
Index(['admit', 'gre', 'gpa', 'rank'], dtype='str')

Distribution of GRE scores and GPA grades

Program:
import seaborn as sns
sns.set(style="white", context="talk")
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
sns.histplot(dataset.iloc[:, 1], kde=True, stat="density", ax=ax1, color="r")
sns.histplot(dataset.iloc[:, 2], kde=True, stat="density", ax=ax2, color="g")
plt.tight_layout()
plt.show()



Multivariate analysis

Program:
sns.pairplot(dataset, hue='admit', palette="husl", x_vars=["gre", "gpa", "rank"], y_vars=["gre", "gpa", "rank"], height=2.5)
plt.show()



Split the data and compare models

Training / testing split

Program:
from sklearn.model_selection import train_test_split
dataArray = dataset.values
X = dataArray[:, 1:4]
y = dataArray[:, 0]
validation_size = 0.10
seed = 9
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=validation_size, random_state=seed)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

Output:
(360, 3)
(40, 3)
(360,)
(40,)

Prepare the models and evaluate each with 10-fold cross validation

Program:
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

num_trees = 200
max_features = 3
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('RF', RandomForestClassifier(n_estimators=num_trees, max_features=max_features)))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

results = []
names = []
scoring = 'accuracy'
for name, model in models:
    kfold = KFold(n_splits=10, shuffle=True, random_state=7)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    print("%s: %f (%f)" % (name, cv_results.mean(), cv_results.std()))

Output:
LR: 0.800000 (0.080316)
LDA: 0.800000 (0.080316)
KNN: 0.769444 (0.079592)
CART: 0.700000 (0.063099)
RF: 0.738889 (0.050000)
NB: 0.788889 (0.075768)
SVM: 0.791667 (0.079786)

Box plots for machine learning algorithm comparison

Program:
fig = plt.figure()
fig.suptitle('Machine Learning algorithms comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()



Logistic Regression model


Create, fit and evaluate the model

Program:
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
model = LogisticRegression()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)
print("Model --> Logistic Regression")
print("Overall Accuracy: {}".format(accuracy_score(Y_test, predictions) * 100))
print(classification_report(Y_test, predictions))

Output:
Model --> Logistic Regression
Overall Accuracy: 80.0
              precision    recall  f1-score   support

         0.0       0.80      1.00      0.89        32
         1.0       0.00      0.00      0.00         8

    accuracy                           0.80        40
   macro avg       0.40      0.50      0.44        40
weighted avg       0.64      0.80      0.71        40

Confusion matrix heatmap

Program:
cm = confusion_matrix(Y_test, predictions)
plt.figure(figsize=(4, 3.5))
sns.heatmap(cm, annot=True, fmt='d', xticklabels=['reject', 'admit'], yticklabels=['reject', 'admit'])
plt.xlabel("Predicted"); plt.ylabel("Actual")
plt.show()

Make predictions on new data - (gre_score, gpa_grade, rank)

Program:
new_data = [(720, 4, 1), (300, 2, 1), (400, 4, 4)]
new_array = np.asarray(new_data)
labels = ["reject", "admit"]
prediction = model.predict(new_array)
no_of_test_cases, cols = new_array.shape
for i in range(no_of_test_cases):
    print("Status of STUDENT with GRE score= {}, GPA grade= {}, Rank= {} will be --> {}".format(
        new_data[i][0], new_data[i][1], new_data[i][2], labels[int(prediction[i])]))

Output:
Status of STUDENT with GRE score= 720, GPA grade= 4, Rank= 1 will be --> reject
Status of STUDENT with GRE score= 300, GPA grade= 2, Rank= 1 will be --> reject
Status of STUDENT with GRE score= 400, GPA grade= 4, Rank= 4 will be --> reject

