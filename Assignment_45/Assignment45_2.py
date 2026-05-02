import pandas as pd

def main():

    # Dataset loading

    DatasetPath = "WinePredictor.csv"

    df = pd.read_csv(DatasetPath)

    print("Dataset loaded Successfully...")

    # Data Cleaning

    print("Missing Values : ")
    print(df.isnull().sum())

    print("Initial values of Dataset : ")
    print(df.head())

    df = df.drop_duplicates()

    print("Columns of the Dataset")
    print(df.columns)

    print("Size of Dataset : ")
    print(df.shape)

if __name__ == "__main__":
    main()