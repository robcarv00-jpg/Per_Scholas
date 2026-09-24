patientID = [101, 102, 103, 104]
name = ['Daniel', 'John', 'Abbi', 'Charlie']
dob = ['2023-01-01', '2024-01-02', '3/10/1987 14045', '13th of October, 2026']

# zip() - function combines lists to make a tuple of tuples
# tuples are an iterator, which is what the DF function takes
pt_df = pd.DataFrame(zip(patientID, name, dob))