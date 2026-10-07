
a) Handle missing data by detecting and dropping / filling missing values

(i) Using isnull() - rows where Team is NaN

Program:
import pandas as pd
data = pd.read_csv("employees.csv")
bool_series = pd.isnull(data["Team"])
print(data[bool_series].head(10))
print("Rows with missing Team:", bool_series.sum())

Output:
      First Name  Gender  Start Date Last Login Time  Salary  Bonus % Senior Management Team
1         Thomas    Male   3/31/1996         6:53 AM   61933    4.170              True  NaN
26         Maria     NaN   7/25/2012        12:37 PM   89867    3.513              True  NaN
41         Jerry  Female   4/29/1985         4:27 AM  112704   13.782             False  NaN
43          Tina  Female   2/14/2009        10:32 AM   83723   11.094             False  NaN
59      Kimberly  Female    8/7/1994         4:12 PM  119744    6.829              True  NaN
62         Henry  Female   7/30/2005         2:24 AM  136706    4.250              True  NaN
81       Frances  Female   4/29/1986         6:16 PM   71285    8.407             False  NaN
95         Kevin    Male  10/24/2006         7:37 PM   66697   14.656             False  NaN
130      Cynthia  Female   1/21/2010         8:01 AM   99374    7.758              True  NaN
155  Christopher    Male   5/11/2011         2:28 AM   35072   10.065             False  NaN
Rows with missing Team: 41

(ii) Using notnull() - rows where Gender is not NaN

Program:
bool_series = pd.notnull(data["Gender"])
print(data[bool_series].head(9))
print("Rows with a Gender value:", bool_series.sum())

Output:
  First Name  Gender  Start Date Last Login Time  Salary  Bonus % Senior Management  \
0    Douglas    Male    8/6/1993        12:42 PM   97308    6.945              True   
1     Thomas    Male   3/31/1996         6:53 AM   61933    4.170              True   
2      Maria  Female   4/23/1993        11:17 AM  130590   11.858             False   
3      Jerry    Male    3/4/2005         1:00 PM  138705    9.340              True   
4      Larry    Male   1/24/1998         4:47 PM  101004    1.389              True   
5    Brandon    Male  10/20/1995        11:49 PM  127963    6.183               NaN   
6    Douglas  Female    7/4/2009         3:32 PM  148888    7.852              True   
7      Henry    Male  12/26/1994         6:10 PM   85016   14.044              True   
8    Brandon    Male   7/21/1995        12:09 PM  117902    1.003              True   

              Team  
0        Marketing  
1              NaN  
2          Finance  
3          Finance  
4  Client Services  
5      Engineering  
6            Sales  
7        Marketing  
8            Legal  
Rows with a Gender value: 970

(iii) Dropping rows with at least 1 null value

Program:
new_data = data.dropna(axis=0, how='any')
print(new_data.head(10))
print("Rows before:", len(data), " rows after dropna:", len(new_data))

Output:
   First Name  Gender  Start Date Last Login Time  Salary  Bonus % Senior Management  \
0     Douglas    Male    8/6/1993        12:42 PM   97308    6.945              True   
2       Maria  Female   4/23/1993        11:17 AM  130590   11.858             False   
3       Jerry    Male    3/4/2005         1:00 PM  138705    9.340              True   
4       Larry    Male   1/24/1998         4:47 PM  101004    1.389              True   
6     Douglas  Female    7/4/2009         3:32 PM  148888    7.852              True   
7       Henry    Male  12/26/1994         6:10 PM   85016   14.044              True   
8     Brandon    Male   7/21/1995        12:09 PM  117902    1.003              True   
9     Michael  Female  11/16/1986        11:32 AM   41400   15.192             False   
10     Louise  Female   8/18/2000         9:55 AM   81204    7.440             False   
11      Henry  Female   3/11/1990         2:15 PM  135111   11.949              True   

               Team  
0         Marketing  
2           Finance  
3           Finance  
4   Client Services  
6             Sales  
7         Marketing  
8             Legal  
9   Client Services  
10            Sales  
11        Marketing  
Rows before: 1000  rows after dropna: 858

(iv) Replacing NaN values with a static value - nba.csv before

Program:
nba = pd.read_csv("nba.csv")
print(nba)

Output:
               Name            Team  Number Position  Age Height  Weight            College  \
