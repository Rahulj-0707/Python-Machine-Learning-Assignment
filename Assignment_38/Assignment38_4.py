import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

Count = len(df)

print("Number of students Passed :")
pass_Count = (df['FinalResult'] == 1).sum()
print(pass_Count)

print("Number of Students Failed : ")
fail_Count = (df['FinalResult'] == 0).sum()
print(fail_Count)

pass_percentage = (pass_Count / Count) * 100
print("Pass Percentage is : ",pass_percentage)

fail_pecentage = (fail_Count / Count) * 100
print("Fail Percentage is : ",fail_pecentage)