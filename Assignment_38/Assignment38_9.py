import pandas as pd
import matplotlib.pyplot as plt

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

passed = df[df['FinalResult'] == 1]['AssignmentsCompleted']
failed = df[df['FinalResult'] == 0]['AssignmentsCompleted']


plt.figure()
plt.boxplot([failed, passed])

plt.xticks([1, 2], ['Failed', 'Passed'])
plt.title("Assignment Completed vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Assignments Completed")

plt.show()