import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score
)

def WinePredictor(DatasetPath):

    Border = "-" * 50
    ###############################################################################################
    # Step 1 : Dataset Loading
    ###############################################################################################

    print(Border)
    print("Step 1 : Dataset Loading")
    print(Border)

    df = pd.read_csv(DatasetPath)
    print("Dataset loaded Successfully...")

    ###############################################################################################
    # Step 2 : Data Cleaning
    ###############################################################################################

    print(Border)
    print("Step 2 : Data Cleaning")
    print(Border)


    print("Missing Values : ")
    print(df.isnull().sum())

    print("Initial values of Dataset : ")
    print(df.head())

    df = df.drop_duplicates()

    print("Columns of the Dataset")
    print(df.columns)

    print("Size of Dataset : ")
    print(df.shape)

    ###############################################################################################
    # Step 3 : Split the data
    ###############################################################################################

    print(Border)
    print("Step 3 : Split the data")
    print(Border)


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

    ###############################################################################################
    # Step 4 : Model Selection
    ###############################################################################################

    print(Border)
    print("Step 4 : Model Selection")
    print(Border)

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=5,
        random_state=42
    )

    print("Model Successfully Created")

    ###############################################################################################
    # Step 5 : Training The Model
    ###############################################################################################

    print(Border)
    print("Step 5 : Training The Model")
    print(Border)

    model.fit(X_train, Y_train)
    print("Model training Completed")

    ###############################################################################################
    # Step 6 : Model Testing
    ###############################################################################################

    print(Border)
    print("Step 6 : Model Testing")
    print(Border)

    Y_Pred = model.predict(X_test)
    print("Model testing is completed")

    print("Actual Answer : ")
    print(Y_test)
    
    print("Predicted Answer : ")
    print(Y_Pred)

    ###############################################################################################
    # Step 7 : Calculate Accuracy
    ###############################################################################################

    print(Border)
    print("Step 7 : Calculate Accuracy")
    print(Border)

    Accuracy = accuracy_score(Y_test, Y_Pred)
    print("Accuracy of the Model is : ", Accuracy * 100)


def main():

    WinePredictor("WinePredictor.csv")    

if __name__ == "__main__":
    main()