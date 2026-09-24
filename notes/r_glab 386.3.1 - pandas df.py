import numpy as np
import pandas as pd 

student_dict = {
    'Name': ['Joe', 'Nat', 'Harry'],
    'Age': [20, 21, 28],
    'Marks': [85.10, 77.80, 91.54]
}
student_df = pd.DataFrame(student_dict)
print(student_df)

data = {
    'Product': ['Laptop', 'Tablet', 'Phone'],
    'Price': [1200, 300, 800],
    'Quantity': [50, 150, 100]
}
product_df = pd.DataFrame(data)
print(product_df)   
patientID = [101, 102, 103, 104]
name = ['Daniel', 'John', 'Abbi', 'Charlie']
dob = ['2023-01-01', '2024-01-02', '3/10/1987 14045', '13th of October, 2026']
patient_df = pd.DataFrame({
    'PatientID': patientID,
    'Name': name,
    'DOB': dob
})
print(patient_df)