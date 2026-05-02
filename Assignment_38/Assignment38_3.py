import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset get loaded successfully...")

Avg = df['StudyHours'].mean()
print("Average of StudyHours is : ",Avg)

Avg = df['Attendance'].mean()
print("Average of Attendance is : ",Avg)

Max = df['PreviousScore'].max()
print("The Maximun PreviousScore is : ", Max)

Min = df['SleepHours'].min()
print("Minimum SleepHours is : ",Min)