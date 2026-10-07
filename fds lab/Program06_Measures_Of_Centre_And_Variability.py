

Measures of centre: mean, median and mode


Create the DataFrame

Program:
import pandas as pd
df = pd.DataFrame({
    'ID': ['1', '2', '3', '4', '5'],
    'Name': ['CS', 'SE', 'SE', 'SE', 'CS'],
    'Department': ['cse', 'eee', 'ece', 'it', 'AI'],
    'Year': ['3', '2', '1', '4', '1'],
    'Subject_Marks': [72, 73, 72, 72, 73]})
print(df)
dataMatrix = {"Subject_Marks": [72, 73, 72, 72, 73]}
dataFrame = pd.DataFrame(data=dataMatrix)
print("DataFrame:")
print(dataFrame)

Output:
  ID Name Department Year  Subject_Marks
0  1   CS        cse    3             72
1  2   SE        eee    2             73
2  3   SE        ece    1             72
3  4   SE         it    4             72
4  5   CS         AI    1             73
DataFrame:
   Subject_Marks
0             72
1             73
2             72
3             72
4             73

Mean (column-wise and row-wise)

Program:
print("Mean:Computed column-wise:")
print(dataFrame.mean())
print("Mean:Computed row-wise:")
print(dataFrame.mean(axis=1))

Output:
Mean:Computed column-wise:
Subject_Marks    72.4
dtype: float64
Mean:Computed row-wise:
0    72.0
1    73.0
2    72.0
3    72.0
4    73.0
dtype: float64

Median (column-wise and row-wise)

Program:
print("Median:Computed column-wise:")
print(dataFrame.median())
print("Median:Computed row-wise:")
print(dataFrame.median(axis=1))

Output:
Median:Computed column-wise:
Subject_Marks    72.0
dtype: float64
Median:Computed row-wise:
0    72.0
1    73.0
2    72.0
3    72.0
4    73.0
dtype: float64

Mode (column-wise and row-wise)

Program:
print("Mode:Computed column-wise:")
print(dataFrame.mode())
print("Mode:Computed row-wise:")
print(dataFrame.mode(axis=1))

Output:
Mode:Computed column-wise:
   Subject_Marks
0             72
Mode:Computed row-wise:
    0
0  72
1  73
2  72
3  72
4  73

Measures of variability: range, standard deviation, variance, IQR


Dataset information

Program:
import pandas as pd
import numpy as np
print(df.shape)
print(df.info())

Output:
(5, 5)
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 5 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   ID             5 non-null      str  
 1   Name           5 non-null      str  
 2   Department     5 non-null      str  
 3   Year           5 non-null      str  
 4   Subject_Marks  5 non-null      int64
dtypes: int64(1), str(4)
memory usage: 332.0 bytes
None

Range, standard deviation, variance, interquartile range and describe()

Program:
from scipy.stats import iqr
marks = dataFrame['Subject_Marks']
print([marks.min(), marks.max()])      # range
print(dataFrame.std())                 # standard deviation
print(dataFrame.var())                 # variance
print(iqr(marks))                      # interquartile range
print(dataFrame.describe(include='all'))

Output:
[np.int64(72), np.int64(73)]
Subject_Marks    0.547723
dtype: float64
Subject_Marks    0.3
dtype: float64
1.0
       Subject_Marks
count       5.000000
mean       72.400000
std         0.547723
min        72.000000
25%        72.000000
50%        72.000000
75%        73.000000
max        73.000000

