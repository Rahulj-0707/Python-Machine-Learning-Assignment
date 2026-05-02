import pandas as pd
import matplotlib.pyplot as plt

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

plt.figure()
plt.hist(df['StudyHours'], bins=10)

plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()