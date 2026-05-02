import pandas as pd
import matplotlib.pyplot as plt

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

plt.figure()
plt.scatter(df['StudyHours'], df['PreviousScore'])
plt.grid()
plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.show()