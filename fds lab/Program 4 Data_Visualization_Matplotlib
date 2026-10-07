

Line Plot


Line plot of Age and Marks per student

Program:
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
headers = ['Name', 'Age', 'Marks']
df = pd.read_csv('student.csv', names=headers)
df.set_index('Name').plot()
plt.show()


Bar Plots


Bar plot of students over the years

Program:
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.bar(X, Y, color='g')
plt.title("Students over 11 Years")
plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.show()

[Image: images/Data_Visualization_Matplotlib_Figure_2.png]

Histograms

Histograms of every column of the diabetes data

Program:
import pandas as pd
data = pd.read_csv("diabetes.csv")
print(data.head())
data.hist(figsize=(10, 10), bins=10)
plt.show()

Output:
   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  \
0            6    148.0           72.0           35.0      0.0  33.6                     0.627   
1            1     85.0           66.0           29.0      0.0  26.6                     0.351   
2            6    117.0           86.0           32.0      0.0  29.0                     0.173   
3            1    120.0            0.0            0.0      0.0  32.6                     0.612   
4            1    177.0           63.0            0.0      0.0  36.6                     0.618   

   Age  Outcome  
0   50        1  
1   31        0  
2   38        0  
3   64        0  
4   39        1  


Density Plots

Density plot of the Age attribute

Program:
import pandas as pd
import matplotlib.pyplot as plt
dataFrame = pd.read_csv("Cricketers2.csv")
dataFrame.Age.plot.density(color='green')
plt.title('Density plot = Age')
plt.show()


Scatter Plots

Scatter plot of tree locations (Latitude vs Longitude)

Program:
import pandas as pd
df = pd.read_csv('Street_Tree_List.csv', parse_dates=['PlantDate'])
df['PlantYears'] = (pd.to_datetime('today') - df['PlantDate']) / pd.Timedelta(days=365)
df['qSpecies'] = df['qSpecies'].apply(lambda x: x.split(" ")[0])
df = df[['Latitude', 'Longitude', 'PlantYears', 'qSpecies']]
df.dropna(subset=['PlantYears', 'Latitude'], inplace=True)
print(df.head())
df.plot.scatter(x='Longitude', y='Latitude', ylim=(37.69, 37.82))
plt.show()

Output:
    Latitude   Longitude  PlantYears    qSpecies
0  37.736095 -122.407330   18.264364    Platanus
4  37.809313 -122.480785   30.256145  Eriobotrya
5  37.757899 -122.432066   11.768474    Platanus
6  37.788809 -122.431533   26.299980      Prunus
7  37.754161 -122.373572   38.245186    Platanus


