
Univariate analysis of numeric variables (Marks.csv)


Descriptive statistics plotted over the distribution of each variable

Program:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Marks.csv')

def UVA_numeric(data):
    var_group = data.columns
    size = len(var_group)
    plt.figure(figsize=(6 * size, 4))
    for j, i in enumerate(var_group):
        mini = data[i].min()
        maxi = data[i].max()
        ran = maxi - mini
        mean = data[i].mean()
        median = data[i].median()
        st_dev = data[i].std()
        skew = data[i].skew()
        kurt = data[i].kurtosis()
        points = mean - st_dev, mean + st_dev
        plt.subplot(1, size, j + 1)
        sns.histplot(data[i], kde=True, stat="density")
        sns.lineplot(x=list(points), y=[0, 0], color='black', label="std_dev")
        sns.scatterplot(x=[mini, maxi], y=[0, 0], color='orange', label="min/max")
        sns.scatterplot(x=[mean], y=[0], color='red', label="mean")
        sns.scatterplot(x=[median], y=[0], color='blue', label="median")
        plt.xlabel(i, fontsize=14)
        plt.ylabel('density')
        plt.title('std_dev = ({}, {}); kurtosis = {};\nskew = {}; range = ({}, {}, {})\nmean = {}; median = {}'.format(
            round(points[0], 2), round(points[1], 2), round(kurt, 2), round(skew, 2),
            round(mini, 2), round(maxi, 2), round(ran, 2), round(mean, 2), round(median, 2)), fontsize=8)
    plt.tight_layout()

UVA_numeric(df)
plt.show()



QQ plot


QQ plot of random data against the normal distribution

Program:
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
data_points = np.random.normal(0, 1, 100)
fig, ax = plt.subplots(figsize=(5, 4))
stats.probplot(data_points, dist="norm", plot=ax)
ax.set_title("QQ plot")
plt.show()


