import pandas as pd

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset get loaded successfully...")

print("Initial entries from the dataset : ")
print(df.head())

print("Last entries from the dataset : ")
print(df.tail())

print("Total Number of rows and columns in the file : ")
print(df.shape)

print("Column Names : ", list(df.columns))

print("Datatype of each column is : ",list(df.dtypes))
