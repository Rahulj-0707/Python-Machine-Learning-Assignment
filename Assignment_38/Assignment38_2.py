import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset get loaded successfully...")

print("Total Number of Student is :", len(df))

print("Number of students Passed :")
Count = (df['FinalResult'] == 1).sum()
print(Count)

print("Number of Students Failed : ")
Count = (df['FinalResult'] == 0).sum()
print(Count)