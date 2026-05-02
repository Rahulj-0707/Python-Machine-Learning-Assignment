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

    # Data Split

    Features = [
        "TV",
        "radio",
        "newspaper"
    ]

    X = df[Features]
    Y = df["sales"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    # Model Selection

    model = LinearRegression()

    # Model Training

    model.fit(X_train, Y_train)

    print("Model is Trained")

    # Model Testing

    Y_Pred = model.predict(X_test)

    print("Model Testing is done")
    

if __name__ == "__main__":
    main()
