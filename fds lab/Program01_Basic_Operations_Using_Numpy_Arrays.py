
a) Create NumPy arrays from Python Data Structures, Intrinsic NumPy objects and Random Functions

Get the data type of an array object

Program:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

Output:
int64

Get the data type of an array containing strings

Program:
import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

Output:
<U6

Create an array with data type string

Program:
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

Output:
[b'1' b'2' b'3' b'4']
|S1

Create an array with data type 4 bytes integer

Program:
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

Output:
[1 2 3 4]
int32

Change data type from float to integer using 'i' as parameter value

Program:
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

Output:
[1 2 3]
int32

Change data type from float to integer using int as parameter value

Program:
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

Output:
[1 2 3]
int64

Change data type from integer to boolean

Program:
import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

Output:
[ True False  True]
bool

Demonstrate the working of array()

Program:
import array
arr = array.array('i', [1, 2, 3])
print("The new created array is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

Output:
The new created array is : 1 2 3 

Intrinsic NumPy array creation: arange()

Program:
import numpy as np
arr = np.arange(10)
print(arr)

Output:
[0 1 2 3 4 5 6 7 8 9]

arange() with start, stop and dtype

Program:
import numpy as np
arr = np.arange(2, 10, dtype=float)
print(arr)

Output:
[2. 3. 4. 5. 6. 7. 8. 9.]

arange() with a float step

Program:
import numpy as np
arr = np.arange(2, 3, 0.1)
print(arr)

Output:
[2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9]

Generate a random integer from 0 to 100

Program:
from numpy import random
x = random.randint(100)
print(x)

Output:
78

Generate a random float from 0 to 1

Program:
from numpy import random
x = random.rand()
print(x)

Output:
0.7119991802189952

Generate a 1-D array containing 5 random integers from 0 to 100

Program:
from numpy import random
x = random.randint(100, size=(5))
print(x)

Output:
[92  8 40 81 20]

Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100

Program:
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)

Output:
[[ 7 83 94 68 34]
 [ 4 67 46 67 89]
 [18 31 64  3 40]]

Generate a 1-D array containing 5 random floats

Program:
from numpy import random
x = random.rand(5)
print(x)

Output:
[0.68207691 0.07618266 0.52807871 0.01684275 0.46555307]

b) Manipulation of NumPy arrays - Indexing, Slicing, Reshaping, Joining and Splitting

Indexing: get the first element

Program:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])

Output:
1

Indexing: get the third and fourth elements and add them

Program:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

Output:
7

Slicing: elements from index 1 to index 5

Program:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

Output:
[2 3 4 5]

Slicing: from the beginning to index 4

Program:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

Output:
[1 2 3 4]

Reshaping: 1-D array with 12 elements into a 2-D array

Program:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

Output:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

Reshaping: 1-D array with 12 elements into a 3-D array

Program:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

Output:
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]

Reshaping: 1-D array with 8 elements to a 3-D array (unknown dimension -1)

Program:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

Output:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]

Reshaping: flatten the array into 1-D

Program:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

Output:
[1 2 3 4 5 6]

Joining: join two arrays

Program:
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

Output:
[1 2 3 4 5 6]

Joining: two 2-D arrays along axis=1

Program:
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

Output:
[[1 2 5 6]
 [3 4 7 8]]

Joining arrays using stack functions

Program:
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

Output:
[[1 4]
 [2 5]
 [3 6]]

Splitting: split the array in 3 parts

Program:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

Output:
[array([1, 2]), array([3, 4]), array([5, 6])]

Splitting: split the array in 4 parts

Program:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

Output:
[array([1, 2]), array([3, 4]), array([5]), array([6])]

Splitting: access the split arrays

Program:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

Output:
[1 2]
[3 4]
[5 6]

Splitting: 2-D array into three 2-D arrays

Program:
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

Output:
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]]), array([[ 9, 10],
       [11, 12]])]

Splitting: 2-D array into three 2-D arrays along axis=1

Program:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

Output:
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]

c) Computation on NumPy arrays using Universal Functions and Mathematical methods


Create your own ufunc for addition

Program:
import numpy as np
def myadd(x, y):
    return x + y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

Output:
[6 8 10 12]

Check if a function is a ufunc

Program:
import numpy as np
print(type(np.add))

Output:
<class 'numpy.ufunc'>

Use an if statement to check if the function is a ufunc

Program:
import numpy as np
if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')

Output:
add is ufunc

Compute the values sin(2*pi*x)

Program:
import numpy as np
x = np.arange(0, 1.25, 0.25)
print(x)
y = np.sin(2 * np.pi * x)
print(y)

Output:
[0.   0.25 0.5  0.75 1.  ]
[ 0.  1.  0. -1. -0.]

Convert all values in an array to radians

