import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():

    # Data Loading    
    DatasetPath = "Advertising.csv"

    df = pd.read_csv(DatasetPath)

    print("Dataset det loaded successfully...")

    # Data Cleaning

    df = df.drop("Unnamed: 0", axis=1)

    print("Missing Values : ")
    print(df.isnull().sum())

    print("The Size of the Dataset",df.shape)


if __name__ == "__main__":
    main()
