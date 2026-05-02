import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def main():
    DatasetPath = "PlayPredictor.csv"

    df = pd.read_csv(DatasetPath)

    print("Original Dataset\n")
    print(df)

    # Feature Encoding

    encoder = LabelEncoder()

    df["Whether"] = encoder.fit_transform(df["Whether"])
    df["Temperature"] = encoder.fit_transform(df["Temperature"])

    print("Encoded Dataset")

    print(df)

    # Data Spliting And Training

    Feature_col = [
        "Whether",
        "Temperature"
    ]

    X = df[Feature_col]
    Y = df["Play"]

    # Model Selection

    model = KNeighborsClassifier(
        n_neighbors=3,
    )

    print("Model Successfully created...")

    # Train the Model 

    model.fit(X, Y)
    print("Model Training is Complted...")

if __name__ == "__main__":
    main()