0     Avery Bradley  Boston Celtics       0       PG   25    6-2     180              Texas   
1       Jae Crowder  Boston Celtics      99       SF   25    6-6     235          Marquette   
2      John Holland  Boston Celtics      30       SG   27    6-5     205  Boston University   
3       R.J. Hunter  Boston Celtics      28       SG   22    6-5     185      Georgia State   
4     Jonas Jerebko  Boston Celtics       8       PF   29   6-10     231                NaN   
5      Amir Johnson  Boston Celtics      90       PF   29    6-9     240                NaN   
6     Jordan Mickey  Boston Celtics      55       PF   21    6-8     235                LSU   
7      Kelly Olynyk  Boston Celtics      41        C   25    7-0     238            Gonzaga   
8      Terry Rozier  Boston Celtics      12       PG   22    6-2     190         Louisville   
9      Marcus Smart  Boston Celtics      36       PG   22    6-4     220     Oklahoma State   
10  Jared Sullinger  Boston Celtics       7        C   24    6-9     260         Ohio State   
11    Isaiah Thomas  Boston Celtics       4       PG   27    5-9     185         Washington   

        Salary  
0    7730337.0  
1    6796117.0  
2          NaN  
3    1148640.0  
4    5000000.0  
5   12000000.0  
6    1170960.0  
7    2165160.0  
8    1824360.0  
9    3431040.0  
10   2569260.0  
11   6912869.0  

Replacing NaN values in College with 'No College' using fillna()

Program:
nba["College"] = nba["College"].fillna("No College")
print(nba)

Output:
               Name            Team  Number Position  Age Height  Weight            College  \
0     Avery Bradley  Boston Celtics       0       PG   25    6-2     180              Texas   
1       Jae Crowder  Boston Celtics      99       SF   25    6-6     235          Marquette   
2      John Holland  Boston Celtics      30       SG   27    6-5     205  Boston University   
3       R.J. Hunter  Boston Celtics      28       SG   22    6-5     185      Georgia State   
4     Jonas Jerebko  Boston Celtics       8       PF   29   6-10     231         No College   
5      Amir Johnson  Boston Celtics      90       PF   29    6-9     240         No College   
6     Jordan Mickey  Boston Celtics      55       PF   21    6-8     235                LSU   
7      Kelly Olynyk  Boston Celtics      41        C   25    7-0     238            Gonzaga   
8      Terry Rozier  Boston Celtics      12       PG   22    6-2     190         Louisville   
9      Marcus Smart  Boston Celtics      36       PG   22    6-4     220     Oklahoma State   
10  Jared Sullinger  Boston Celtics       7        C   24    6-9     260         Ohio State   
11    Isaiah Thomas  Boston Celtics       4       PG   27    5-9     185         Washington   

        Salary  
0    7730337.0  
1    6796117.0  
2          NaN  
3    1148640.0  
4    5000000.0  
5   12000000.0  
6    1170960.0  
7    2165160.0  
8    1824360.0  
9    3431040.0  
10   2569260.0  
11   6912869.0  

b) Transform data using apply() and map() methods

(i) apply() - label every stock price as Low / Normal / High

Program:
import pandas as pd
s = pd.read_csv("stock.csv").squeeze("columns")

def fun(num):
    if num < 200:
        return "Low"
    elif num >= 200 and num < 400:
        return "Normal"
    else:
        return "High"

new = s.apply(fun)
print(new.head(3))
print(new[1400], new[1500], new[1600])
print(new.tail(3))

Output:
0    Low
1    Low
2    Low
Name: Stock Price, dtype: str
Low Normal Normal
3009    High
3010    High
3011    High
Name: Stock Price, dtype: str

(ii) map() - map Pokemon names to their types

Program:
pokemon_names = pd.read_csv("pokemon.csv", usecols=["Pokemon"]).squeeze("columns")
pokemon_types = pd.read_csv("pokemon.csv", index_col="Pokemon").squeeze("columns")
new = pokemon_names.map(pokemon_types)
print(new)

Output:
0      Grass
1      Grass
2      Grass
3       Fire
4       Fire
5       Fire
6      Water
7      Water
8      Water
9        Bug
10       Bug
11       Bug
12       Bug
13       Bug
14       Bug
15    Normal
16    Normal
17    Normal
Name: Pokemon, dtype: str

c) Detect and filter outliers


Load the data and drop the unnecessary columns

Program:
import pandas as pd
import numpy as np
df = pd.read_csv('uber.csv')
df = df.drop(columns=['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude'])
print(df.head())

