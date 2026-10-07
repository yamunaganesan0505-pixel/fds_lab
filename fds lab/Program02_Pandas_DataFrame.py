Program:
import pandas as pd
import matplotlib.pyplot as plt

author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti']

# Creating a simple Series
auth_series = pd.Series(author)
print(auth_series)

# Add series externally in DataFrame
article = [210, 211, 114, 178]

auth_series = pd.Series(author)
article_series = pd.Series(article)

frame = {
    'Author': auth_series,
    'Article': article_series
}

result = pd.DataFrame(frame)

age = [21, 21, 24, 23]
result['Age'] = pd.Series(age)

print(result)

Output:
0    Jitender
1    Purnima
2      Arpit
3      Jyoti
dtype: object

    Author  Article  Age
0  Jitender      210   21
1  Purnima      211   21
2    Arpit      114   24
3    Jyoti      178   23

Program 
import pandas as pd

df = pd.read_csv ('winequality-red.csv')
print(df)

Output 
fixed acidity;"volatile acidity";"citric acid";"residual sugar";
"chlorides";"free sulfur dioxide";"total sulfur dioxide";
"density";"pH";"sulphates";"alcohol";"quality"

0    7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5
1    7.8;0.88;0;2.6;0.098;25;67;0.9968;3.2;0.68;9.8;5

Program 
result = df.head(10)
print("First 10 rows of the DataFrame:")
print(result)

df_last_10 = df.tail(10)
print("last 10 rows of the DataFrame:")
print(df_last_10)

Output 
First 10 rows of the DataFrame:

fixed acidity;"volatile acidity";"citric acid";"residual sugar";
"chlorides";"free sulfur dioxide";"total sulfur dioxide";
"density";"pH";"sulphates";"alcohol";"quality"

0    7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5
1    7.8;0.88;0;2.6;0.098;25;67;0.9968;3.2;0.68;9.8;5
2    7.8;0.76;0.04;2.3;0.092;15;54;0.997;3.26;0.65;...
3    11.2;0.28;0.56;1.9;0.075;17;60;0.998;3.16;0.58...
4    7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5
5    7.4;0.66;0;1.8;0.075;13;40;0.9978;3.51;0.56;9.4;5
6    7.9;0.6;0.06;1.6;0.069;15;59;0.9964;3.3;0.46;9...
7    7.3;0.65;0;1.2;0.065;15;21;0.9946;3.39;0.47;10;7
8    7.8;0.58;0.02;2;0.073;9;18;0.9968;3.36;0.57;9.5;7
9    7.5;0.5;0.36;6.1;0.071;17;102;0.9978;3.35;0.8;...
1589    6.6;0.725;0.2;7.8;0.073;29;79;0.9977;3.29;0.54...
1590    6.3;0.55;0.15;1.8;0.077;26;35;0.99314;3.32;0.8...
1591    5.4;0.74;0.09;1.7;0.089;16;26;0.99402;3.67;0.5...
1592    6.3;0.51;0.13;2.3;0.076;29;40;0.99574;3.42;0.7...
1593    6.8;0.62;0.08;1.9;0.068;28;38;0.99651;3.42;0.8...
1594    6.2;0.6;0.08;2;0.09;32;44;0.9949;3.45;0.58;10.5;5
1595    5.9;0.55;0.1;2.2;0.062;39;51;0.99512;3.52;0.76...
1596    6.3;0.51;0.13;2.3;0.076;29;40;0.99574;3.42;0.7...
1597    5.9;0.645;0.12;2;0.075;32;44;0.99547;3.57;0.71...
1598    6;0.31;0.47;3.6;0.067;18;42;0.99549;3.39;0.66;...

Program 
shape = df.shape

print('\nDataFrame Shape :', shape)
print('\nNumber of rows :', shape[0])
print('\nNumber of columns :', shape[1])

Output
DataFrame Shape : (1599, 1)

Number of rows : 1599

Number of columns : 1

Program 
df=pd.read_csv('employees.csv')
df.head()

new_df=df[df['Bonus %']>5]
new_df

Output
First Name  Gender  Start Date  Last Login Time  Salary  Bonus %  Senior Management  Team

Douglas     Male    8/6/1993    12:42 PM         97308   6.945    True               Marketing
Maria       Female  4/23/1993   11:17 AM        130590  11.858    False              Finance
Jerry       Male    3/4/2005    1:00 PM         138705   9.340    True               Finance
Dennis      Male    4/18/1987   1:35 AM        115163  10.125    False              Legal
Ruby        Female  8/17/1987   4:20 PM         65476  10.012    True               Product
...
Tina        Female  5/15/1997   3:53 PM         56450  19.040    True               Engineering
Henry       NaN     11/23/2014  6:09 AM        132483  16.655    False              Distribution
Phillip     Male    1/31/1984   6:30 AM         42392  19.675    False              Finance
Larry       Male    4/20/2013   4:45 PM         60500  11.985    False              Business Development
Albert      Male    5/15/2012   6:24 PM        129949  10.169    True               Sales

Program
new_df=df.loc[df['Salary']>60000]
new_df

Program
# creating a rank column and passing the returned rank series
df["Rank"] = df["Salary"].rank()

# display
df

# sorting w.r.t name column
df.sort_values("Salary", inplace = True)

# display after sorting w.r.t Name column
df

Output
First Name  Gender  Start Date  Last Login Time  Salary  Bonus %  Senior Management  Team  Rank

Michael     Male    7/30/1993   5:35 PM          35013   14.879   False              Product  1.0
Kevin       Male    3/25/1982   7:31 AM          35061    5.128   False              Legal    2.0
Steven      Male    3/30/1980   9:20 PM          35095    8.379   True               Client Services  3.0
Matthew     Male    1/2/2013    10:33 PM         35203   18.040   False              Human Resources  4.0
Cynthia     Female  7/5/1986    1:24 AM          35381   11.749   False              Finance  5.0
...
Kathy       Female  3/18/2000   7:26 PM         149563   16.991   True               Finance  996.0

Program
# Calculate the Mean of 'Salary' column
mean = df['Salary'].mean()

# Print mean
print(mean)

Output 
90662.181

Program
# Calculate Median of 'Bonus %' column
median = df['Bonus %'].median()

# Print median
print(median)

Output 
9.8385

Program
# Calculate Count of 'Bonus %' column
count = df['Bonus %'].count()

# Print count
print(count)

Output 
1000

Program 
s = pd.value_counts(df.Salary)
s1 = pd.Series({'nunique': len(s), 'unique values': s.index.tolist()})
s.append(s1)

Output
121160    2
86676     2
91462     2
145988    2
147183    2
...
71975     1
72002     1
149908    1

nunique           995

unique values     [121160, 86676, 91462, 145988, 147183, 35013, ...]

Length: 997, dtype: object

Program 
#rename Team as Team_name
df3=df.rename(columns={'Team':'Team_name'},inplace=True)

Output 
First Name  Gender  Start Date  Last Login Time  Salary  Bonus %  Senior Management  Team_name  Rank

Michael     Male    7/30/1993   5:35 PM          35013   14.879   False              Product    1.0
Kevin       Male    3/25/1982   7:31 AM          35061    5.128   False              Legal      2.0
