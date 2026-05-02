import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    DatasetPath = "PlayPredictor.csv"

    df = pd.read_csv(DatasetPath)

    print("Original Dataset\n")
    print(df)

    encoder = LabelEncoder()

    df["Whether"] = encoder.fit_transform(df["Whether"])
    df["Temperature"] = encoder.fit_transform(df["Temperature"])

    print("Encoded Dataset")

    print(df)

if __name__ == "__main__":
    main()