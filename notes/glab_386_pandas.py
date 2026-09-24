import pandas as pd
import numpy as np


# declare series
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))

print(ser)
# declare series
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))

# Give it a name attribute
ser.name = 'alphabet'

print(ser)
# Index is specified, corresponding data will be pulled into the series
customer_index = pd.Series(d, index=['a', 'y', 'x'])

print(customer_index)
carlories = {
    'day1': 2200,
    'day2': 2500,
    'day3': 2700,
}
# Series of scalar value. Each index will have the same value
scalar_series = pd.Series(5.0, index=['a', 'b', 'c', 'd', 'e'])

print(scalar_series)
patientID = [101, 102, 103, 104]
name = ['Daniel', 'John', 'Abbi', 'Charlie']
dob = ['2023-01-01', '2024-01-02', '3/10/1987 14045', '13th of October, 2026']

# zip() - function combines lists to make a tuple of tuples
# tuples are an iterator, which is what the DF function takes
pt_df = pd.DataFrame(zip(patientID, name, dob))

print(pt_df)
stocks = ['IBM', 'APPLE', 'TWTTER', 'GE', 'MSFT']
prices = [115.00, 119.14, 19.77, 25.99, 26]
stocks_df = pd.DataFrame({'Stock': stocks, 'Price': prices})
print(stocks_df)
data = [
    {'x': 1, 'y': 2, 'z': 3},
    {'x': 2, 'y': 10, 'z': 15},
    {'x': 4, 'y': 13, 'z': 16}
]
data = [
    {'x': 1, 'y': 2, 'z': 3},
    {'x': 2, 'y': 10, 'z': 15},
    {'x': 4, 'y': 13, 'z': 16}
]

print(pd.DataFrame(data))
data = [
    [1, 2, 3],
    [2, 4, 100],
    [3, 8, 100]
]

print(pd.DataFrame(data, columns=['a', 'b', 'c']))
arr = np.array([[1, 2, 3], [2, 10, 15], [4, 8, 16]])

print(pd.DataFrame(arr, columns=['x', 'y', 'z']))