Program:
import numpy as np
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

Output:
[1.57079633 3.14159265 4.71238898 6.28318531]

Find the angle of 1.0

Program:
import numpy as np
x = np.arcsin(1.0)
print(x)

Output:
1.5707963267948966

d) Import a CSV file and perform various Statistical and Comparison operations on rows/columns

Create a NumPy array with the same number of rows and columns as the CSV

Program:
import csv
import numpy as np
with open("winequality-red.csv", 'r') as f:
    wines = list(csv.reader(f, delimiter=";"))
wines = np.array(wines[1:], dtype=float)
print(wines.shape)
wines

Output:
(1599, 12)
array([[ 7.4 ,  0.7 ,  0.  , ...,  0.56,  9.4 ,  5.  ],
       [ 7.8 ,  0.88,  0.  , ...,  0.68,  9.8 ,  5.  ],
       [ 7.3 ,  0.45,  0.07, ...,  0.75, 11.2 ,  7.  ],
       ...,
       [10.2 ,  0.53,  0.77, ...,  0.62, 10.7 ,  7.  ],
       [ 6.8 ,  0.87,  0.  , ...,  0.85, 10.7 ,  5.  ],
       [ 8.9 ,  0.48,  0.16, ...,  0.52, 12.1 ,  6.  ]], shape=(1599, 12))

Calculate the median value of a column

Program:
import pandas as pd
df = pd.read_csv('winequality-red.csv', delimiter=';')
fixedacidity_median = df['fixed acidity'].median()
print('fixedacidity median =', fixedacidity_median)

Output:
fixedacidity median = 8.3

Comparison: which wines have a quality rating higher than 5

Program:
wines[:, 11] > 5

Output:
array([False, False,  True, ...,  True, False,  True], shape=(1599,))

Comparison: do any wines have a quality rating equal to 10

Program:
wines[:, 11] == 10

Output:
array([False, False, False, ..., False, False, False], shape=(1599,))

Select rows in wines where the quality is over 7

Program:
high_quality = wines[:, 11] > 7
wines[high_quality, :][:3, :]

Output:
array([[ 9.3    ,  0.49   ,  0.45   ,  3.     ,  0.083  ,  1.     , 72.     ,  0.998  ,
         3.35   ,  0.77   , 12.7    ,  8.     ],
       [ 9.1    ,  0.51   ,  0.29   ,  2.3    ,  0.115  ,  1.     , 50.     ,  0.99967,
         3.5    ,  0.88   , 10.8    ,  8.     ],
       [ 8.6    ,  0.68   ,  0.47   ,  3.2    ,  0.108  ,  1.     , 34.     ,  0.99868,
         2.98   ,  0.56   , 11.3    ,  8.     ]])

Look for wines with a lot of alcohol and high quality

Program:
high_quality_and_alcohol = (wines[:, 10] > 10) & (wines[:, 11] > 7)
wines[high_quality_and_alcohol, 10:]

Output:
array([[12.7,  8. ],
       [10.8,  8. ],
       [11.3,  8. ],
       [11.5,  8. ],
       [11.7,  8. ],
       [11.8,  8. ],
       [12.6,  8. ],
       [10.5,  8. ],
       [11.9,  8. ],
       [10.2,  8. ],
       [12.1,  8. ],
       [12.4,  8. ],
       [11.3,  8. ],
       [11.7,  8. ],
       [13.8,  8. ],
       [11.4,  8. ],
       [12.6,  8. ],
       [12.4,  8. ],
       [12.1,  8. ],
       [12.3,  8. ],
       [13. ,  8. ],
       [13.4,  8. ],
       [11.9,  8. ],
       [10.4,  8. ],
       [12.2,  8. ],
       [12.5,  8. ],
       [10.3,  8. ],
       [13.3,  8. ],
       [11.4,  8. ],
       [11.7,  8. ],
       [11. ,  8. ],
       [12.8,  8. ],
       [10.9,  8. ],
       [10.7,  8. ],
       [11.2,  8. ]])

e) Load an image file and do crop and flip operations using NumPy indexing



Program:
import imageio.v2 as iio
import matplotlib.pyplot as plt
img = iio.imread("emma_stone.jpg")
iio.imwrite("emma_stone.jpg", img)
plt.imshow(img)
plt.show()



Program:
from PIL import Image
Image1 = Image.open('emma_stone.jpg')
croppedIm = Image1.crop((130, 120, 200, 200))
plt.imshow(croppedIm)
plt.show()


Program:
img0 = img.copy()
for i in range(img0.shape[0] // 2):
    c = img0[i, :, :].copy()
    img0[i, :, :] = img0[img0.shape[0] - i - 1, :, :]
    img0[img0.shape[0] - i - 1, :, :] = c
plt.imshow(img0)
plt.show()