Output:
   Unnamed: 0                          key  fare_amount      pickup_datetime  passenger_count
0           0  2015-05-07 19:52:06.0000000        -52.0  2010-08-25 22:23:42                0
1           1  2015-05-07 19:52:06.0000001        499.0  2013-06-02 16:21:58              208
2           2  2015-05-07 19:52:06.0000002        350.0  2011-04-01 09:42:00                0
3           3  2015-05-07 19:52:06.0000003        275.5  2010-09-08 00:37:41                0
4           4  2015-05-07 19:52:06.0000004        180.0  2014-08-06 06:44:14                1

Summary statistics help to spot outliers

Program:
print(df[['fare_amount', 'passenger_count']].describe())

Output:
         fare_amount  passenger_count
count  200000.000000    200000.000000
mean       11.347686         1.719835
std         6.288260         1.433057
min       -52.000000         0.000000
25%         6.870000         1.000000
50%         9.970000         1.000000
75%        14.330000         2.000000
max       499.000000       208.000000

d) Perform vectorized string operations on a Pandas Series


str.upper() on the Team column

Program:
import pandas as pd
data = pd.read_csv("employees.csv")
data["Team"] = data["Team"].str.upper()
print(data.head(13))

Output:
   First Name  Gender  Start Date Last Login Time  Salary  Bonus % Senior Management  \
0     Douglas    Male    8/6/1993        12:42 PM   97308    6.945              True   
1      Thomas    Male   3/31/1996         6:53 AM   61933    4.170              True   
2       Maria  Female   4/23/1993        11:17 AM  130590   11.858             False   
3       Jerry    Male    3/4/2005         1:00 PM  138705    9.340              True   
4       Larry    Male   1/24/1998         4:47 PM  101004    1.389              True   
5     Brandon    Male  10/20/1995        11:49 PM  127963    6.183               NaN   
6     Douglas  Female    7/4/2009         3:32 PM  148888    7.852              True   
7       Henry    Male  12/26/1994         6:10 PM   85016   14.044              True   
8     Brandon    Male   7/21/1995        12:09 PM  117902    1.003              True   
9     Michael  Female  11/16/1986        11:32 AM   41400   15.192             False   
10     Louise  Female   8/18/2000         9:55 AM   81204    7.440             False   
11      Henry  Female   3/11/1990         2:15 PM  135111   11.949              True   
12    Brandon  Female   12/8/1995         7:01 PM  113936   15.469             False   

               Team  
0         MARKETING  
1               NaN  
2           FINANCE  
3           FINANCE  
4   CLIENT SERVICES  
5       ENGINEERING  
6             SALES  
7         MARKETING  
8             LEGAL  
9   CLIENT SERVICES  
10            SALES  
11        MARKETING  
12  HUMAN RESOURCES  

str.lower() on the First Name column

Program:
data = pd.read_csv("employees.csv")
data["First Name"] = data["First Name"].str.lower()
print(data.head(13))

Output:
   First Name  Gender  Start Date Last Login Time  Salary  Bonus % Senior Management  \
0     douglas    Male    8/6/1993        12:42 PM   97308    6.945              True   
1      thomas    Male   3/31/1996         6:53 AM   61933    4.170              True   
2       maria  Female   4/23/1993        11:17 AM  130590   11.858             False   
3       jerry    Male    3/4/2005         1:00 PM  138705    9.340              True   
4       larry    Male   1/24/1998         4:47 PM  101004    1.389              True   
5     brandon    Male  10/20/1995        11:49 PM  127963    6.183               NaN   
6     douglas  Female    7/4/2009         3:32 PM  148888    7.852              True   
7       henry    Male  12/26/1994         6:10 PM   85016   14.044              True   
8     brandon    Male   7/21/1995        12:09 PM  117902    1.003              True   
9     michael  Female  11/16/1986        11:32 AM   41400   15.192             False   
10     louise  Female   8/18/2000         9:55 AM   81204    7.440             False   
11      henry  Female   3/11/1990         2:15 PM  135111   11.949              True   
12    brandon  Female   12/8/1995         7:01 PM  113936   15.469             False   

               Team  
0         Marketing  
1               NaN  
2           Finance  
3           Finance  
4   Client Services  
5       Engineering  
6             Sales  
7         Marketing  
8             Legal  
9   Client Services  
10            Sales  
11        Marketing  
12  Human Resources

