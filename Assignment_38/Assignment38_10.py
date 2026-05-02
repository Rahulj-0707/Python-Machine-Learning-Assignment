import pandas as pd
import matplotlib.pyplot as plt

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

passed = df[df['FinalResult'] == 1]['SleepHours']
failed = df[df['FinalResult'] == 0]['SleepHours']

plt.figure()
plt.boxplot([failed, passed])

plt.xticks([1, 2], ['Failed', 'Passed'])
plt.title("Sleep Hours vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Sleep Hours")

plt.show()