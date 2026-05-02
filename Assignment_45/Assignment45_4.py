import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


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

    # Split the data

    Features = [
        "Alcohol",
        "Malic acid",
        "Ash",
        "Alcalinity of ash",
        "Magnesium",
        "Total phenols",
        "Flavanoids",
        "Nonflavanoid phenols",
        "Color intensity",
        "Hue",
        "OD280/OD315 of diluted wines",
        "Proline"
    ]

    X = df[Features]
    Y = df["Class"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    # Model Selection

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=5,
        random_state=42
    )

    print("Model Successfully Created")

    # Training The Model

    model.fit(X_train, Y_train)
    print("Model training Completed")

    # Model Testing

    Y_Pred = model.predict(X_test)
    print("Model testing is completed")

    print("Actual Answer : ")
    print(Y_test)
    
    print("Predicted Answer : ")
    print(Y_Pred)

if __name__ == "__main__":
    main()