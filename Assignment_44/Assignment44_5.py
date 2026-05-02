import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def Advertising(DatasetPath):

    Border = "-" * 50

    ###############################################################################################
    # Step 1 : Dataset Loading
    ###############################################################################################

    print(Border)
    print("Step 1 : Dataset Loading")
    print(Border) 

    df = pd.read_csv(DatasetPath)

    print("Dataset det loaded successfully...")

    ###############################################################################################
    # Step 2 : Data Cleaning
    ###############################################################################################

    print(Border)
    print("Step 2 : Data Cleaning")
    print(Border) 

    df = df.drop("Unnamed: 0", axis=1)

    print("Missing Values : ")
    print(df.isnull().sum())

    print("The Size of the Dataset",df.shape)

    ###############################################################################################
    # Step 3 : Data Split
    ###############################################################################################

    print(Border)
    print("Step 3 : Data Split")
    print(Border) 


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

    ###############################################################################################
    # Step 4 : Model Selection
    ###############################################################################################

    print(Border)
    print("Step 4 : Model Selection")
    print(Border)

    model = LinearRegression()

    ###############################################################################################
    # Step 5 : Model Training
    ###############################################################################################

    print(Border)
    print("Step 5 : Model Training")
    print(Border)

    model.fit(X_train, Y_train)

    print("Model is Trained")

    ###############################################################################################
    # Step 6 : Model Testing
    ###############################################################################################

    print(Border)
    print("Step 6 : Model Testing")
    print(Border)


    Y_Pred = model.predict(X_test)

    print("Model Testing is done")
 
    ###############################################################################################
    # Step 7 : Values Displayed
    ###############################################################################################

    print(Border)
    print("Step 7 : Values Displayed")
    print(Border)

    print("Actual Values : ")
    print(Y_test)

    print("Predicted Values : ")
    print(Y_Pred)


def main():
    Advertising("Advertising.csv")

if __name__ == "__main__":
    main()
