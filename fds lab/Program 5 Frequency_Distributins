

(i) Ungrouped frequency distributions

Create the DataFrame

Program:
import pandas as pd
df = pd.DataFrame({
    'ID': ['1', '2', '3', '4', '5', '6'],
    'Product_name': ['alex', 'bob', 'cathy', 'doge', 'eric', 'fred'],
    'State': ['Taminadu', 'Tamilnadu', 'Taminadu', 'Andra', 'Madhyapradesh', 'Orissa'],
    'Salescount': ['1000', '2000', '3500', '450', '560', '250']})
print(df)

Output:
  ID Product_name          State Salescount
0  1         alex       Taminadu       1000
1  2          bob      Tamilnadu       2000
2  3        cathy       Taminadu       3500
3  4         doge          Andra        450
4  5         eric  Madhyapradesh        560
5  6         fred         Orissa        250

Histogram of the State column

Program:
import matplotlib.pyplot as plt
plt.hist(df['State'])
plt.ylabel('Frequency count')
plt.xlabel('Data')
plt.title('My histogram')
plt.show()



b) Grouped frequency distribution


Group by ID and plot the maximum Salescount

Program:
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'ID': ['1', '1', '2', '3', '4'],
    'Product_Name': ['CS', 'SE', 'SE', 'SE', 'CS'],
    'State': [60, 70, 59, 51, 80],
    'Salescount': [20, 21, 20, 22, 23]})
print(df)
df.groupby('ID')['Salescount'].max().plot(kind='bar', legend=True)
plt.show()

Output:
  ID Product_Name  State  Salescount
0  1           CS     60          20
1  1           SE     70          21
2  2           SE     59          20
3  3           SE     51          22
4  4           CS     80          23


c) Cumulative frequency distributions


Cumulative frequency using scipy.stats.cumfreq

Program:
from scipy import stats
import numpy as np
Salescount = [20, 21, 20, 22, 23]
print("Array element : ", Salescount, "\n")
a, b, c, d = stats.cumfreq(Salescount, numbins=4)
print("cumulative frequency : ", a)
print("Lower Limit : ", b)
print("bin size : ", c)
print("extra-points : ", d)

Output:
Array element :  [20, 21, 20, 22, 23] 

cumulative frequency :  [2. 3. 4. 5.]
Lower Limit :  19.5
bin size :  1.0
extra-points :  0

d) Relative frequency distributions


Relative frequency histogram

Program:
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
Salescount = [20, 21, 20, 22, 23]
print("Array element : ", Salescount, "\n")
a, b, c, d = stats.cumfreq(Salescount, numbins=4)
print("cumulative frequency : ", a)
print("Lower Limit : ", b)
print("bin size : ", c)
print("extra-points : ", d)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(Salescount, edgecolor='black', weights=np.ones_like(Salescount) / len(Salescount))
plt.show()

Output:
Array element :  [20, 21, 20, 22, 23] 

cumulative frequency :  [2. 3. 4. 5.]
Lower Limit :  19.5
bin size :  1.0
extra-points :  0

