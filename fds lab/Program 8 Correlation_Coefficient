

a) Plot the correlation plot on dataset and visualize an overview of relationships among data (Iris)


Read the data

Program:
import pandas as pd
df = pd.read_csv("Iris.csv")
print(df.head())
print(df.shape)
print(df.isnull().sum())

Output:
   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0   1            5.1           3.5            1.4           0.2  Iris-setosa
1   2            4.9           3.0            1.4           0.2  Iris-setosa
2   3            4.7           3.2            1.3           0.2  Iris-setosa
3   4            4.6           3.1            1.5           0.2  Iris-setosa
4   5            5.0           3.6            1.4           0.2  Iris-setosa
(150, 6)
Id               0
SepalLengthCm    0
SepalWidthCm     0
PetalLengthCm    0
PetalWidthCm     0
Species          0
dtype: int64

Unique species and counts

Program:
data = df.drop_duplicates(subset="Species")
print(data)
print(df.value_counts("Species"))

Output:
      Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm          Species
0      1            5.1           3.5            1.4           0.2      Iris-setosa
50    51            7.0           3.2            4.7           1.4  Iris-versicolor
100  101            6.3           3.3            6.0           2.5   Iris-virginica
Species
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
Name: count, dtype: int64

Count plot of Species

Program:
import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='Species', data=df)
plt.show()


b) Find the correlation matrix


Pearson correlation matrix with dataframe.corr()

Program:
num = df.select_dtypes('number')
print(num.corr(method='pearson'))

Output:
                     Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
Id             1.000000       0.716676     -0.402301       0.882637      0.900027
SepalLengthCm  0.716676       1.000000     -0.117570       0.871754      0.817941
SepalWidthCm  -0.402301      -0.117570      1.000000      -0.428440     -0.366126
PetalLengthCm  0.882637       0.871754     -0.428440       1.000000      0.962865
PetalWidthCm   0.900027       0.817941     -0.366126       0.962865      1.000000

Heatmap of the correlation matrix

Program:
corr = num.corr()
plt.figure(figsize=(6, 4.5))
sns.heatmap(corr, annot=True, cmap='coolwarm', xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.title("Correlation matrix (Pearson)")
plt.show()

c) Analysis of variance (ANOVA), when data have categorical variables - Iris

Mean sepal width per species

Program:
print(df['SepalWidthCm'].groupby(df['Species']).mean())
print(df.drop(columns='Species').mean())

Output:
Species
Iris-setosa        3.428
Iris-versicolor    2.770
Iris-virginica     2.974
Name: SepalWidthCm, dtype: float64
Id               75.500000
SepalLengthCm     5.843333
SepalWidthCm      3.057333
PetalLengthCm     3.758000
PetalWidthCm      1.199333
dtype: float64

