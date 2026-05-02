import pandas as pd
import matplotlib.pyplot as plt

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

plt.figure()
plt.boxplot(df['Attendance'])

plt.title("Box Plot of Attendance")
plt.ylabel("Attendance")

plt.show()